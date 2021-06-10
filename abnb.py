import streamlit as st
from PIL import Image
import math

logo = Image.open('Airbnb_Logo.png')
abnblogo= st.image(logo)
st.title('Airbnb Rental Property Price Calculator')
subhead=st.markdown("<h2 style='text-align: center;'><br/>This is a pricing tool to estimate the fair price per night of an Airbnb listing in Malta based on actual data from May 2019.<br/> <br/> Created by Rafael Fearne with data from InsideAirbnb.<br/> </h2>", unsafe_allow_html=True)
link=st.markdown("&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; The model and description of the data is available in the author's **[study](https://doi.org/10.1108/IJHMA-12-2020-0147)**", unsafe_allow_html=True)


superhost = st.selectbox("Is the owner a registered superhost?",options=['Yes' , 'No'])
total_listings = st.number_input("How many listings does the owner have on Airbnb?")
property_type = st.selectbox("Which of the following describes the property",options=['Apartment' , 'Bungalow/Farmhouse', 'House', 'Villa'])
roomtype = st.selectbox("Is the listing for an entire house/apartment or for a room?",options=['Entire house/apartment' , 'Shared/Private room'])
accomodates = st.number_input("How many people does the property sleep?")
bathrooms = st.number_input("How many bathrooms does the property have?")
bedrooms = st.number_input("How many bedrooms does the property have?")
seaview = st.selectbox("Does the property have a seaview?",options=['Yes' , 'No'])
wifi = st.selectbox("Does the property have wifi?",options=['Yes' , 'No'])
breakfast = st.selectbox("Does the property offer breakfast?",options=['Yes' , 'No'])
parking = st.selectbox("Does the property have parking?",options=['Yes' , 'No'])
pool = st.selectbox("Does the property have a pool?",options=['Yes' , 'No'])
instantly_bookable = st.selectbox("Is the property instantly bookable?",options=['Yes' , 'No'])
cancellation = st.selectbox("Is free cancellation available?",options=['Yes' , 'No'])
smoking = st.selectbox("Is smoking allowed?",options=['Yes' , 'No'])
guest_pp = st.selectbox("Does the property require guests to have a profile picture to book?",options=['Yes' , 'No'])
reviews_py = st.number_input("How many reviews does the property get per year? *If none yet, enter 14*")
reviews_score = st.number_input("What is the average review score? *If none yet, enter 95*")
region = st.selectbox("In which region is the property situated?",options=['Western' , 'Southern Harbour', 'Northern', 'Northern Harbour', 'South Eastern','Gozo & Comino'])

superhost = 0 if superhost == 'No' else 1

if property_type== 'Apartment': property_type= 0
elif property_type=='Villa': property_type= 2
elif property_type=='Bungalow/Farmhouse' or 'House': property_type=1 

roomtype = 0 if roomtype == 'Shared/Private room' else 1
seaview = 0 if seaview == 'No' else 1
wifi = 0 if wifi == 'No' else 1
breakfast = 0 if breakfast== 'No' else 1
parking = 0 if parking == 'No' else 1
pool = 0 if pool== 'No' else 1
instantly_bookable = 0 if instantly_bookable== 'No' else 1
cancellation = 0 if cancellation == 'No' else 1
smoking = 0 if smoking == 'No' else 1
guest_pp = 0 if guest_pp == 'No' else 1

western , sharbour, northern, nharbour, southeastern, gozo = 0,0,0,0,0,0
if region == 'Western':
    western = 1
elif region == 'Southern Harbour':
    sharbour= 1
elif region == 'Northern':
    northern= 1
elif region == 'Northern Harbour':
    nharbour= 1
elif region == 'South Eastern':
    southeastern= 1
else:
    gozo= 1

logresult=3.231+(0.0655*superhost)+(0.00237*total_listings)+(0.202*property_type)+(0.72*roomtype)+(0.0479*accomodates)+(-0.0132*bathrooms)+(0.133*bedrooms)+(0.0905*seaview)+(0.141*wifi)+(0.17*breakfast)+(-0.108*parking)+(0.399*pool)+(0.103*instantly_bookable)+(-0.0356*cancellation)+(-0.0708*smoking)+(0.213*guest_pp)+(-0.00753*reviews_py)+(0.00198*reviews_score)+(-0.466*gozo)+(-0.36*northern)+(-0.175*nharbour)+(-0.382*southeastern)+(-0.21*western)
resultraw=math.exp(logresult)
result= f"The price per night is approximately **€{resultraw:.2f}**."

generate = st.button('Generate Result')
if generate:
    st.markdown(result)
