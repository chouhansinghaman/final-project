# test_project.py

# Import necessary modules
import pandas as pd
from project import detect_fraud, summarize_data

def test_detect_fraud_empty():
    """
    Test detect_fraud with an empty DataFrame.
    Expect the result to also be an empty DataFrame.
    """
    df = pd.DataFrame(columns=["Time", "Amount", "Class"])
    result = detect_fraud(df)
    assert result.empty

def test_detect_fraud_all_legit():
    """
    Test detect_fraud with only legitimate transactions (Class == 0).
    Expect the result to be empty since there's no fraud.
    """
    df = pd.DataFrame({
        "Time": [0, 1],
        "Amount": [100.0, 200.0],
        "Class": [0, 0]
    })
    result = detect_fraud(df)
    assert result.empty

def test_detect_fraud_all_fraud():
    """
    Test detect_fraud with all fraudulent transactions (Class == 1).
    Expect the result to include all records from the input.
    """
    df = pd.DataFrame({
        "Time": [0, 1],
        "Amount": [500.0, 900.0],
        "Class": [1, 1]
    })
    result = detect_fraud(df)
    assert len(result) == 2
    assert all(result["Class"] == 1)

def test_detect_fraud_mixed():
    """
    Test detect_fraud with a mix of fraud and legitimate transactions.
    Expect only the fraudulent transaction(s) to be returned.
    """
    df = pd.DataFrame({
        "Time": [0, 1, 2],
        "Amount": [100.0, 5000.0, 250.0],
        "Class": [0, 1, 0]
    })
    result = detect_fraud(df)
    assert len(result) == 1
    assert result.iloc[0]["Amount"] == 5000.0

def test_summarize_data():
    """
    Test summarize_data to ensure it returns correct statistics.
    Check totals, fraud count, legit count, and fraud percentage.
    """
    df = pd.DataFrame({
        "Time": [0, 1, 2, 3],
        "Amount": [100.0, 200.0, 300.0, 400.0],
        "Class": [0, 1, 0, 0]
    })
    summary = summarize_data(df)
    assert summary["total_transactions"] == 4
    assert summary["fraud_transactions"] == 1
    assert summary["legit_transactions"] == 3
    assert summary["fraud_percentage"] == 25.0
