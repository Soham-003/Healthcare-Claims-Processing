import pandas as pd

from pipeline.healthcare_etl import clean_claims_data


def test_clean_claims_data():
    data = {
        "patient_id": [101, None],
        "claim_amount": [5000, None]
    }

    df = pd.DataFrame(data)

    result = clean_claims_data(df)

    assert len(result) == 1

    assert result.iloc[0]["patient_id"] == 101

    assert result.iloc[0]["claim_amount"] == 5000