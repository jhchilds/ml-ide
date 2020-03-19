# ml-ide
A collaborative IDE enhanced with a machine learning algorithm to automatically recognize languages as a user writes.

## Setup Guide

### Create a file called pw.txt. 

The file should be organized as follows:
```
github_username 
github_password
```
on the first and second lines respectively.

### Install dependencies

Navigate to the project directory and run 'pip3 install -r requirements.txt'

### Run prediction pipeline

1. Gather data via 'python3 data_collection/collect_data.py'
2. Create labeled dataset via 'python3 create_data.py'
3. Create n-gram features from the dataset via 'python3 create_features.py'
4. Create and measure model performance via 'python3 predict.py'

PCA visualizations can also be obtained by running 'python3 pca_reduction.py'
