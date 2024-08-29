import streamlit as st
import datetime

# レイアウト
col = st.columns(3)

# 時間を範囲指定するため
datetime_list = []
datetime_list.append(datetime.date(2024,1,1))
datetime_list.append(datetime.date(2024,8,31))

with col[0]:
    select_val0 = st.selectbox(label="column0 selectbox",options=["a","b","c"])

with col[1]:
    select_val1 = st.selectbox(label="column1 selectbox",options=["d","e","f"])

with col[2]:
    st.date_input(label="time",value=datetime_list)

st.write(select_val0)
st.write(select_val1)