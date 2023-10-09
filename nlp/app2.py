import streamlit as st
import os

import pandas as pd
import numpy as np
import datetime
import webbrowser

st.title('Qua Qua hotel recommendation')

with st.sidebar:
  st.image("qqimg.png", width=200)
  
# option = st.selectbox(
#     'Purpose of the trip?',
#     ('Personal', 'Business', 'Blend'), index=None)

# st.write("Your selected purpose:", option)


genre = st.radio(
    "What's your purpose of trip",
    ["Personal", "Business", "Blend "])

st.write("Your selected purpose:", genre)

# Load the CSV file
##@st.cache  # Caching for improved performance
def load_data():
    data = pd.read_csv('qq_data.csv')  # Replace 'data.csv' with your CSV file's path
    return data

data = load_data()

# Display the unique values from the selected column in a dropdown
dropdown_values = data.Location.unique()
city = st.selectbox('Select city:', dropdown_values)

# Show the selected value
st.write(f"You selected: {city}")


ndays = st.number_input('No. of days', min_value=1, max_value=None, value=1)
st.write('No of days to travel: ', ndays)


npersons = st.number_input('No. of persons', min_value=1, max_value=None, value=1)
st.write('No of persons to travel: ', npersons)

d = st.date_input("Select your start date of travel", value=None)
st.write('Start date:', d)


# Display the unique values from the selected column in a dropdown
dropdown_values = data.Theme.unique()
theme = st.selectbox('Select theme:', dropdown_values)

# Show the selected value
st.write(f"You selected: {theme}")

df = data[(data.Location == city) & (data.Theme == theme)]

nrooms=np.ceil(npersons/df.Max_people)

df['Number_of_rooms'] = nrooms.astype(int)

df1 = df[['Hotel_Name','Number_of_rooms','Rating','Rate_Card','Booking_link' ]].sort_values(by='Rating',ascending=False).reset_index(drop=True)

def make_clickable(link):
    # target _blank to open new window
    # extract clickable text to display for your link
    url = 'https://www.agoda.com/?cid=1844104'
    text = "Book now"
    return f'<a target="_blank" href="{url}">{text}</a>'

df1['Booking_link'] = df1['Booking_link'].apply(make_clickable)
df1 = df1.to_html(escape=False)
st.write(df1, unsafe_allow_html=True)

# url = 'https://www.agoda.com/?cid=1844104'

# if st.button('Book Hotel'):
#     webbrowser.open_new_tab(url)