# Creating a demo file
with open("demo.txt", "w") as f:
    f.write("Hello, this is a file handling example.")

# Reading the file using seek()
with open("demo.txt", "r") as f:
    print("Initial read:", f.read(5))  # Read first 5 characters
    
    f.seek(0)  # Move pointer back to the beginning
    print("After seek(0):", f.read(5))  # Again read first 5 characters
    
    f.seek(7)  # Move to position 7
    print("From position 7:", f.read(4))  # Read 4 characters from position 7
