import pandas as pd
from pandas import DataFrame, concat
from datetime import datetime
import os
from fastapi.responses import JSONResponse
from tabulate import tabulate


def outputFun():
    data = {
        "Name": ["Alice", "Bob", "Charlie", "David"],
        "Age": [25, 30, 22, 35],
        "City": ["New York", "San Francisco", "Los Angeles", "Chicago"],
    }

    df = pd.DataFrame(data)
    print(df)
    return {df.to_json(orient="table")}
