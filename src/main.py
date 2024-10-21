import streamlit as st
import datetime
import plotly.graph_objects as go
import sys 
from os import environ
from postgresql import POSTGRESQL
import pandas as pd
import psycopg2
import plotly.express as px
import matplotlib.pyplot as plt

st.set_page_config(layout='wide')
# DBに接続
connection_conf ={
    'user':'postgres',
    'password':environ.get('MYPASSWORD'),
    'host':'192.168.2.161',
    'database':'sensor_db'
}
DB = psycopg2.connect(**connection_conf)
print('connect DB')
df = pd.read_sql("select * from sensor_tb",DB)
columns = pd.read_sql("select column_name from information_schema.columns where table_name = 'sensor_tb' and column_name!='created_at'",DB)
st.write(columns["column_name"])
# レイアウト
col = st.columns(3)
df_list = ['temperature','humidity']
    

# plt.figure(figsize=[5,5])
# plt.plot(df['created_at'],df['temperature'])
# plt.plot(df['created_at'],df['humidity'])
# st.pyplot(plt)


# 時間を範囲指定するため
datetime_list = []
datetime_list.append(datetime.date(2024,1,1))
datetime_list.append(datetime.date(2024,8,31))

with col[0]:
    select_val0 = st.selectbox(label="column0 selectbox",options=["a","b","c"])

with col[1]:
    # select_val1 = st.selectbox(label="column1 selectbox",options=columns)
    select_val1 = st.multiselect(label="column1 multi selectbox",options=columns)

with col[2]:
    st.date_input(label="time",value=datetime_list)

plot_data_list=[]

for x in range(0,len(select_val1)):
    plot_data_list.append(go.Scatter(x=df['created_at'],y=df[select_val1[x]]))
# st.write(plot_data_list)
# グラフのオブジェクト
fig = go.Figure(data=plot_data_list)
# fig = go.Figure(data=[
#     go.Scatter(x=df['created_at'], y=df['temperature']),
#     go.Scatter(x=df['created_at'], y=df['humidity'])
# ])
st.plotly_chart(fig)