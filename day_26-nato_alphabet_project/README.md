# List and Dictionary Comprehension

## Overview
List
```py
new_list = [new_item for item in list if test]
```
Dictionaries
```py
new_dict = {new_key:new_value for item in list}
```
List here means any form of iterable

A dictionary/list comprehensino is just a new way of creating one or the other using shorthand syntax.

Taking it one step further, we can make a new dictionary based on the values in an existing dictionary
```py
new_dict = {new_key:new_value for (key, value) in dict.items()}
```
We can also add our conditions as with lists
```py
new_dict = {new_key:new_value for (key, value) in dict.items() if test}
```

## How to Iterate over a pandas Dataframe
```py
for (key, value) in student_data_frame.items():
	print(key, value)
```
This method loops through a dataframe the same way we would a dictionary. Pandas has an inbuilt method called `iterrows` allows us to loop through each row
```py
for (index, row) in student_data_frame.iterrows():
	print(row) # or print(index)
```
Access row data 
```py
for (index, row) in student_data_frame.iterrows():
	print(row.student)
```
