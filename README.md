# 🎬 MovieGPT: RAG-Powered Movie Recommendation System

MovieGPT is an AI-powered movie recommendation system that uses **semantic search** and **vector similarity** to recommend movies based on natural language queries. Instead of relying on keyword matching, MovieGPT leverages **BGE embeddings** and **FAISS vector search** to retrieve semantically relevant movies and display them with posters and metadata through an interactive Streamlit interface.

---

## 🚀 Features

* 🔍 Semantic movie search using natural language
* 🧠 BGE Embeddings (`BAAI/bge-base-en-v1.5`)
* ⚡ FAISS vector database for fast similarity search
* 🎬 Movie posters and metadata display
* 📚 Retrieval-Augmented Generation (RAG) workflow
* 🌐 Interactive Streamlit web application
* 🎭 Genre, overview, language, and IMDb rating information
* 📈 Top-K movie retrieval

---

## 🏗️ Architecture

```text
User Query
     ↓
BGE Embedding Model
     ↓
FAISS Vector Search
     ↓
Top-K Relevant Movies
     ↓
Metadata Retrieval
     ↓
Movie Posters + Details
```

---

## 🛠 Tech Stack

* Python
* Streamlit
* Pandas
* Sentence Transformers
* FAISS

---

## 📂 Project Structure

```text
MovieGPT/
│
├── app.py
├── movie.csv
├── requirements.txt
├── README.md
├── .gitignore
```

---

## 📷 Preview

---

## 💡 Example Queries

```text
dream manipulation and subconscious mind

space survival and humanity exploration

romantic story between strangers in space

superhero vigilante fighting crime

alien invasion and first contact

Christopher Nolan movies

time travel and paradoxes

animated family adventure
```

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/yourusername/MovieGPT-RAG-Movie-Recommendation-System.git
```

### Move into the project directory

```bash
cd MovieGPT-RAG-Movie-Recommendation-System
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the application

```bash
streamlit run app.py
```

---

## 🧠 How It Works

1. User enters a natural language query.
2. The query is converted into vector embeddings using **BGE Base v1.5**.
3. FAISS performs similarity search on movie embeddings.
4. Top relevant movies are retrieved.
5. Metadata and posters are displayed through Streamlit.

---

## 🔮 Future Improvements

* Cross-Encoder reranking for better recommendations
* LLM-generated explanations ("Why recommended?")
* Genre and language filters
* IMDb rating filters
* Netflix-style UI cards
* User watchlist and favorites
* Deploy with Streamlit Community Cloud

---

## 📊 Skills Demonstrated

* Retrieval-Augmented Generation (RAG)
* Semantic Search
* Vector Databases
* Sentence Transformers
* FAISS Similarity Search
* Streamlit Application Development
* Data Processing with Pandas
* Information Retrieval

---

## ⭐ If you found this project useful, consider giving it a star!
