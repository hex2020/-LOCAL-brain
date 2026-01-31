import os, tempfile, streamlit as st
try:
    import pysqlite3, sys
    sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')
except ImportError: pass

from langchain_community.document_loaders import PyMuPDFLoader
from langchain_ollama import OllamaEmbeddings, ChatOllama
from langchain_chroma import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter

def main():
    st.set_page_config(page_title="Local Brain Turbo", page_icon="🧠", layout="wide")
    st.title("🧠 Local Brain: ask your computer(offline)")
    
    try:
        llm = ChatOllama(model="llama3.2:1b", temperature=0, num_thread=8)
        embed = OllamaEmbeddings(model="nomic-embed-text")
    except:
        st.error("Ollama not running!"); return

    with st.sidebar:
        st.header("⚡ Turbo Settings")
        mode = st.radio("Mode", ["🚀 Instant Turbo (Sampling)", "🔍 Deep Scan (Full)"])
        uploaded_files = st.file_uploader("Upload PDFs", type="pdf", accept_multiple_files=True)
        if st.button("Reset System"):
            for key in ["vs", "msgs"]: st.session_state.pop(key, None)
            st.rerun()

    if uploaded_files:
        if "vs" not in st.session_state:
            all_docs = []
            progress_bar = st.progress(0)
            status_text = st.empty()
            
            for i, up in enumerate(uploaded_files):
                status_text.text(f"Reading file {i+1}/{len(uploaded_files)}...")
                with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as f:
                    f.write(up.getvalue()); path = f.name
                
                loader = PyMuPDFLoader(path)
                docs = loader.load()
                if mode == "🚀 Instant Turbo (Sampling)" and len(docs) > 50:
                    docs = docs[::3] # Sample every 3rd page for massive speed
                all_docs.extend(docs)
                progress_bar.progress((i + 1) / len(uploaded_files) * 0.5)

            status_text.text("Creating Search Index (This is the heavy part)...")
            c_size = 4000 if mode == "🚀 Instant Turbo (Sampling)" else 1000
            splits = RecursiveCharacterTextSplitter(chunk_size=c_size, chunk_overlap=50).split_documents(all_docs)
            
            st.session_state.vs = Chroma.from_documents(documents=splits, embedding=embed)
            progress_bar.progress(1.0)
            status_text.text("Done! Ask your questions below.")
        
        retriever = st.session_state.vs.as_retriever(search_kwargs={"k": 2})
        if "msgs" not in st.session_state: st.session_state.msgs = []
        for m in st.session_state.msgs:
            with st.chat_message(m["role"]): st.markdown(m["content"])
            
        if p := st.chat_input("Ask anything..."):
            st.session_state.msgs.append({"role": "user", "content": p})
            with st.chat_message("user"): st.markdown(p)
            with st.chat_message("assistant"):
                ctx = "\n".join([d.page_content for d in retriever.invoke(p)])
                res = llm.invoke(f"Context: {ctx}\n\nQuestion: {p}").content
                st.markdown(res)
            st.session_state.msgs.append({"role": "assistant", "content": res})

if __name__ == "__main__": main()