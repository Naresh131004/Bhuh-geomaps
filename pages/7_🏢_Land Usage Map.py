import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")

markdown = """
Website
<https://www.bhuhpramaan.com>
"""

st.sidebar.title("About")
st.sidebar.info(markdown)
logo = "https://i.imgur.com/MWpI4OI.jpeg"
st.sidebar.image(logo)

st.title("Land Usage Map")

with st.expander("See source code"):
    with st.echo():
        m = leafmap.Map()
        before = "https://github.com/Naresh131004/Bhuh-geomaps/raw/main/2000.tif"
        after = "https://github.com/Naresh131004/Bhuh-geomaps/raw/main/2023.tif"
        m.split_map(
            left_layer=before, right_layer=after, left_label="2000", right_label="2023"
        )

m.to_streamlit(height=700)

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
