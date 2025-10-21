# Gemini LLM Application

A comprehensive collection of AI-powered applications built using Google's Gemini LLM and various AI frameworks. This repository contains multiple Streamlit applications showcasing different use cases of generative AI, from document processing to automated content creation.

## 🚀 Features

### Core Applications
- **Basic Q&A Chat** - Simple conversational AI interface
- **Vision Analysis** - Image description and analysis using Gemini Vision
- **Chat History** - Interactive chat with conversation memory
- **Invoice Extractor** - Multi-language invoice processing
- **PDF Chat** - Chat with multiple PDF documents
- **Document Q&A** - Question answering from document collections
- **Text-to-SQL** - Natural language to SQL query conversion
- **ATS Resume Analyzer** - Application Tracking System for resume evaluation
- **Health Management** - Nutrition analysis from food images
- **YouTube Summarizer** - Automatic video transcript summarization

### CrewAI Integration
- **Blog Content Generation** - Automated blog writing from YouTube channels
- **News Research & Writing** - AI-powered news article creation
- **Multi-Agent Workflows** - Collaborative AI agent systems

## 📁 Project Structure

```
├── 1-app.py                 # Basic Gemini Q&A application
├── 2-vision.py              # Vision analysis application
├── 3-qachat.py              # Chat with history
├── 4-invoice-extractor.py   # Invoice processing
├── 5-chatpdf.py             # PDF chat application
├── 6-documentqa.py          # Document Q&A system
├── 7-text2sql.py            # Natural language to SQL
├── 8-ats.py                 # ATS resume analyzer
├── 9-health.py              # Health/nutrition analyzer
├── 10-summarizer.py         # YouTube video summarizer
├── main.py                  # Main application entry
├── sql.py                   # Database setup script
├── crewai/                  # CrewAI implementations
│   ├── agents.py            # YouTube content agents
│   ├── tasks.py             # Content creation tasks
│   ├── tools.py             # YouTube search tools
│   ├── crew.py              # Crew orchestration
│   └── gemini/              # Gemini-powered crew
│       ├── agents.py        # News research agents
│       ├── tasks.py         # Research tasks
│       ├── tools.py         # Search tools
│       └── crew.py          # Gemini crew setup
├── faiss_index/             # Vector database storage
└── us_census/               # Sample documents
```

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/gemini-llm-application.git
   cd gemini-llm-application
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   Create a `.env` file in the root directory:
   ```env
   GOOGLE_API_KEY=your_google_api_key
   GROQ_API_KEY=your_groq_api_key
   OPENAI_API_KEY=your_openai_api_key
   SERPER_API_KEY=your_serper_api_key
   GENAI_API_KEY=your_genai_api_key
   ```

## 🚀 Usage

### Running Individual Applications

Each application can be run independently using Streamlit:

```bash
# Basic Q&A
streamlit run 1-app.py

# Vision Analysis
streamlit run 2-vision.py

# PDF Chat
streamlit run 5-chatpdf.py

# Text-to-SQL
streamlit run 7-text2sql.py

# YouTube Summarizer
streamlit run 10-summarizer.py
```

### Database Setup

Initialize the SQLite database for text-to-SQL functionality:

```bash
python sql.py
```

### CrewAI Workflows

Run automated content creation workflows:

```bash
# YouTube blog generation
cd crewai
python crew.py

# News research and writing
cd gemini
python crew.py
```

## 📊 Applications Overview

### 1. Basic Chat ([`1-app.py`](1-app.py))
Simple Q&A interface using Gemini Pro model.

### 2. Vision Analysis ([`2-vision.py`](2-vision.py))
Upload images and get detailed descriptions using Gemini Vision.

### 3. Interactive Chat ([`3-qachat.py`](3-qachat.py))
Conversational AI with persistent chat history.

### 4. Invoice Extractor ([`4-invoice-extractor.py`](4-invoice-extractor.py))
Extract and analyze invoice data from images in multiple languages.

### 5. PDF Chat ([`5-chatpdf.py`](5-chatpdf.py))
Upload multiple PDFs and chat with their content using RAG.

### 6. Document Q&A ([`6-documentqa.py`](6-documentqa.py))
Question-answering system for document collections with FAISS vector search.

### 7. Text-to-SQL ([`7-text2sql.py`](7-text2sql.py))
Convert natural language queries to SQL and execute them on a sample database.

### 8. ATS Resume Analyzer ([`8-ats.py`](8-ats.py))
Analyze resumes against job descriptions with matching scores and suggestions.

### 9. Health Analyzer ([`9-health.py`](9-health.py))
Analyze food images to calculate calories and nutritional information.

### 10. YouTube Summarizer ([`10-summarizer.py`](10-summarizer.py))
Generate detailed notes and summaries from YouTube video transcripts.

## 🤖 CrewAI Integration

The project includes sophisticated multi-agent workflows:

- **Blog Creation Crew** ([`crewai/crew.py`](crewai/crew.py)): Automated blog writing from YouTube content
- **News Research Crew** ([`crewai/gemini/crew.py`](crewai/gemini/crew.py)): AI-powered news research and article writing

## 🔧 Key Dependencies

- **Streamlit** - Web application framework
- **Google GenerativeAI** - Gemini model integration
- **LangChain** - LLM application framework
- **CrewAI** - Multi-agent AI workflows
- **FAISS** - Vector similarity search
- **PyPDF2** - PDF processing
- **SQLite3** - Database operations

## 📝 Configuration

### API Keys Required

- **Google API Key**: For Gemini models access
- **Groq API Key**: For alternative LLM access
- **OpenAI API Key**: For CrewAI workflows
- **Serper API Key**: For web search capabilities

### Model Configuration

The applications use various Gemini models:
- `gemini-2.5-flash` - Primary model for most applications
- `models/embedding-001` - For text embeddings

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙋‍♂️ Support

For questions and support, please open an issue in the GitHub repository.

## 🚀 Future Enhancements

- [ ] Add authentication and user management
- [ ] Implement more document formats support
- [ ] Add multilingual support
- [ ] Create Docker containerization
- [ ] Add comprehensive testing suite
- [ ] Implement caching mechanisms
- [ ] Add monitoring and logging

---

**Note**: Make sure to keep your API keys secure and never commit them to the repository. Always use environment variables or secure secret management systems.
