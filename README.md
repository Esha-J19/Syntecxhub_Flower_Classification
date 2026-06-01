# Iris Flower Classification using Machine Learning

## Overview

This project classifies Iris flower species using Machine Learning algorithms. The Iris dataset was analyzed, visualized, and used to train classification models. A Command Line Interface (CLI) was also developed to predict flower species based on user input.

## Dataset

The project uses the Iris dataset provided by Scikit-learn.

### Features

* Sepal Length (cm)
* Sepal Width (cm)
* Petal Length (cm)
* Petal Width (cm)

### Target Classes

* Setosa
* Versicolor
* Virginica

## Exploratory Data Analysis (EDA)

The dataset was explored using:

* Data inspection (`head()`, `info()`, `describe()`)
* Pairplot visualization
* Correlation heatmap

## Machine Learning Models

The following classification models were implemented:

1. Logistic Regression
2. Decision Tree Classifier

## Evaluation Metrics

The models were evaluated using:

* Accuracy Score
* Confusion Matrix
* Precision
* Recall
* F1-Score

## Results

| Model               | Accuracy |
| ------------------- | -------- |
| Logistic Regression | 91.1%    |
| Decision Tree       | 88.9%    |

Logistic Regression achieved the highest accuracy and was selected as the final model.

## CLI Prediction System

A command-line interface was developed to allow users to enter flower measurements and predict the flower species.

Example inputs:

* Sepal Length
* Sepal Width
* Petal Length
* Petal Width

Output:

* Predicted Iris Species

## Project Structure

iris-flower-classification/

├── iris_classification.ipynb

├── predict.py

├── flower_model.pkl

├── README.md

└── requirements.txt

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* Joblib

## Future Improvements

* Hyperparameter tuning
* Random Forest Classifier
* Streamlit web application
* Model deployment

