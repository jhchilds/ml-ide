# ml-ide
This is a prototype IDE that uses a Deep Neural Network in order to classify code as its respective language. In order to recreate the model, (or make a better one) follow the setup guide.


As a user types in the code editor, this is what happens:
1. With each modification to the editor, all of the text is sent to the server via HTTP.  
2. The text is then vectorized into character bi-grams.
3. Features are extracted by considering the highest 2000 string frequencies as individual features.
4. The features are passed into a DNN that classifies each set of features into 1 of 6 output classes (C, Java, Python, JavaScript, Haskell, & Swift)



## Setup Guide

NOTE: This step can be ignored since we have provided the names of repos to clone in the `repos`
### Create a file called pw.txt. 

The file should be organized as follows:
```
github_username 
github_password
```
on the first and second lines respectively.

### Install dependencies

Navigate to the project directory and run `pip3 install -r requirements.txt`

### Run prediction pipeline

1. Gather data via `python3 data_collection/collect_data.py`
2. Create labeled dataset via `python3 create_data.py`
3. Create n-gram features from the dataset via `python3 create_features.py`
4. Create and measure model performance via `python3 predict.py`

PCA visualizations can also be obtained by running `python3 pca_reduction.py`
