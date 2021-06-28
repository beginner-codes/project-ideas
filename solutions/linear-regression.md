# 📏 Basic Linear Regression Model with Scikit Learn - Solution Walkthrough using Python and Jupyter
[Instructions](https://github.com/beginnerpy-com/project-ideas/blob/main/projects/linear-regression.md) | Solution Code [(Github)](https://github.com/beginnerpy-com/project-ideas/blob/main/solutions/linear-regression.ipynb) or [(NBViewer)](https://nbviewer.jupyter.org/github/beginnerpy-com/project-ideas/blob/main/solutions/linear-regression.ipynb) | [All Ideas](https://github.com/beginnerpy-com/project-ideas/blob/main/README.md)

There are many ways to do this project, depending on how analytical you want to be or how accurate you want your machine learning model. However, this is how we completed it using simple to understand techniques.

## Getting Started - Linear Regression Model
### Installing Libraries Used
For this project, I used VSCode as my code editor, but you could also use Google Colab or Jupyter Notebook/Lab. Before starting the project, we need to install libraries for data manipulation and machine learning that do not come preinstalled with Python (unless you use Google Colab, which has these installed already). It is recommended that you create a new Python virtual environment before installing any libraries using anaconda, venv, virtualenv, or another alternative. The libraries we need to install are:
```
- jupyter-lab
- pandas
- numpy
- scikit-learn
- matplotlib
- seaborn
```

To install these using conda for an Anaconda environment, the commands are: 
```
conda install -c conda-forge jupyterlab
conda install pandas
conda install numpy
conda install -c conda-forge scikit-learn
conda install matplotlib
conda install seaborn
```
The installation of these packages using Pip can be found easily by searching `[library name] install pip` on Google.
### Dataset
We also need data to train and test our model on. For the project, we used a simple linear dataset designed to teach people linear regression from Kaggle, which you can download [here](https://www.kaggle.com/andonians/random-linear-regression).

Once downloaded and extracted, it comes with two files: `train.csv` and `test.csv`. As their names imply, we will be training our linear regression model on `train.csv` and testing our model on `test.csv`.

## Getting Started with Code
The first thing we need to do is import the required libraries we will be using. To do this we run a code cell containing these lines of code:
```py
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
```
`pandas` is used for data manipulation and cleaning, `numpy` is used for arrays, matrices, and numerical calculations, and `seaborn` and `matplotlib` is for plotting.

Next we need to read the csv files into our notebook so that we can use the data we have downloaded. To do this, we read the `train.csv` and `test.csv` files into a dataframe using the `pandas` library.

#### Training data
To import the training data we use `pd.read_csv(file_path)` for example:
```py
train_df = pd.read_csv("datasets/train.csv")
```
Then we can use
```py
train_df.head()
```
to preview to first 5 rows to make sure that the data is loaded in properly.

![train_df](https://user-images.githubusercontent.com/41812358/123644140-35315500-d879-11eb-83be-5a9df3c319a5.png)


#### Testing data
For the testing data, we do the same thing but use the testing data's file path.
```py
test_df = pd.read_csv("datasets/test.csv")

test_df.head()
```
![test_df](https://user-images.githubusercontent.com/41812358/123644330-63169980-d879-11eb-8d1d-1cc0f1a681b8.png)
