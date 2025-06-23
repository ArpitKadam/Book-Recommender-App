import pandas as pd
pd.set_option('display.max_columns', None)

df = pd.read_pickle("artifacts\\data_transformation\\transformed_data\\book_names.pkl")
print(df)

print("="*100)

df1 = pd.read_pickle("artifacts\\data_transformation\\transformed_data\\book_pivot.pkl")
print(df1.columns)
print(df1.index)

print("="*100)

df2 = pd.read_pickle("artifacts\\data_transformation\\transformed_data\\transformed_data.pkl")
print(df2.columns)
print(df2.index)

df3 = pd.read_pickle("artifacts\\data_transformation\\transformed_data\\final_ratings.pkl")
print(df3.columns)
print(df3.index)

print("="*100)