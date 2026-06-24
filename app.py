import pandas as pd
import streamlit as st
from sentence_transformers import SentenceTransformer
import faiss

df = pd.read_csv('movie.csv')
df = df[['original_title','overview','genres','keywords','directors','cast','poster_path','spoken_languages','averageRating']]

st.set_page_config(
    page_title="MovieGPT",
    page_icon="🎬",
    layout="wide"
)

st.title("🎬 MovieGPT")
st.caption("RAG-Powered Movie Recommendation System")

@st.cache_data
def create_documents(df):
    documents = []
    for _, row in df.iterrows():
        doc = f"""
        Genres: {row['genres']}
        Keywords:{row['keywords']}
        Overview:{row['overview']}
        Director:{row['directors']}
        Cast:{row['cast']}
        """
        documents.append(doc)

    return documents
document = create_documents(df)
@st.cache_data
def create_metadata(df):
    metadata = []
    for _, row in df.iterrows():
        metadata.append({
            'Title': row['original_title'],
            'overview': row['overview'],
            'genres': row['genres'],
            'directors': row['directors'],
            'poster_url':
                "https://image.tmdb.org/t/p/w500" + row['poster_path'],
            'Language': row['spoken_languages'],
            'IMDB': row['averageRating']
        })

    return metadata
metadata = create_metadata(df)

@st.cache_resource
def load_model():
    model = SentenceTransformer('BAAI/bge-base-en-v1.5')

    return model
model = load_model()

@st.cache_data
def create_embedding(document):
    return model.encode(document,normalize_embeddings=True).astype("float32")

@st.cache_resource
def create_index(movie_embedding):
    index = faiss.IndexFlatIP(movie_embedding.shape[1])
    index.add(movie_embedding)
    return index

movie_embedding = create_embedding(document)
index = create_index(movie_embedding)


query = st.text_input(
    "Search Movies",
    placeholder="Dream manipulation, space survival, romantic drama..."
)

button = st.button('Search',width = 'stretch')

if query and button:
    
    query_embedding = model.encode(
            "Represent this sentence for retrieving relevant movies: " + query,
            normalize_embeddings=True
        ).astype("float32")
    distance, indices = index.search(
    query_embedding.reshape(1,-1),
        k=10
    )
    retrieved_movies = [metadata[idx] for idx in indices[0]]

    st.subheader("Recommended Movies")

    for movie in retrieved_movies:
        with st.container(border=True):

            col1, col2 = st.columns([1,2])

            with col1:
                st.image(movie['poster_url'], width=200)

            with col2:
                st.subheader(movie['Title'])
                st.write(movie['overview'])
                st.write(f"🎭 Genres : {movie['genres']}")
                st.write(f"🎬 Director : {movie['directors']}")
                st.write(f"🌎 Language : {movie['Language']}")
                st.write(f"⭐ IMDB : {movie['IMDB']}")
            