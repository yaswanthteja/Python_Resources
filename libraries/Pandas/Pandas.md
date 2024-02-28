# Pandas

Pandas is a popular open-source data manipulation and analysis library for Python. It provides data structures and functions needed to efficiently manipulate large datasets and perform various data analysis tasks. Pandas is built on top of the NumPy library and is widely used in data science, machine learning, and data analysis projects. Some of the key features of Pandas include:

1. **DataFrame**: The core data structure in Pandas is the DataFrame, which is a two-dimensional tabular data structure with labeled axes (rows and columns). It allows you to store and manipulate structured data easily.
2. **Series**: A Series is a one-dimensional labeled array that can hold data of various types, similar to a column in a spreadsheet. It's the building block of a DataFrame.
3. **Data Alignment**: Pandas automatically aligns data by label, making it easy to work with datasets with missing or misaligned data.
4. **Data Cleaning and Transformation**: Pandas provides a wide range of functions for data cleaning, transformation, and reshaping, such as handling missing values, filtering, sorting, grouping, and merging.
5. **Indexing and Selection**: You can select, filter, and manipulate data using intuitive indexing methods, including label-based indexing, integer-based indexing, and Boolean indexing.
6. **Time Series Data**: Pandas has robust support for working with time series data, including date and time manipulation, resampling, and time zone handling.
7. **Input/Output**: Pandas supports reading and writing data in various formats, including CSV, Excel, SQL databases, and JSON.
8. **Statistical and Mathematical Operations**: Pandas provides a variety of statistical and mathematical functions for data analysis, including mean, median, sum, standard deviation, correlation, and more.
9. **Visualization**: While not a visualization library itself, Pandas integrates well with visualization libraries like Matplotlib and Seaborn, allowing you to create plots and visualizations from your data.
10. **Integration with Other Libraries**: Pandas is often used alongside other libraries in the PyData ecosystem, such as NumPy, Matplotlib, Seaborn, and Scikit-learn.

Here's a simple example of how you can use Pandas to load and manipulate data from a CSV file:

```python
import pandas as pd

# Load data from a CSV file into a DataFrame
data = pd.read_csv('data.csv')

# Display the first few rows of the DataFrame
print(data.head())

# Perform basic data analysis
mean_age = data['Age'].mean()
max_salary = data['Salary'].max()

print("Mean Age:", mean_age)
print("Max Salary:", max_salary)

# Filter and select data
young_employees = data[data['Age'] < 30]
high_salary_employees = data[data['Salary'] > 50000]

# Save the filtered data to a new CSV file
young_employees.to_csv('young_employees.csv', index=False)
```

# How to install Pandas

1. using pip

```python
pip install pandas

or
python -m pip install pandas
```

1. Anaconda

```python
conda install pandas
```

1. Unix or Debian

```python
sudo apt-get install python-pandas
```

1. Ubuntu

```python
sudo apt-get install build-essential python-all-dev
```

## How to check Pandas Installed or not

Open your terminal and run python

```python
python
>>> import pandas
>>> pandas.__version__
'0.18.0'
```

# Data Structures in Pandas

At the core of pandas are three data structures:

```python
DATA STRUCTURE DIMENSIONALITY SPREADSHEET ANALOG
------------------------------------------------
Series       |   1D      |    Column
DataFrame    |   2D      |    Single Sheet
Panel        |   3D      |    Multiple Sheets

```

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/a898e757-613c-4037-87c2-dbd727725984/Untitled.png)

Pandas provides two main data structures for working with tabular data: **`Series`** and **`DataFrame`**. These structures are built on top of the NumPy library and offer powerful capabilities for data manipulation, analysis, and exploration.

1. **Series**:
    - A **`Series`** is a one-dimensional labeled array that can hold data of any type (integer, float, string, etc.).
    - It's similar to a column in a spreadsheet or a single-dimensional array.
    - Each element in a Series has a label, called an index, which allows for easy and efficient data access.
    - Series are often used to represent a single variable or data column.
2. **DataFrame**:
    - A **`DataFrame`** is a two-dimensional tabular data structure with labeled axes (rows and columns).
    - It's similar to a spreadsheet or a SQL table.
    - Each column in a DataFrame is a Series, and all columns share the same index.
    - DataFrames can hold data of different types, making them versatile for heterogeneous datasets.
    - DataFrames are commonly used for data manipulation, analysis, and exploration.

Here's a brief overview of how to create and work with these data structures:

```python
import pandas as pd

# Creating a Series
data = [10, 20, 30, 40, 50]
index = ['a', 'b', 'c', 'd', 'e']
series = pd.Series(data, index=index)
print(series)

# Creating a DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 22],
    'Salary': [50000, 60000, 45000]
}
df = pd.DataFrame(data)
print(df)

# Accessing elements in a Series or DataFrame
print(series['b'])  # Accessing a value in a Series using index label
print(df['Name'])   # Accessing a column in a DataFrame

# Adding a new column to a DataFrame
df['Gender'] = ['F', 'M', 'M']
print(df)

# Applying operations on Series and DataFrame
df['Age'] = df['Age'] + 1  # Incrementing values in a column
print(df)

# Filtering data
young_employees = df[df['Age'] < 30]
print(young_employees)

# Grouping and aggregation
grouped = df.groupby('Gender')['Salary'].mean()
print(grouped)

# Reading and writing data
df.to_csv('employees.csv', index=False)
new_df = pd.read_csv('employees.csv')
print(new_df)
```

1. **Panel**

- The **`Panel`** data structure was an important part of Pandas in its earlier versions, but it has been deprecated since Pandas version 0.25.0.
- As of my knowledge cutoff date in September 2021, the **`Panel`** has been removed from the core Pandas library and is no longer recommended for use. Instead, the focus in Pandas is on using the more versatile and powerful **`DataFrame`** and **`Series`** structures to handle data.
- The **`Panel`** was designed to handle three-dimensional data (similar to how a **`DataFrame`** handles two-dimensional data), but it was found that most use cases could be adequately handled using **`DataFrame`** objects.
- Therefore, the **`Panel`** was deprecated to simplify the Pandas library and encourage users to work with **`DataFrame`** and **`Series`** structures.
- If you are working with multi-dimensional data, consider using a combination of **`DataFrame`** objects and hierarchical indexing (MultiIndex). Hierarchical indexing allows you to represent and manipulate higher-dimensional data within the **`DataFrame`** structure.
- Here's an example of how you might represent multi-dimensional data using hierarchical indexing:
