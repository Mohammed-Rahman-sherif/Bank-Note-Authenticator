# Author: Mohammed Rahman Sherif
# Date: 2023-08-25
# Time: 13:07:22

from fastapi import FastAPI, Query
from pydantic import BaseModel
import uvicorn, pickle

with open("RandomForestClassifier.pkl", "rb") as file:
    clf = pickle.load(file)

app = FastAPI()

class PredictionInputs(BaseModel):
    variance: float = Query(..., description="variance")
    skewness: float = Query(..., description="skewness")
    curtosis: float = Query(..., description="curtosis")
    entropy: float = Query(..., description="entropy")

@app.get("/")
def welcome():
    return "Welcome to the page"

@app.post("/predict")
def bank_note_authentication(input_data: PredictionInputs):
    prediction = clf.predict([[input_data.variance, input_data.skewness, input_data.curtosis, input_data.entropy]])
    return f"The predicted note is class: {str(prediction)}"