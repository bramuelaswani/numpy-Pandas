import numpy as np

def create_numpy_array():
    """Returns a NumPy array with range 
    from 1 up to and including 5.

    >>> create_numpy_array()
    array([1, 2, 3, 4, 5])
    """
    return np.array([1, 2, 3, 4, 5])


##2
import numpy as np

python_list = list(range(5))
numpy_array = np.array(range(5))
python_list, numpy_array

##3
inclusive_begin = 3
exclusive_end = 10
np.arange(inclusive_begin, exclusive_end)


##4
size = (1, 2, 3) # Could also be (1, 2) or (4, 3, 2, 1, ...), etc. 
np.random.random_sample(size=size)


###5
size = (1, 2, 3)
shape_ex = np.random.random_sample(size=size)

shape_ex.reshape(1, 6).shape, shape_ex.flatten().shape