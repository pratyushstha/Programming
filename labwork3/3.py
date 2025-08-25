#Write a function book_info(title, author, year) that prints book details.Call the function using keyword arguments in different orders.
# Function definition
def book_info(title, author, year):
    print("Book Information:")
    print(f"Title : {title}")
    print(f"Author: {author}")
    print(f"Year  : {year}")

# Function calls using keyword arguments in different orders
book_info(title="1984", author="George Orwell", year=1949)

print()

book_info(author="J.K. Rowling", year=1997, title="Harry Potter and the Philosopher's Stone")

print()

book_info(year=1869, title="War and Peace", author="Leo Tolstoy")
