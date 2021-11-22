"""
Make data set
"""
import pandas as pd


def make_data():
    # We'll use this data set for user data
    data = pd.read_csv("ab_test_ads/data/AdSmartABdata - AdSmartABdata 2.csv")

    # Truncate unique ids
    data["auction_id"] = data["auction_id"].apply(lambda x: x.split("-")[0])

    # AB testing columns
    data["conversion"] = data["yes"]
    data.drop(columns=["experiment", "hour", "yes", "no"], inplace=True)
    data.to_csv("data.csv")


if __name__== "__main__":

    make_data()
