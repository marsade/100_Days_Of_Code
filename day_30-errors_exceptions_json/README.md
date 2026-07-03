# Day 30 - Learning about Exceptions and Improving Password Manager App

## Overview
This lecture focuses on error handling in python. In our programs, we can catch eexceptions so the program wont fail catastrophically, we can fail more gracefully or decide that something else should happen.

## Some common errors
- FileNotFound
```py
with open("a_file.txt) as file:
	file.read()
```

- KeyError
```py
a_dictionary = {"key": "value"}
value = a_dictionary["a non-existent key"]
```

- IndexError
```py
fruit_list = ["Apple", "Banana", "Pear"]
fruit = fruit_list[3]
```

- TypeError
```py
text = "abc"
print(text + 5)
```
## Dealing with exceptions
- `try`: This is the block of code comes when you're executing something that might cause an exception. 
- except: This is what you want executed if there was an exception (something went wrong)
```py
try:
	file = open("a_file.txt")
except:
	print("There was an error")
```
Here, since the try block raises an error, the except block will be executed. According to PEP8 regulations, you should never use a bare except because it catches all possible errors. \it is common to have multiple except blocks
```py
try:
	file = open("a_file.txt")
	a_dictionary = {"key": "value"}
	print(a_dictionary["adsdrr"])
except FileNotFoundError:
	file = open("a_file.txt", "w")
	file.write("Something")
except KeyError as error_message:
	print(f"The key {error_message} does not exist.")
```
- `else`: Piece of code you want to be executed if there were no exceptions. This can occur when the code succeeded and there were no problems.
```py
try:
	file = open("a_file.txt")
	a_dictionary = {"key": "value"}
	print(a_dictionary["key"])
except FileNotFoundError:
	file = open("a_file.txt", "w")
	file.write("Something")
except KeyError as error_message:
	print(f"The key {error_message} does not exist.")
else:
	content = file.read()
	print(content)
```
The second time running this codw will not have any exceptions so `Something` will be printed to the console.
- `finally`: This is a block of code to execute no matter what happens.
```py
try:
	file = open("a_file.txt")
	a_dictionary = {"key": "value"}
	print(a_dictionary["adsdrr"])
except FileNotFoundError:
	file = open("a_file.txt", "w")
	file.write("Something")
except KeyError as error_message:
	print(f"The key {error_message} does not exist.")
else:
	content = file.read()
	print(content)
finally:
	file.close()
	print("File was closed")
```

## Raising Exceptions
When dealing with exceptions and error handling we have covered the 4 keywords that are the most important. The final one is called `raise` and it allows us to raise our own exception. To do that, you have to tap into one of the known exception classes
```py
try:
	file = open("a_file.txt")
	a_dictionary = {"key": "value"}
	print(a_dictionary["adsdrr"])
except FileNotFoundError:
	file = open("a_file.txt", "w")
	file.write("Something")
except KeyError as error_message:
	print(f"The key {error_message} does not exist.")
else:
	content = file.read()
	print(content)
finally:
	raise TypeError("This is an error I made up")
```
## When you might want to raise exceptions
In cases where perfectly valid code and/or inputs may bring wrong results. In this bmi calculator examole, a `ValueError` is raised when the height input is over 3:
```py
height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
	raise ValueError("Human Height should not be over 3 meters.")

bmi = weight/height ** 2
print(bmi)
```

## Code Exercise
[nato_main.py](nato_main.py) - Update Nato Phonetic Alphabet program with exceptions

## Challenge
- Improving Password manager app with search functionality
- Replacing saved passwords txt file to JSON
- Using python to work with JSON

## Writing to JSON
```py
json.dump(object_to_dump, file_name, optional:indent)
```

## Reading from JSON
```py
json.load(file_name)
```
## How to update JSON
We have first have to load data then update
```py
data = json.load(data_file)
data.update(new_data)
```