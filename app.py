

import streamlit as st
import pickle
import pandas as pd
import requests


def fetch_poster(movie_id):

         response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=3228f4d00af03bcbd793b88ed4878fdb&language=en-US'.format(movie_id),timeout=10)
         print(movie_id)
         movie_data = response.json()

         # extract poster_path value
         poster_path = movie_data.get('poster_path', None)

         print("data",poster_path)
         print("responses", response)
         return f"https://image.tmdb.org/t/p/w500/{poster_path}"


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distance = similarity[movie_index]
    movie_list = sorted(list(enumerate(distance)), reverse = True, key = lambda x:x[1])[1:6]


    recommended_movies = []
    recommended_movies_posters = []
    for i in movie_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movies_posters



movie_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movie_dict)

similarity = pickle.load(open('similarity.pkl','rb'))

st.title("Movie Recommendation System")


selected_movie_name = st.selectbox("Enter the name of movie", movies['title'].values)

if st.button("Recommend"):
    names,posters = recommend(selected_movie_name)

    col1,col2,col3,col4,col5 = st.columns(5)

    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])

