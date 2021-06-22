# # Let's create a shopping list
# # Syntax [] - name_of_list = ["", "", ""]
#
# shopping_list = ["apples", "eggs", "dark chocolate", "tea"]
# print(shopping_list)
# # check data type:
# print(type(shopping_list))
#
# # access items from list - indexing
# print(shopping_list[2]) # third item, index starts at 0
# print(shopping_list[-1]) # last item
#
# # replace items in list
# shopping_list[0] = "mango" # replaces at specific index
# print(shopping_list)
# # add item to shopping list
# shopping_list.append("tuna")
# print(shopping_list)
#
# # search python documentation and find out how to delete item from this list
# shopping_list.remove(shopping_list[3]) # deletes item at specific index
# print(shopping_list)
# shopping_list.remove("mango") # deletes specific item from list
# print(shopping_list)
# # can also use list.pop(index) to remove add index
#
# mix_list = [1, 2, 3, "one", "two", "three"] #lists can be a mix of data types, e.g. ints and strings
# print(mix_list)

# What are tuples and whats the difference between lists and tuples?
# Tuples syntax () - name_tuple = ("", "", "")

essentials = ("paracetamol", "milk", "butter")
print(essentials)
print(type(essentials))

# essentials.pop(1) this line would give attribute error
# print(essentials)
# lists are MUTABLE tuples are IMMUTABLE