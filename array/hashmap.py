import os
import pandas as pd

# Read the Excel file into a DataFrame
file_path = 'C:/Users/Agemark/Desktop/data_structure_and_algorithm/array/a.csv'  # Ensure the correct path
# df = pd.read_excel(file_path)

# # Convert the data into a list
# stock_price = df.values.tolist()

# print(stock_price)
print(os.path.exists(file_path))


stock_price=[]
with open(file_path,'r',encoding='ISO-8859-1') as f:
    for line in f:
        tokens = line.strip().split(',')
        print(f"Tokens: {tokens}")
        day = tokens[0]
        price= float(tokens[1])
        stock_price.append([day,price])
print(stock_price)        