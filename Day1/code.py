
import json


def calculate_mean(arr):
    sum_of_elem = 0
    for elem in arr:
        sum_of_elem = sum_of_elem + elem
    arr_mean = sum_of_elem/len(arr)
    return arr_mean
    
arr = input('Enter the array: ')
arr_dict = json.loads(arr)
arr_mean = calculate_mean((arr_dict['arr']))
print(arr_mean)