import streamlit as st
import pickle
import pandas as pd


def recommend(app_name):
    app_index =app[app["Name"] == app_name].index[0]
    distances = similarity[app_index]
    app_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    recommended_app=[]
    for i in app_list:
        recommended_app.append(app.iloc[i[0]].Name)
    return recommended_app


app_dict = pickle.load(open('app_data_dict.pkl','rb'))
app =pd.DataFrame(app_dict)
similarity = pickle.load(open('similarity.pkl','rb'))
st.title("Application Recommender System")
selected_app_name = st.selectbox(
    'Please provide  your App requirnmnet',
    (app))
if st.button('Recommend'):
    recommendations = recommend(selected_app_name)
    for i in recommendations:
     st.write(i)
