import streamlit as st
import plotly.express as px
from backend import get_data

st.title("Weather Forecast for the Next Days")
place = st.text_input("PLace: ")
days = st.slider("Forecast Days", min_value=1, max_value=5, help="Select the number of forecasted days")
option = st.selectbox("Select data to view", ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")

if place:
    try:
        data = get_data(place if place != "" else "Vancouver", days)
        match option:
            case "Temperature":
                temperatures = [i['main']['temp'] / 10 for i in data]
                dates = [i['dt_txt'] for i in data]
                figure = px.line(x=dates, y=temperatures, labels={"x": "Date", "y": "Temperature (C)"})
                st.plotly_chart(figure)
            case "Sky":
                sky_conditions = [i['weather'][0]['main'] for i in data]
                print(sky_conditions)
                images = {"Clouds": "images/cloud.png", "Clear": "images/clear.png", "Rain": "images/rain.png",
                          "Snow": "images/snow.png"}
                image_paths = [images[i] for i in sky_conditions]
                print(image_paths)
                st.image(image_paths, width=115)
    except KeyError:
        st.error("You need to enter a valid place")