# Define a function named `update_file` that takes in two parameters:`import_file` and `remove_list`
def update_file(import_file, remove_list):
# Build `with` statement to read in the initial contents of the file
with open(import_file, "r") as file:
# Use `.read()` to read the imported file and store it in a variable named `ip_addresses`
ip_addresses = file.read()
# Use `.split()` to convert `ip_addresses` from a string to a list
ip_addresses = ip_addresses.split()

# Build iterative statement
# Name loop variable `element`
# Loop through `ip_addresses`

for element in ip_addresses:
# Build conditional statement
# If current element is in `remove_list`,
if element in remove_list:
# then current element should be removed from `ip_addresses`
ip_addresses.remove(element)
# Convert `ip_addresses` back to a string so that it can be written into the text file
ip_addresses = " ".join(ip_addresses)
# Build `with` statement to rewrite the original file
with open(import_file, "w") as file:
# Rewrite the file, replacing its contents with `ip_addresses`
file.write(ip_addresses)
# Call `update_file()` and pass in "allow_list.txt" and a list of IP addresses to be removed
update_file("allow_list.txt", ["192.168.25.60", "192.168.140.81", "192.168.203.198"]
	
# Build `with` statement to read in the updated file
with open("allow_list.txt", "r") as file:
# Read in the updated file and store the contents in `text`
text = file.read()
# Display the contents of `text`
print(text)

"""
Print result:
ip_address 192.168.205.12 192.168.6.9 192.168.52.90 192.168.90.124
192.168.186.176 192.168.133.188 192.168.218.219 192.168.52.37 192.168.156.224
192.168.60.153 192.168.69.116
"""

"""
Python has functions and syntax that help you import and parse text files.
	The with statement allows you to efficiently handle files.
	The open() function allows you to import or open a file. It takes in the name of the file as the first parameter and a string that indicates the purpose of opening the file as the second parameter.
		Specify "r" as the second parameter if you're opening the file for reading purposes.
		Specify "w" as the second parameter if you're opening the file for writing purposes.

The .read() method allows you to read in a file.

The .write() method allows you to append or write to a file.

You can use a for loop to iterate over a list.

You can use an if statement to check if a given value is in a list and execute a specific action if so.
You can use the .split() method to convert a string to a list.

You can use Python to compare contents of a text file against elements of a list.

Algorithms can be incorporated into functions. When defining a function, you must specify the parameters it takes in and the actions it should execute.

"""
