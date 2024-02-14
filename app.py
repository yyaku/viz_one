import streamlit as st
import numpy as np
import time
from streamlit_image_coordinates import streamlit_image_coordinates
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import json
import plotly.express as px


dates = ['2019-1-14','2019-2-8','2019-3-25','2019-4-6','2019-5-11','2019-6-28','2019-7-15','2019-8-9','2019-9-3','2019-10-23','2019-11-2','2019-12-22','2020-1-14','2020-2-20','2020-3-26','2020-4-23','2020-5-20','2020-6-29','2020-7-19','2020-8-28','2020-9-7','2020-10-22','2020-11-6','2020-12-24','2021-1-15','2021-2-12','2021-3-14','2021-4-28','2021-5-10','2021-6-29','2021-7-9','2021-8-8','2021-9-27','2021-10-15','2021-11-11','2021-12-4','2022-1-25','2022-2-7','2022-3-4','2022-4-10','2022-5-15','2022-6-12','2022-7-24','2022-8-13','2022-9-15','2022-10-2','2022-11-21','2022-12-21','2023-1-8','2023-2-22','2023-3-24','2023-4-10','2023-5-3','2023-6-27','2023-7-29','2023-8-8','2023-9-25','2023-10-27','2023-11-14','2023-12-24']

#vals = [2.8552397596104067,2.7250713187456537,1.8793288064417895,3.0514593692360545,1.2604629458009877,1.556492722511974,1.1767847255928954,1.0256337608707466,1.9106815573516367,1.8241534942945674,4.184153991655403,2.7243296285843797,3.4524773400230933,2.28948841890497,2.050569019184846,2.7935009030045994,1.619975729253054,1.3267731567601024,1.8055624192585085,2.0857499420699646,2.7067445196367865,1.9978632149622584,3.143514120083887,1.7193061264060499,3.3183979519193207,1.860202189651334,1.6409283935283598,1.580360892057658,0.9513942353754549,0.9538689172307534,0.9542932677222635,0.9297083654564752,1.0073123382761286,1.5752842772894942,1.5989433653043705,1.9323812873078117,1.6983788011729255,1.3333233868523933,1.5739805417254422,1.5879276642120876,1.0951955712271546,1.2481097824986156,1.0420240862677006,1.11137380001431,1.1705052160554938,1.035436088404264,1.3914647289843107,1.5005031380980722,1.280617118395571,1.1594445197946763,1.2262470300288852,1.1340685773545773,1.0734395089584756,1.3064652358021274,0.822170095473048,1.0293799569356268,1.5176994487075162,1.9933987599976069,1.4453651764133684,1.7705465932286086]


with open('datier_detection_list_and_indices_v2.json', 'r') as js:
  obj = json.load(js)



st.sidebar.image("circles.jpg", caption='Map', )

user_input = st.sidebar.text_input('Palm number')

#user_input = st.text_input('Enter something:')

if st.sidebar.button('Submit'):
    st.title(f"Palm {user_input}")
    
    ndvi_vals = obj[int(user_input)-1]["ndvi_vals"]
    ndre_vals = obj[int(user_input)-1]["ndre_vals"]
    ndwi_vals = obj[int(user_input)-1]["ndwi_vals"]
    gci_vals = obj[int(user_input)-1]["gci_vals"]
    
    
    #fig, ax = plt.subplots()
    
    fig = px.line(x=dates, y=ndvi_vals, title='NDVI')
    # fig.update_xaxes(tickmode='array', tickvals=list(range(len(dates))), ticktext=dates)

    st.plotly_chart(fig)
    
    fig = px.line(x=dates, y=ndwi_vals, title='GNDVI')
    st.plotly_chart(fig)
    
    fig = px.line(x=dates, y=ndre_vals, title='NDRE')
    st.plotly_chart(fig)
  
    
    fig = px.line(x=dates, y=gci_vals, title='GCI')
    st.plotly_chart(fig)
    
    
    # fig, ax = plt.subplots(figsize=(15, 7))
    # sns.lineplot(x=dates, y=ndvi_vals,marker='.', ax=ax)
    # ax.set_title('NDVI')

    # plt.xticks(rotation=45, ha='right')
    # st.pyplot(fig)
    
    
    # fig, ax = plt.subplots(figsize=(15, 7))
    # sns.lineplot(x=dates, y=ndre_vals,marker='.', ax=ax)
    # ax.set_title('NDRE')

    # plt.xticks(rotation=45, ha='right')
    # st.pyplot(fig)
    
    # fig, ax = plt.subplots(figsize=(15, 7))
    # sns.lineplot(x=dates, y=ndwi_vals,marker='.', ax=ax)
    # ax.set_title('NDWI')

    # plt.xticks(rotation=45, ha='right')
    # st.pyplot(fig)
    
    # fig, ax = plt.subplots(figsize=(15, 6))
    # sns.lineplot(x=dates, y=gci_vals,marker='.', ax=ax)
    # ax.set_title('GCI')

    # plt.xticks(rotation=45, ha='right')
    # st.pyplot(fig)




