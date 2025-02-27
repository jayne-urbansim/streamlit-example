from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
from PIL import Image
from st_aggrid import AgGrid

import time
import requests
from streamlit_lottie import st_lottie
from streamlit_lottie import st_lottie_spinner

from streamlit_option_menu import option_menu
import streamlit.components.v1 as components



# ---- Page Configuration -----

st.set_page_config(
     page_title="Ex-stream-ly Cool App",
     page_icon="🧊",
     layout="wide",
     initial_sidebar_state="expanded",

 )
# ----- Maps -----

st.header('ArcMap Experiments')

st.subheader('Map created in Experience Builder')
components.html(
     """
     <iframe width='100%' height='900px' src="https://experience.arcgis.com/experience/4838f87e2d704891af2d343a38b92f45/"></iframe>
     """,
     height=900,
)


st.header('Mapbox Experiments')

st.subheader('Map from Mapbox API')
components.html(
     """
     <iframe width='100%' height='900px' src="https://api.mapbox.com/styles/v1/jayne-urbansim/cl2v5x0hi002415ld4uhltc6z.html?title=false&access_token=pk.eyJ1IjoiamF5bmUtdXJiYW5zaW0iLCJhIjoiY2wydGV5aTRiMDF2ODNjcXZ6dHJ1cWRyYiJ9.RLM3qCHCGm7qJ00RxBLRCQ&zoomwheel=false#12.88/33.97365/-118.39509" title="Monochrome-copy" style="border:none;"></iframe>
     """,
     height=900,
)

st.subheader('Draw on the custom map')
components.iframe("https://satin-odd-shield.glitch.me/drawmap.html", 
	height=900,
)

st.subheader('Change Color')
components.iframe("https://satin-odd-shield.glitch.me/changecolor.html", 
	height=900,
)

st.subheader('Show or Hide Layers')
components.iframe("https://satin-odd-shield.glitch.me/layerstest.html", 
	height=900,
)

st.subheader('Show Custom Image')
components.iframe("https://satin-odd-shield.glitch.me/imagetest.html", 
	height=900,
)
# ----- Image -----

#image = Image.open('img/noun-city-141548-00BBC3.png')
#st.image(image, caption='This is a cute kitten')

# ----- Buttons -----

if st.button('👀 Say hello', help='This is a tootip test', disabled=True):
     st.write('Why hello there')
else:
     st.write('Goodbye')

# ----- Sidebar Stuff -----
          
with st.sidebar:
     image = Image.open('img/noun-city-141548-00BBC3.png')
     st.title('Scenario Modeler')   
     
# Using object notation
add_selectbox = st.sidebar.selectbox(
    "Region",
    ("Vancouver", "Toronto", "Calgary")
)

# Using "with" notation
#with st.sidebar:
#    add_radio = st.radio(
#        "Choose a shipping method",
#        ("Standard (5-15 days)", "Express (2-5 days)")
#   )

# ---- Tab test ---

tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])

with tab1:
    st.header("A cat")
    st.image("https://static.streamlit.io/examples/cat.jpg", width=200)

with tab2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg", width=200)

with tab3:
    st.header("An owl")
    st.image("https://static.streamlit.io/examples/owl.jpg", width=200)

# ----- Container Stuff -----

with st.container():
    st.header("This is a grid of images")
    st.write("This is inside the container")

    col1, col2, col3 = st.columns(3)

    with col1:
		
          st.subheader("A cat")
          st.image("https://static.streamlit.io/examples/cat.jpg")

    with col2:
          st.subheader("A dog")
          st.image("https://static.streamlit.io/examples/dog.jpg")

    with col3:
          st.subheader("An owl")
          st.image("https://static.streamlit.io/examples/owl.jpg")




with st.container():
    st.write("This is inside the container")

    col1, col2, col3 = st.columns(3)

    with col1:
          st.subheader("A cat")
          st.image("https://static.streamlit.io/examples/cat.jpg")

    with col2:
          st.subheader("A dog")
          st.image("https://static.streamlit.io/examples/dog.jpg")

    with col3:
          st.subheader("An owl")
          st.image("https://static.streamlit.io/examples/owl.jpg")

          
          
st.write("This is outside the container")

# ----- Expander Stuff -----

with st.expander("See explanation"):

	
# Sample code from the demo
    with st.echo(code_location='below'):
         total_points = st.slider("Number of points in spiral", 1, 5000, 2000)
         num_turns = st.slider("Number of turns in spiral", 1, 100, 9)

         Point = namedtuple('Point', 'x y')
         data = []

         points_per_turn = total_points / num_turns

         for curr_point_num in range(total_points):
             curr_turn, i = divmod(curr_point_num, points_per_turn)
             angle = (curr_turn + 1) * 2 * math.pi * i / points_per_turn
             radius = curr_point_num / total_points
             x = radius * math.cos(angle)
             y = radius * math.sin(angle)
             data.append(Point(x, y))

         st.altair_chart(alt.Chart(pd.DataFrame(data), height=500, width=500)
             .mark_circle(color='#0068c9', opacity=0.5)
             .encode(x='x:Q', y='y:Q'))
	
     
# ---- Components Test -----

st.header('Playing around with the community components')


df = pd.read_csv('https://raw.githubusercontent.com/fivethirtyeight/data/master/airline-safety/airline-safety.csv')
AgGrid(df)


# Lottie

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


lottie_url_hello = "https://assets9.lottiefiles.com/packages/lf20_ff1eftyp.json"
lottie_url_download = "https://assets4.lottiefiles.com/private_files/lf30_t26law.json"
lottie_hello = load_lottieurl(lottie_url_hello)
lottie_download = load_lottieurl(lottie_url_download)


st_lottie(lottie_hello, key="hello")

if st.button("Download"):
    with st_lottie_spinner(lottie_download, key="download"):
        time.sleep(5)
    st.balloons()

# Option menu

# 1. as sidebar menu
with st.sidebar:
    selected = option_menu(None, ['Map Atlas','Scenarios','Run Manager','Visualizations','Support','My Account'], 
     icons=['geo-alt', 'pencil-square', 'card-checklist', 'graph-up-arrow','question-circle','person'], menu_icon="building", default_index=1)
    selected

# 2. horizontal menu
selected2 = option_menu(None, ["Home", "Upload", "Tasks", 'Settings'], 
    icons=['house', 'cloud-upload', "list-task", 'gear'], 
    menu_icon="cast", default_index=0, orientation="horizontal")
selected2

# 3. CSS style definitions
selected3 = option_menu(None, ["Home", "Upload",  "Tasks", 'Settings'], 
    icons=['house', 'cloud-upload', "list-task", 'gear'], 
    menu_icon="cast", default_index=0, orientation="horizontal",
    styles={
        "container": {"background-color": "#ffffff"},
        "icon": {"color": "#6941C6", "font-size": "24px"}, 
        "nav-link": {"font-size": "24px", "--hover-color": "#F9F5FF"},
    }
)
# ---- Elements

