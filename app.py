from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

# Load the trained model
model_name = 'Logistic Regression.pkl'
model = joblib.load(f'models/{model_name}')

# Create a FastAPI instance
app = FastAPI()

# Define the input data structure
class InputData(BaseModel):
    Gender: str
    Age: int
    Hypertension: int
    Heart_disease: int
    Ever_married_binary: int
    Work_type: str
    Residence_type_binary: int
    Avg_glucose_level: float
    Filled_bmi: float
    Smoking_status: str

# Define a prediction endpoint
@app.post('/predict')
def predict(input_data: InputData):
    # Convert input data to DataFrame
    input_df = pd.DataFrame([input_data.dict()])

    # Perform the prediction
    prediction = model.predict(input_df)

    # Return the prediction
    return {'prediction': int(prediction[0])}