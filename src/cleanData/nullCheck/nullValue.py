
import pandas as pd
from src.dataLoad import LoadCSVToDataFrame


BureauDataFrame1 = LoadCSVToDataFrame("train_credit_bureau_a_1_*")
print(BureauDataFrame1.head())

