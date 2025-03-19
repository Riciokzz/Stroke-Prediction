import requests

# Example input data (modify this according to your actual features)
input_data = {
    'Gender': 'Male',               # Male, Female, Other
    'Age': 58,                      # integer > 0
    'Hypertension': 0,              # 1 or 0
    'Heart_disease': 0,             # 1 or 0
    'Ever_married_binary': 0,       # Yes - 1, No - 0
    'Work_type': 'Private',         # 'children', 'Govt_jov', 'Never_worked', 'Private' or 'Self-employed'
    'Residence_type_binary': 1,     # Urban - 1, Rural - 0
    'Avg_glucose_level': 82.15,     # float > 0
    'Filled_bmi': 23.5,             # float > 0
    'Smoking_status': 'smokes',     # 'formerly smoked', 'never smoked', 'smokes' or 'Unknown'
}

# Make a POST request to the FastAPI app
response = requests.post('http://127.0.0.1:8000/predict', json=input_data)

# Print the prediction
response = requests.post('http://127.0.0.1:8000/predict', json=input_data)
if response.status_code == 200:
    print(response.json())
else:
    print(f"Request failed with status code: {response.status_code}")
    print(response.json())