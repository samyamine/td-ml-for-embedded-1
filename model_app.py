import streamlit as st
import joblib


# 4. In model_app.py, using the joblib library, load the model from the "regression.joblib "file
model = joblib.load("regression.joblib")

# 5. Using the st.number_input function, create three form fields for size, number of bedrooms and whether a house has a garden
size = st.number_input("Size", min_value=0)
nb_bedroom = st.number_input("Nb bedrooms", min_value=0)
has_garden = st.number_input("Garden", min_value=0, max_value=1)


# 6. Retrieve the information and pass it to the model via the predict function. Display the result in the streamlit
input_data = [[size, nb_bedroom, has_garden]]
prediction = model.predict(input_data)

# Use st.write to display the prediction result
st.write("Result:", prediction)
