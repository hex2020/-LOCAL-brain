# -LOCAL-brain
In an era of AI privacy leaks and data harvesting, we provide Privacy by Design. We empower users with the world's most advanced AI models while ensuring their most sensitive secrets stay behind their own firewall. Zero internet. Zero leaks. Unlimited Queries.
🧠 Local Brain: Private & Offline AI Knowledge Base
Local Brain is a high-performance, 100% offline RAG (Retrieval-Augmented Generation) application designed for students and researchers. It allows you to chat with massive PDF documents (800+ pages) without ever sending data to the cloud.
🚀 Key Features
 * 100% Privacy: All processing happens on your local CPU. Zero data leaves your machine.
 * Zero Latency/Cost: No API keys or internet required. Works in flight mode or remote areas.
 * Ultra-Fast Indexing: Uses PyMuPDF and RAM-based vector storage to analyze documents 10x faster than standard tools.
 * Dual-Mode Intelligence: Choose between Turbo Mode (Instant sampling for massive files) or Deep Scan (High-precision analysis).
🛠️ Tech Stack
 * AI Models: Llama 3.2:1b (via Ollama) & Nomic-Embed-Text
 * Frontend: Streamlit (Responsive Web UI)
 * Orchestration: LangChain
 * Vector DB: ChromaDB (In-Memory)
 * Engine: PyMuPDF (High-speed document parsing)
📥 Prerequisites
 * Install Ollama.
 * Run these commands in your terminal:
   ollama pull llama3.2:1b
ollama pull nomic-embed-text

⚡ Quick Start
 * Clone this repository.
 * Windows: Double-click run_windows.bat.
 * Mac/Linux: Run bash run_mac.sh.
 * Upload your PDFs and start chatting with your data!
Built with focus on speed, privacy, and accessibility.
