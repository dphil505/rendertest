import streamlit as st
from time import sleep
from navigation import make_sidebar

import streamlit as st

st.set_page_config(layout='centered')

if "role" not in st.session_state:
    st.session_state.role = None
if st.session_state.role== None:

    hide_decoration_bar_style = '''
        <style>
            header {visibility: hidden;}
        </style>
    '''
    st.markdown(hide_decoration_bar_style, unsafe_allow_html=True)

    video_html = """
                <style>

                #myVideo {
                position: fixed;
                right: 0;
                bottom: 0;
                min-width: 100%;
                min-height: 100%;
                }

                .content {
                position: fixed;
                bottom: 0;
                background: rgba(0, 0, 0);
                color: #f1f1f1;
                width: 100%;
                padding: 0px;
                }

                </style>
                <video autoplay muted loop id="myVideo">
                <source src="https://cdn.pixabay.com/video/2023/01/05/145411-786670497_small.mp4">
                Your browser does not support HTML5 video.
                </video>
                """

    st.markdown(video_html, unsafe_allow_html=True)

st.title("Welcome to Ohmik AI")
st.write("Please log in to continue (username `test`, password `test`).")

username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Log in", type="primary"):
    if username == "test" and password == "test":
        st.session_state.logged_in = True
        st.success("Logged in successfully!")
        sleep(0.5)
        st.switch_page("pages/helloworld.py")
    else:
        st.error("Incorrect username or password")
