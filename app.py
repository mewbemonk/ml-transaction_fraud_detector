import streamlit as st
import joblib as jb
import pandas as pd


model = jb.load("pickle-files/fraud_model.pkl")
scaler = jb.load("pickle-files/scaler.pkl")
features = jb.load("pickle-files/features.pkl")


st.title("Transaction Fraud Detector")


st.markdown("Please enter your transaction details below")

st.divider()


transaction_type = st.selectbox("Transaction-Type",['type_CASH_IN', 'type_CASH_OUT','type_DEBIT', 'type_PAYMENT', 'type_TRANSFER'])


amount = st.number_input("Amount",min_value=0.0,value=1000.0)


old_bal_orig = st.number_input("Old Balance (sender)",min_value=0.0,value=10000.0)
new_bal_orig = st.number_input("New balance (sender)",min_value=0.0,value=9000.0)



old_bal_dest = st.number_input("Old Balance (receiver)",min_value=0.0,value=0.0)
new_bal_dest = st.number_input("New balance (receiver)",min_value=0.0,value=0.0)


type_dict = {
        'type_CASH_IN':0,
        'type_CASH_OUT':0,
        'type_DEBIT':0,
        'type_PAYMENT':0,
        'type_TRANSFER':0
    }


if st.button("Predict"):
    balance_diff_orig = old_bal_orig-new_bal_orig
    balance_diff_dest = old_bal_dest-new_bal_dest

    type_dict[transaction_type] = 1

    data = {
    "amount": amount,
    "oldbalanceOrg": old_bal_orig,
    "newbalanceOrig": new_bal_orig,
    "oldbalanceDest": old_bal_dest,
    "newbalanceDest": new_bal_dest,
    "balance_diff_orig": balance_diff_orig,
    "balance_diff_dest": balance_diff_dest,
    **type_dict
}
    
    numeric_col = [
    'amount',
    'oldbalanceOrg',
    'newbalanceOrig',
    'oldbalanceDest',
    'newbalanceDest'
]

    df = pd.DataFrame([data])

    df = df[features]


    df[numeric_col] = scaler.transform(df[numeric_col])

    pred = model.predict(df)[0]



    if pred==1:

        st.error("⚠️ Fraudulent Transaction Detected")

    else:

        st.success("✅ Transaction is Legitimate")
