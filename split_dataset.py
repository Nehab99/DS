# split_dataset.py

import pandas as pd
from sklearn.model_selection import train_test_split

def split_dataset(input_path, train_output_path, test_output_path, test_size=0.2):
    # Load the dataset
    data = pd.read_csv(input_path, header=None, names=["label", "text"])
    
    # Split the data into training and test sets
    train_data, test_data = train_test_split(data, test_size=test_size, random_state=42)
    
    # Save the training data
    train_data.to_csv(train_output_path, index=False, header=False)
    
    # Save the test data
    test_data.to_csv(test_output_path, index=False, header=False)
    print(f"Test data saved at {test_output_path}")

# Define dataset paths
input_data = "/Users/drish/Documents/GitHub/project/data/cleaned_reviews.csv"
train_output = "/Users/drish/Documents/GitHub/project/data/train_cleaned_reviews.txt"
test_output = "/Users/drish/Documents/GitHub/project/data/test_cleaned_reviews.txt"

# Split the dataset
split_dataset(input_data, train_output, test_output, test_size=0.2)