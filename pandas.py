import numpy as np
import pandas as pd
##1
def create_pandas_dataframe():
    """Returns a Pandas DataFrame with a 2D array 
    containing values 1, 2, 3, and 4, and columns 
    named 'column_1' and 'column_2'

    >>> create_pandas_dataframe()
       column_1  column_2
    0         1         2
    1         3         4
    """
    return pd.DataFrame(np.array([[1, 2], [3, 4]]), columns=['column_1', 'column_2'])


##2
python_list = [1, 2, 3, 4]
numpy_arr = np.array(python_list)
pandas_series = pd.Series(numpy_arr, index=["a", "b", "c", "d"])

print(python_list[0], numpy_arr[0], pandas_series[0], pandas_series["a"])
print(pandas_series['c'])

##3
pandas_series = pd.Series([1, 2, 3, 4], index=["a", "b", "c", "d"])
print(pandas_series[1:3])

##4
pandas_series = pd.Series(
    [1, 2, 3, 4],  # Python list
    index=["a", "b", "c", "d"]  # Python list
)

##5
# Define an (optional) explicit index for the DataFrame
index_list = ["costs per night", "average room capacity"]

# As Python dictionary
dataframe_dict = {
    "Amsterdam": ["$100,-", "2 people"],
    "Rotterdam": ["$110,-", "3 people"],
    "Utrecht": ["$90,-", "1 person"],
}

print(">> Python Dictionary:")
print(pd.DataFrame(dataframe_dict, index=index_list))


##6
# Define an (optional) explicit index for the DataFrame
index_list = ["costs per night", "average room capacity"]

# As Python lists
two_d_list = [["$100,-", "$110,-", "$90,-"], ["2 people", "3 people", "1 person"]]
two_d_columns = ["Amsterdam", "Rotterdam", "Utrecht"]

print("\n>> Python Lists:")
print(pd.DataFrame(two_d_list, columns=two_d_columns, index=index_list))

# Define an (optional) explicit index for the DataFrame
index_list = ["costs per night", "average room capacity"]

##7
# As NumPy arrays
np_array = np.array([["$100,-", "$110,-", "$90,-"], ["2 people", "3 people", "1 person"]])
np_columns = np.array(["Amsterdam", "Rotterdam", "Utrecht"])

print("\n>> NumPy Arrays:")
print(pd.DataFrame(np_array, columns=np_columns, index=index_list))

# Define an (optional) explicit index for the DataFrame
index_list = ["costs per night", "average room capacity"]
# As Python lists
two_d_list = [["$100,-", "$110,-", "$90,-"], ["2 people", "3 people", "1 person"]]

##8
# As Pandas Series
pd_series_1 = pd.Series([two_d_list[0][0], two_d_list[1][0]], index=index_list)
pd_series_2 = pd.Series([two_d_list[0][1], two_d_list[1][1]], index=index_list)
pd_series_3 = pd.Series([two_d_list[0][2], two_d_list[1][2]], index=index_list)

print("\n>> Pandas Series:")
print(
    pd.DataFrame(
        {"Amsterdam": pd_series_1, "Rotterdam": pd_series_2, "Utrecht": pd_series_3}
    )
)