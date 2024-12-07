import pandas as pd
import numpy as np
import math
import sys

import describe_df

def main() -> None:
    df = pd.read_csv("dataset_test.csv")
    # print(df.describe()['mean'])
    # print(df.dtypes)
    ds = describe_df.describ(df)

main()