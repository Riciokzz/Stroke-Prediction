# Stroke Prediction

## Introduction

According to the World Health Organization (WHO) stroke is the 2nd leading cause of death globally, 
responsible for approximately 11% of total deaths.

The aim of this work is to create a machine learning model, which could predict if the patient is likely to get a 
stroke - being able to determine which patients have high stroke risk will allow your doctors to advise them and 
their families on how to act in case of an emergency. We will pretend to be a data analyst working in 
The Johns Hopkins Hospital.

We will check for data quality, correlations and relation of features. We will perform statistical inference, 
form hypothesis base by what we find in our data and create machine learning models to predict patients 
who have risk of the stroke.

To install all necessary libraries use `pip install -r requirements.txt`

To deploy model follow  the steps:
1. Pick model from models and edit `app.py` model_name. (Default model: Logistic Regression)
2. Run this code `uvicorn app:app --reload` in terminal.
3. Edit `predict_data.py` file to input values.
4. Run this code `python predict_data.py` in terminal.
5. Answer will be printed in console: `{'prediction': 0} or {'prediction': 1}`. 0 for No and 1 for Yes


Dataset can be downloaded from 
[Kaggle](https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset/data).


## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Contact Information
[Email](ricardas.poskrebysev@gmail.com)
[LinkedIn](https://www.linkedin.com/in/ri%C4%8Dardas-poskreby%C5%A1evas-665207206/)
[GitHub](https://github.com/Riciokzz)
