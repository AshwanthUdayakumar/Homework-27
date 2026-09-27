import numpy as np
arr=np.arange(10)
print("Original array:",arr)
new_arr=np.where(arr%2==0,-1,arr)
print("Array with odd numbers replaced:",new_arr)
arr_2d=arr.reshape(2,5)
print("2D array:",arr_2d)
even_sum=0
for i in arr:
    if i%2==0:
        even_sum+=i
print("Sum of even numbers:",even_sum)