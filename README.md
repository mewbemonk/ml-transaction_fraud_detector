💳 Transaction Fraud Detection using Machine Learning
📌 Overview

This project builds a Machine Learning–based Fraud Detection System to identify fraudulent financial transactions.
The system analyzes transaction patterns such as transaction type, amount, and balance changes to determine whether a transaction is legitimate or fraudulent.

The model was trained using supervised machine learning algorithms and deployed with a Streamlit web interface for real-time predictions.

🚀 Features

Detects fraudulent vs legitimate transactions

Uses feature engineering to extract meaningful patterns

Compares multiple ML models

Performs hyperparameter tuning

Uses cross-validation to prevent overfitting

Deployable interactive Streamlit application

Saves trained model using Joblib

📊 Dataset

The dataset contains financial transaction records with the following information:

Feature	Description
amount	Transaction amount
oldbalanceOrg	Sender's balance before transaction
newbalanceOrig	Sender's balance after transaction
oldbalanceDest	Receiver's balance before transaction
newbalanceDest	Receiver's balance after transaction
type	Type of transaction
isFraud	Target variable (1 = Fraud, 0 = Legitimate)
Target Variable
isFraud
0 → Legitimate transaction
1 → Fraudulent transaction
🧠 Feature Engineering

Additional features were created to improve model performance.

Balance difference features
balance_diff_orig = oldbalanceOrg - newbalanceOrig
balance_diff_dest = oldbalanceDest - newbalanceDest

These features help detect abnormal balance changes, which are common indicators of fraud.

⚙️ Data Preprocessing

Steps performed during preprocessing:

Removed unnecessary columns

nameOrig
nameDest

One-Hot Encoding of transaction type

type_CASH_IN
type_CASH_OUT
type_DEBIT
type_PAYMENT
type_TRANSFER

Feature Scaling using StandardScaler

Converted dataset to float32 to reduce memory usage.

🤖 Machine Learning Models Used

The following models were trained and evaluated:

Model	Description
Logistic Regression	Baseline linear model
Decision Tree	Rule-based classifier
Random Forest	Ensemble tree model
XGBoost	Gradient boosting algorithm
🔎 Hyperparameter Tuning

Hyperparameter tuning was performed using RandomizedSearchCV.

Example:

RandomizedSearchCV(
    model,
    param_distributions=params,
    cv=5,
    n_iter=10
)

This helps find the best model configuration efficiently.

📈 Model Performance
Cross Validation Scores
Model	CV Score
Logistic Regression	0.951
Decision Tree	0.982
Random Forest	0.986
XGBoost	0.985
Best Model
RandomForestClassifier
📉 Classification Report
precision    recall  f1-score

Fraud Detection Performance
Accuracy: ~99%
Fraud Recall: ~99%

This indicates strong model performance with minimal overfitting.

🔁 Cross Validation

5-Fold Cross Validation was used to ensure the model generalizes well.

Example scores:

[0.954, 0.991, 0.993, 0.992, 0.994]
Mean CV Score: 0.985
💾 Model Saving

The trained model and preprocessing components were saved using Joblib.

fraud_model.pkl
scaler.pkl
features.pkl

This allows the model to be loaded directly for predictions.

🖥 Streamlit Web App

A simple Streamlit application was built for real-time predictions.

Users can input:

Transaction Type

Amount

Sender Balance

Receiver Balance

The model then predicts:

⚠️ Fraudulent Transaction
or
✅ Legitimate Transaction
📂 Project Structure
fraud-detection-project
│
├── dataset
│   └── transaction_dataset.csv
│
├── notebook
│   └── model_training.ipynb
│
├── pickle-files
│   ├── fraud_model.pkl
│   ├── scaler.pkl
│   └── features.pkl
│
├── app.py
├── requirements.txt
└── README.md
📦 Installation

Clone the repository

git clone https://github.com/mewbemonk/ml-transaction_fraud_detector.git

Move into the directory

cd fraud-detection-project

Install dependencies

pip install -r requirements.txt
▶️ Run the Application
streamlit run app.py
🧪 Example Prediction Flow
User Input
↓
Feature Engineering
↓
Scaling
↓
ML Model Prediction
↓
Fraud / Legitimate Output
📚 Technologies Used

Python

Pandas

NumPy

Scikit-Learn

XGBoost

Streamlit

Matplotlib

Joblib

🎯 Future Improvements

Add SHAP explainability

Deploy using Docker

Create REST API using FastAPI

Add real-time transaction monitoring

👨‍💻 Author

Rishabh

Machine Learning Enthusiast focused on building practical AI systems for real-world problems.