import streamlit as st 
import pandas as pd
import pickle

movie_dict = pickle.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movie_dict)
similarity = pickle.load(open('similarity.pkl','rb'))

def recommend(movie):
    movie_index = movies[movies['title']== movie].index[0]
    distance = similarity[movie_index]
    movie_list= sorted(enumerate(distance),reverse=True,key=lambda x: x[1])[1:6]
    recommended_movies =[]
    
    for i in movie_list:
        recommended_movies.append ((movies.iloc[i[0]].title))
    return recommended_movies

st.title('MOVIE RECOMMENDER SYSTEM')

option = st.selectbox(
    'What is in your mind?',
    (movies['title'].values)
)
if st.button('Recommend'):
    recommendation = recommend(option)
    for i in recommendation:
        st.write(i)

    