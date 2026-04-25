# Import extract, transform, and load functions

# Import the os library
import pandas as pd
import sqlalchemy
import logging


def extract():
    return pd.read_csv("datasets/bmw.csv")


data_frame =  extract()

def transform(car_data):
	# Find the items prices less than 100000 euros
	return car_data.loc[car_data["Avg_Price_EUR"] < 100000, ["Revenue_EUR", "Premium_Share","Fuel_Price_Index"]]

def load(clean_data):
	# Write the data to a CSV file without the index column
	clean_data.to_csv("datasets/transformed_cars_data.csv", index=False)


clean_cars_data = transform(data_frame)

# Call the load function on the cleaned DataFrame
load(clean_cars_data)