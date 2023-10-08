import streamlit as st
import requests
from bs4 import BeautifulSoup as bs

st.title(':red[Geologist Earth View]')
# https://worldview.earthdata.nasa.gov/
urls = st.sidebar.text_input('Enter Location')
st.map()
tab1, tab2, tab3 = st.tabs(["Events", "Categories", "Layout"])
if urls:
    with st.spinner('Getting Data'):
        with tab2:
            page2 = requests.get("https://eonet.gsfc.nasa.gov/api/v3/categories/" + urls)
            pt2 = page2.json()
            st.write(pt2)
        with tab3:
            st.markdown("### Layout")
            page3 = requests.get('https://eonet.gsfc.nasa.gov/api/v3/layers/' + urls)
            pt3 = page3.json()
            st.write(pt3)
        with tab1:
            page1 = requests.get('https://eonet.gsfc.nasa.gov/api/v3/events' + urls)
            st.write(page1.json())

