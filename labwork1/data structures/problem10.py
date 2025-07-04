#input key-value pairs from the user and enter in a dictionary. allow user to search for the key and return its value
# Initialize an empty dictionary
my_dict = {}

# Input number of key-value pairs
n = int(input("How many key-value pairs do you want to enter? "))

# Input key-value pairs
for i in range(n):
    key = input(f"Enter key #{i+1}: ")
    value = input(f"Enter value for '{key}': ")
    my_dict[key] = value

# Search for a key
search_key = input("\nEnter the key you want to search for: ")

# Return the value if key exists
if search_key in my_dict:
    print(f"Value for '{search_key}' is: {my_dict[search_key]}")
else:
    print(f"Key '{search_key}' not found in the dictionary.")
