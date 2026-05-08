import pandas as pd


def clean_claims_data(df):
    cleaned_df = df.dropna(subset=["patient_id"])

    cleaned_df["claim_amount"] = cleaned_df[
        "claim_amount"
    ].fillna(0)

    return cleaned_df

if __name__ == "__main__":
    sample_data = {
        "patient_id": [101, None, 103],
        "claim_amount": [5000, None, 3000]
    }

    df = pd.DataFrame(sample_data)

    print("Original Data:\n")
    print(df)

    cleaned_df = clean_claims_data(df)

    print("\nCleaned Data:\n")
    print(cleaned_df)