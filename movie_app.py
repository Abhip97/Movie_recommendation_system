import streamlit as st
import requests
import pickle

movies = pickle.load(open('movies.pkl','rb'))
similarity = pickle.load(open('similarity1.pkl','rb'))

movies_list = movies['title'].values

st.title("Movie recommendation System")
selectedvalue = st.selectbox("Select a movie", movies_list)

def fetch_poster(movie_id):
    url= "https://api.themoviedb.org/3/movie/{}?api_key=35d5d3b8baeb1a6fb1ee9e81d615eecc&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/"+poster_path
    return full_path



def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distance = sorted(list(enumerate(similarity[index])),reverse=True,key = lambda x:x[1]) # use enumerate to fix the index and sort in descending order to dind most simialr movies
    recommend_movie =[]
    recommend_poster=[]
    for i in distance[1:6]:
        movies_id = movies.iloc[i[0]]['movie_id']
        recommend_movie.append(movies.iloc[i[0]].title)
        recommend_poster.append(fetch_poster(movies_id))
    return recommend_movie, recommend_poster


if st.button("Recommend"):
    movie_name,movie_poster = recommend(selectedvalue)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(movie_name[0])
        st.image(movie_poster[0])
    with col2:
        st.text(movie_name[1])
        st.image(movie_poster[1])
    with col3:
        st.text(movie_name[2])
        st.image(movie_poster[2])
    with col4:
        st.text(movie_name[3])
        st.image(movie_poster[3])
    with col5:
        st.text(movie_name[4])
        st.image(movie_poster[4])

