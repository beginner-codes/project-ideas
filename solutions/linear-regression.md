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

## Looking Around Our Dataset
Now before using any data to train models, we need to make sure that the data is usable and suitable for a machine model. This is done during the data exploration and cleaning phases. As the dataset we are using is quite simple and is almost ready to be used, I am combining both the data exploration part and the data cleaning parts together. This also means that the data will probably not need much cleaning. 

**Remember:** Other datasets (especially real life ones) will need a lot more throrough exploration and cleaning than the dataset being used in this project. Every dataset is different and so differing techniques may be required from the ones shown in this project solution.

Once again we look at each ofthe individual datasets seperately when exploring and cleaning the datasets.

#### Training data

##### Shape and datatypes of our data
In Pandas, dataframes have a lot of useful methods and attributes that can be extremely helpful. Now something that I normally like to do when working with data is to see exactly how much data we have. So this means I would like to know how many datapoints we have (rows of the dataframe), and how many columns we have. To do this we simply use the `DataFrame.shape` attribute which will return the number of rows and columns as a tuple (rows, columns).

```py
train_df.shape
```
This returns `(700, 2)` signifying that our dataset has 700 rows and 2 columns. 

After this, I wanted to check if our data was suitable for a linear regression model. For data to be suitable for this purpose, it needs to satisfy some requirements such as the values need to be numeric, have a linear correlation, there are no missing values, etc.


To make sure that the values are numeric, we use the `DataFrame.dtypes` attribute like this:
```py
train_df.dtypes

# x    float64
# y    float64
# dtype: object
```

And we see that both `x` and `y` are float64 and so the values are numeric variables.


##### Missing values
Next I wanted to see if there were any missing values and if so, remove them. There are other ways to deal with missing values but for simplicity I decided to just remove it.

One easy way to check how many missing values are in our data, we use two pandas methods: `DataFrame.isnull()` and `DataFrame.sum()`. What the `isnull()` method does is, for every value in the dataframe, if it is null or invalid or missing, then it will represent that as `False` otherwise it will be `True`. This creates a new dataframe where every value is replaced with a boolean value. From there, we can chain the `sum()` method on the boolean dataframe which will sum up all the values in each row. As `False` can be represented as 0 and `True` can be represented as 1, if we see that a column has a summed value of more than 0, then there are missing values.

```py
train_df.isnull().sum()

# x    0
# y    1
# dtype: int64
```

We see that the `y` column has one missing value. If we wanted to see what row this is, we can run `train_df[train_df["y"].isnull()]`. I won't explain how this code works in this walkthrough but it's mostly just Pandas indexing which is pretty straightfoward. If you want to get an explanation behind that code, ask me in the beginner.py server and ping me (@wang$5464).

To remove all missing values we run
```py
train_df = train_df.dropna()
```
This drops the rows containing null values and then we reassign `train_df` to the new dropped null values dataframe.

Lastly we check if there are any more null values by running
```py
train_df.isnull().any()

# x    False
# y    False
# dtype: bool
```
This is similar to what we did before but we are now using the `DataFrame.any()` method which returns `True` if at least one value in the column is `True` else it will return `False`.

##### Checking linearity
The last thing I did was to check if the two variables `x` and `y` are linearly correlated and there are not too many outliers. This can be done with a simple plot of the data using either matplotlib, seaborn, or any other data visualisation library. I will be using seaborn as I like how easy it is to use and how the plots are better looking than matplotlib (in my opinion).

```py
sns.scatterplot(x="x", y="y", data=train_df);
```

`sns.scatterplot()` creates a scatterplot where the x axis is equal to `train_df[x]` and the y axis is equal to `train_df[y]`.

![image](https://user-images.githubusercontent.com/41812358/127419070-38e658ae-aa9c-4822-b8fe-3c8ce84c2c8d.png)

So we see that the data is linearly correalated and also there are not any obvious outliers. This means that a linear regression model is suitable for the data.

#### Testing Data
For the testing data, I did something similar to what I did with the training data.

#### Model Building
Now it's time to finally build something. So the linear regression model I will be using is part of the sci-kit learn library that you previously installed. The way we import it is by using the following code: 
```py
from sklearn.linear_model import LinearRegression
```

Next, I created variables for the training X and y data, and the testing X and y data.

```py
X_train, y_train, X_test, y_test = train_df[["x"]], train_df["y"], test_df[["x"]], test_df["y"]
```
This makes it a lot easier to know what part of the data we are using.


We then create a linear regression model object by running `model = LinearRegression()`. I just called it model however, like any variable in this tutorial, you can call it whatever you like. So now that we have a linear regression model object in the variable `model`, we can now train it with the `fit()` method.

```py
model.fit(X_train, y_train)
```

The `fit()` method takes two arguments: training X and training y which is what we put in the brackets. After runnning that line of code, our linear regression model has now trained itself on the training data.

Lastly, to get the parameters of the model (slope and y-intercept), we access the `coef_` and `intercept_` attributes by running:
```py
model.coef_     # array([1.00065638])

model.intercept_      # -0.10726546430097272
```
This means that our linear regression's fomula is `y = 1.00065638x - 0.1072655`.

## Conclusion
So this project walkthrough went through the basics of building a linear regression model with simple data cleaning, visualisation, and model building. Of course machine learning is never actually this straightfoward and there are normally more steps such as model evaluation, but this was just a simple taste of the field of data science/machine learning :).
