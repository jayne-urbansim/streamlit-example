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

#from streamlit_elements import elements, mui, html


#import pandas as pd

# ---- Page Configuration -----

st.set_page_config(
     page_title="Ex-stream-ly Cool App",
     page_icon="🧊",
     layout="wide",
     initial_sidebar_state="expanded",

 )
# ----- Text -----

st.header('Map Atlas')


components.html(
     """
     <iframe width='100%' height='900px' src="https://api.mapbox.com/styles/v1/jayne-urbansim/cl2v5x0hi002415ld4uhltc6z.html?title=false&access_token=pk.eyJ1IjoiamF5bmUtdXJiYW5zaW0iLCJhIjoiY2wydGV5aTRiMDF2ODNjcXZ6dHJ1cWRyYiJ9.RLM3qCHCGm7qJ00RxBLRCQ&zoomwheel=false#12.88/33.97365/-118.39509" title="Monochrome-copy" style="border:none;"></iframe>
     """,
     height=900,
)


components.html(
     """
     <!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Draw a polygon and calculate its area</title>
<meta name="viewport" content="initial-scale=1,maximum-scale=1,user-scalable=no">
<link href="https://api.mapbox.com/mapbox-gl-js/v2.8.2/mapbox-gl.css" rel="stylesheet">
<script src="https://api.mapbox.com/mapbox-gl-js/v2.8.2/mapbox-gl.js"></script>
<style>
body { margin: 0; padding: 0; }
#map { position: absolute; top: 0; bottom: 0; width: 100%; }
</style>
</head>
<body>
<style>
.calculation-box {
height: 75px;
width: 150px;
position: absolute;
bottom: 40px;
left: 10px;
background-color: rgba(255, 255, 255, 0.9);
padding: 15px;
text-align: center;
}
 
p {
font-family: 'Open Sans';
margin: 0;
font-size: 13px;
}
</style>
 
<script src="https://unpkg.com/@turf/turf@6/turf.min.js"></script>
<script src="https://api.mapbox.com/mapbox-gl-js/plugins/mapbox-gl-draw/v1.2.2/mapbox-gl-draw.js"></script>
<link rel="stylesheet" href="https://api.mapbox.com/mapbox-gl-js/plugins/mapbox-gl-draw/v1.2.2/mapbox-gl-draw.css" type="text/css">
<div id="map"></div>
<div class="calculation-box">
<p>Click the map to draw a polygon.</p>
<div id="calculated-area"></div>
</div>
 
<script>
	mapboxgl.accessToken = 'pk.eyJ1IjoiamF5bmUtdXJiYW5zaW0iLCJhIjoiY2wydGV5aTRiMDF2ODNjcXZ6dHJ1cWRyYiJ9.RLM3qCHCGm7qJ00RxBLRCQ';
const map = new mapboxgl.Map({
container: 'map', // container ID
style: 'mapbox://styles/mapbox/satellite-v9', // style URL
center: [-91.874, 42.76], // starting position [lng, lat]
zoom: 12 // starting zoom
});
 
const draw = new MapboxDraw({
displayControlsDefault: false,
// Select which mapbox-gl-draw control buttons to add to the map.
controls: {
polygon: true,
trash: true
},
// Set mapbox-gl-draw to draw by default.
// The user does not have to click the polygon control button first.
defaultMode: 'draw_polygon'
});
map.addControl(draw);
 
map.on('draw.create', updateArea);
map.on('draw.delete', updateArea);
map.on('draw.update', updateArea);
 
function updateArea(e) {
const data = draw.getAll();
const answer = document.getElementById('calculated-area');
if (data.features.length > 0) {
const area = turf.area(data);
// Restrict the area to 2 decimal points.
const rounded_area = Math.round(area * 100) / 100;
answer.innerHTML = `<p><strong>${rounded_area}</strong></p><p>square meters</p>`;
} else {
answer.innerHTML = '';
if (e.type !== 'draw.delete')
alert('Click the map to draw a polygon.');
}
}
</script>
 
</body>
</html>
     """,
     height=900,
)









st.header('Scenarios')
st.header('Run Manager')
st.header('Visualizations')
st.header('Support')
st.header('My Account')



# ----- Image -----

#image = Image.open('img/noun-city-141548-00BBC3.png')
#st.image(image, caption='This is a cute kitten')

# ----- Buttons -----

if st.button('👀 Say hello', help='This is a tootip test'):
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

# with elements("new_element"):
#     mui.Typography("Hello world")

# with elements("multiple_children"):
#     mui.Button(
#             mui.icon.EmojiPeople,
#             mui.icon.DoubleArrow,
#             "Button with multiple children"
#     )

#     with mui.Button:
#        mui.icon.EmojiPeople()
#        mui.icon.DoubleArrow()
#        mui.Typography("Button with multiple children")
     
#with elements("nested_children"):
#     with mui.Paper:
#             with mui.Typography:
#                 html.p("Hello world")
#                 html.p("Goodbye world")     

