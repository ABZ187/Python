import numpy as np

myarr = np.array([[1, 2, 3], [12, 3, 6]])
print(myarr)
print(myarr.size)  # no. of elements in array
print(myarr.shape)  # rows x columns
print(myarr.dtype)
zeroes = np.zeros((3, 4), np.int8)  # zero matrix of the order
print(zeroes)
print(zeroes.shape)
print(zeroes.size)  # no of elements
myarr[1, 1] = 55  # change the element at a particular position
print(myarr)
rny = np.arange(5)  # create a array of 5 no.s from 0 t0 4
print(rny)
ls = np.linspace(1, 5, 10)  # equally spaced array from 1 to 5 with 10 parts
print(ls)
emp = np.empty((1, 3))  # empty array of given size without entries
print(emp)
emp_like = np.empty_like(myarr)
print(emp_like)
id = np.identity(5)
print(id)
print(7 * id)
arr = np.arange(18)  # single dimensional array with 18 element from 0 to 17
print(arr)
arr = arr.reshape(2, 9)
print(arr)
arr = arr.ravel()  # converting a array into single dimensional
print(arr)
x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
ar2 = np.array(x)
print(ar2)
print(ar2.sum(axis=0))  # Adds all the elements of column and make array of 1x3
print(ar2.sum(axis=1))  # Adds all the elements of row and make array of 1x3
print(ar2.T)  # Transpose
for n in ar2.flat:  # iterates elements of array row by row
    print(n)
print(ar2.ndim)  # dimensions of array
print(ar2.nbytes)  # total bytes consumed
print(ar2.argmax())  # position of max element (starting with zero)
print(ar2.argmax(axis=0))  # position of max element in a column
print(ar2.argmin())  # position of min element (starting with zero)
print(ar2.argsort())  # give the position of elements in ascending order
print(ar2.argsort(axis=0))  # give the position of elements in ascending order column wise
arr = np.array([[1, 2, 3], [10, 5, 2], [1, 0, 0]])
print(arr * ar2)  # multiplies arrays position wise
print(np.sqrt(ar2))  # sqrt of every element
print(ar2.max())  # finds max element
print(ar2.min())  # finds min element
print(np.where(ar2 > 7))  # find position of a element
print(np.count_nonzero(ar2))  # counts the number of non zero element
print(np.nonzero(ar2))  # gives position of non zero elements

a=np.random.randn(3,10) # a.shape = (12288, 150)a.shape=(12288,150)

b = np.random.randn(10, 4)# b.shape = (150, 45)$$

c = np.dot(a,b)
print(c)
print(c.shape)

a=np.random.randn(4,3) # a.shape = (4, 3)a.shape=(4,3)

b = np.random.randn(3, 2) # b.shape = (3, 2)b.shape=(3,2)

c = a*b
print(c.shape)
