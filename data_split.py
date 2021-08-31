import pandas as pd
from sklearn.model_selection import train_test_split

data = pd.read_csv("COA_path_gt_cleaned.txt", sep='\t')
train, test = train_test_split(data, test_size=0.2, random_state=42, shuffle=True)
print("Test", test)
train, valid = train_test_split(train, test_size=0.1, random_state=42, shuffle=False)
train.to_csv("COA_train_cleaned1.csv", sep='\t', index=False)
test.to_csv("COA_test_cleaned1.csv", sep='\t', index=False)
valid.to_csv("COA_valid_cleaned1.csv", sep='\t', index=False)

