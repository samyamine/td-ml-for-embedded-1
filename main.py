from typing import Union
import joblib

from fastapi import FastAPI

app = FastAPI()


@app.get("/predict")
async def read_item(size: int = 0, nb_bedroom: int = 0, has_garden: int = 0):
    model = joblib.load("regression.joblib")
    input_data = [[size, nb_bedroom, has_garden]]
    prediction = model.predict(input_data)

    return {"predicted_price": prediction[0]}