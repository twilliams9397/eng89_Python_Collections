- How to create new project in Pycharm: `click file` then `new project`
  then `enter name` click `create`

# Python Data Collections
- Lists
- Tuples
- Dict
- Sets

Lists (AKA array in other languages)
- shopping list (multiple items)
- add, edit, delete, update
- what is `CRUD` - `Create` `Read` `Update` `Delete`
```python
shopping_list = ["apples", "eggs", "dark chocolate", "tea"]
print(shopping_list)
# check data type:
print(type(shopping_list))

# access items from list - indexing
print(shopping_list[2]) # third item, index starts at 0
print(shopping_list[-1]) # last item

# replace items in list
shopping_list[0] = "mango" # replaces at specific index
print(shopping_list)
# add item to shopping list
shopping_list.append("tuna")
print(shopping_list)

# search python documentation and find out how to delete item from this list
shopping_list.remove(shopping_list[3]) # deletes item at specific index
print(shopping_list)
shopping_list.remove("mango") # deletes specific item from list
print(shopping_list)
```
can also use `list.pop(index)` to remove add index

#### What are tuples and whats the difference between lists and tuples?
`syntax () - name_tuple = ("", "", "")`

```python
essentials = ("paracetamol", "milk", "butter")
print(essentials)
print(type(essentials))

essentials.pop(1) this line would give attribute error
print(essentials)
```
this above code will return an error as lists are MUTABLE tuples are IMMUTABLE

## Dictionaries and sets are both Data collections in python

Dictionaries and sets are both Data collections in python

Dicts are another way to manage data but can be a little more dynamic
- Dict work as KEY and VALUE
- KEY = the reference of the object
- VALUE = data that is stored for the key
- dynamic as we have Lists and another dict inside a dict
- Syntax - `name = {}`, `key = {value}`
```python
student_1 = {
    "name": "James",
    "stream": "DevOps",
    "completed_lessons": 4,
    "completed_lessons_names": ["data types", "git and github", "operators", "lists and tuples"]
}

# check syntax by printing
# print(student_1)
# print(type(student_1))
print(student_1["stream"]) # accessing specific key to return value
print(student_1["completed_lessons_names"][1]) # accessing index in list value
print(student_1["completed_lessons_names"][-2])

# can we apply CRUD
student_1["completed_lessons"] = 3 # change value for key
print(student_1["completed_lessons"])

student_1["completed_lessons_names"].remove("operators") # remove item from value list
print(student_1["completed_lessons_names"])

# we have built in methods to use with dict
# to print all keys .keys()
print(student_1.keys())

# to print all values .values()
print(student_1.values())
```
## Sets are also data collection
- syntax `name = {"", "", ""}`
- sets are unordered
```python
shopping_list = ["eggs", "tea", "milk"]
print(shopping_list)
car_parts = {"engine", "wheels", "windows"}
print(car_parts) # re printing will change order in print

car_parts.add("seats")
print(car_parts)
car_parts.discard("wheels")
print(car_parts)
```