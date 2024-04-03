import streamlit as st

# Set page title and header
st.set_page_config(page_title="Pandas Tutorial", layout="wide")
st.title("Pandas Tutorial")

def pandas():
    st.header("1.Pandas")
    st.subheader("Pandas is a Python library used for data manipulation and analysis."
         " It provides data structures and functions for efficiently handling structured data, "
         "such as tabular data, making it essential for tasks like data cleaning, exploration, and analysis in data science and analytics workflows.\n\n\n\n\n\n")
    libraries = ['NumPy', 'pandas', 'Matplotlib', 'scikit-learn', 'Seaborn']
    usage_percentages = [80, 85, 70, 75, 60]  # Example usage percentages (can be adjusted)

    # Create a Streamlit app
    st.header('Usage of Data Science Libraries')

    # Display the usage percentages in a bar chart using Streamlit
    st.bar_chart({library: percentage for library, percentage in zip(libraries, usage_percentages)})

    st.markdown("---")
# Define sections with headers
def importing():
    st.header("2. Importing Pandas & IDE's")
    code_1 = "import pandas as pd"
    st.code(code_1)
    st.write("Import the pandas library.\n\n\n")

    st.subheader("IDE'S for compiling ")
    st.write("GOOGLE COLABS")
    st.write("Anaconda Navigator")
    st.write("PyCharm")
    st.write("VS Code")


    st.markdown("---")


def rwd():
    st.header("3. Reading and Writing Data")

# Section for CSV operations
    st.subheader("I. Read and Write CSV File")
    st.code("pd.read_csv('file.csv')")
    st.write("Read data from a CSV file into a DataFrame.")

# Section for Excel operations
    st.subheader("II. Read and Write Excel File")
    st.code("pd.read_excel('file.xlsx')")
    st.write("Read data from an Excel file into a DataFrame.")

# Section for JSON operations
    st.subheader("III. Read and Write JSON File")
    st.code("pd.read_json('file.json')")
    st.write("Read data from a JSON file into a DataFrame.")

# Section for DataFrame to file operations
    st.subheader("IV. DataFrame to CSV, Excel, JSON File")
    st.code("df.to_csv('output.csv', index=False)")
    st.code("df.to_excel('output.xlsx', index=False)")
    st.code("df.to_json('output.json', orient='records')")
    st.write("Convert DataFrame into CSV, Excel, or JSON file.")

#Exploring Data
    st.markdown("---")

def exp():
    st.header("4.Exploring Data")

    st.code("df.head(5)")
    st.write("Display the first five rows of the DataFrame\n")

    st.code("df.tail(5)")
    st.write("Display the last five rows of the DataFrame\n")

    st.code("df.sample(5)")
    st.write("Display the random five rows of the DataFrame\n")

    st.code("df.info()")
    st.write("Display information about the DataFrame, including data types and memory usage")

    st.code("df.dtypes")
    st.write("Display the datatype of the DataFrame")

    st.code("df.describe()")
    st.write("Generate descriptive statistics of numerical columns")

    st.markdown("---")

def index():
    st.header("5.Indexing and Selection")

    st.subheader("Selecting columns")
    st.code("df.column_name")
    st.write("OR")
    st.code("df['colunmn_name']")

    st.subheader("Selecting rows")
    st.code("df.loc['row_label']")
    st.write("label-based indexing ")
    st.code("df.iloc['row_label']")
    st.write("integer-based indexing")

    st.subheader("Filtering rows")
    st.code("df[df['column'] > value]")
    st.write("Boolean indexing")

    st.markdown("---")

def data_cleaning():
    st.header("6.Data Cleaning or Handling Missing Data")

    st.code("df.dropna()")
    st.write("Drop rows with missing values\n")

    st.code("df.fillna()")
    st.write("Fill missing values with specified values")

    st.code("df.isnull()")
    st.write("Or")
    st.code("df.notnull()")
    st.write("Check for missing values and return boolean masks")

    st.code("df.drop_duplicates()")
    st.write("Drop duplicate rows")
# Add a footer or closing note
    st.markdown("---")

def dm():
    st.header("7.Data Manipulation")

    st.code("df.groupby('column_name')")
    st.write(" Group DataFrame by one or more columns")

    st.code("pd.merge(df1, df2)")
    st.write("Merge two DataFrames based on a common column")

    st.code("pd.concat([df1, df2])")
    st.write("Concatenate DataFrames along rows or columns")

    st.code("df.join(df2)")
    st.write("Join DataFrames based on index or columns")

    st.code("df.pivot_table(values='value_column', index='index_column', columns='column_to_pivot', aggfunc='mean')")
    st.write(" Create a pivot table from DataFrame")

    st.code("df.agg()")
    st.write("Or")
    st.code("df.aggregate()")
    st.write("Apply aggregation functions to grouped data")

    st.markdown("---")

def da():
    st.header("8.Data Aggregation")
    code="""df.mean()
df.median()
df.sum()"""
    st.code(code)
    st.write("Calculate mean, median, and sum of columns")

    st.code("df.groupby().agg()")
    st.write("Apply custom aggregation functions")

    st.markdown("---")

def cdh():
    st.header("9.Categorical Data Handling")

    st.code("df.astype()")
    st.write("Convert data types of columns, including converting to categorical type")

    st.code("pd.Categorical()")
    st.write(" Create categorical data from arrays or Series")

    st.code("pd.get_dummies(df['column_name'])")
    st.write("Convert categorical variable into dummy/indicator variables (one-hot encoding)")

    st.markdown("---")

def tsa():
    st.header("10.Time Series Analysis")

    st.code("pd.to_datetime(df['column'])")
    st.write("Convert datetime columns")

    st.code("df.resample()")
    st.write("Resample time series data")

    st.code("df.tz_localize()")
    st.write("Or")
    st.code("df.tz_convert()")
    st.write("Time zone conversion")

    st.markdown("---")

def po():
    st.header("11.Performance Optimization")

    st.code("df.memory_usage()")
    st.write("Display memory usage of each column in the DataFrame")

    st.code("df.query()")
    st.write(" Perform query operations on DataFrame using expression strings.Use efficient data types like int32, float32 for memory optimization.")


    st.markdown("---")

def at():
    st.header("12.Advanced Topics")

    st.code("df.apply()")
    st.write("Or")
    st.code("df.applymap()")
    st.write("Apply functions element-wise or row/column-wise")

    st.code("df.pipe()")
    st.write("Apply a sequence of operations to DataFrame")

    st.code("df.melt()")
    st.write("Convert wide format to long format (tidy data)")
    st.markdown("---")

    st.markdown("Explore more Pandas functionalities in the [official documentation](https://pandas.pydata.org/docs/).")

sidebar_options={
    "Pandas":pandas,
    "Importing Pandas":importing,
    "Reading and Writing Data":rwd,
    "Exploring Data":exp,
    "Indexing and Selection":index,
    "Data Cleaning":data_cleaning,
    "Data Manipulation":dm,
    "Data Aggregation":da,
    "Categorical Data Handling":cdh,
    "Time Series Analysis":tsa,
    "Performance Optimization":po,
    "Advanced Topics":at,





}
selected_page = st.sidebar.radio("Select Page", list(sidebar_options.keys()))
sidebar_options[selected_page]()
