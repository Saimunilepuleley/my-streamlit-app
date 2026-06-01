import streamlit as st
st.title("welcome to my first unity app")
st.write("you are welcomed kijanaa")
st.write("hello! my name is saimuni na ukipenda zaidi ni simon liam from kenya")
st.header("tell me about yourself")
name=st.text_input("what is your name bro and dont put jokes?")
age=st.number_input("how old are you?",min_value=12,max_value=75)
country=st.text_input("whre are you from?")
if st.button("submit"):
    st.success(f"hello {name} you are {age} years from {country}")
    if age>=18:
        st.write("i hope uko kadi")
    else:
        st.write("sorry but tulia tukutolee ruto kwa kiti")
                             
