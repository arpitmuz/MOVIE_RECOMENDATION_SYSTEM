import streamlit as st
import pickle
import pandas as pd
import numpy as np
import requests

def fetch_poster(movie_id):
    response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=8f6708a938fdc0b2af9c748da8c20887&language=en-US'.format(movie_id))
    data=response.json()
    return "https://image.tmdb.org/t/p/w500/"+data['poster_path']


def recommend(movie):
    movie_index=movies[movies['title']==movie].index[0]
    distances=similarity[movie_index]
    movies_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    recommended_movies=[]
    recommended_movies_posters=[]
    for i in movies_list:
        movies_id=(movies.iloc[i[0]].movie_id)
        # fetch poster or images of that movie through movies_id#

        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movies_id))
    return recommended_movies,recommended_movies_posters



movies_dict=pickle.load(open('movies.pkl','rb'))
movies=pd.DataFrame(movies_dict)

similarity=pickle.load(open('simalarity.pkl','rb'))





st.title('Movie Recommender System')

selected_movie_name=st.selectbox(
'Select the movie name please?',
movies['title'].values,
)
if st.button('Recommend'):
    name,posters= recommend(selected_movie_name)
    col1,col2,col3,col4,col5 = st.columns(5)
    with col1:
        st.text(name[0])
        st.image(posters[0])
    with col2:
         st.text(name[1])
         st.image(posters[1])
    with col3:
        st.text(name[2])
        st.image(posters[2])
    with col4:
        st.text(name[3])
        st.image(posters[3])
    with col5:
       st.text(name[4])
       st.image(posters[4])
