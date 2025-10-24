#Create a Python program that collects book titles from a user. Your program should use a while loop to prompt the user to enter a total of 10 book titles.

#Starts the main function.
def main():
    #Make an empty list to store book titles.
    book_titles = []

    #Use a while loop to collect 10 book titles from the user.
    while len(book_titles) < 10:
        title = input("Enter book title: ")
        #Capitalize the title using the title() method.
        capitalized_title = title.title()
        #Add the capitalized title to the list.
        book_titles.append(capitalized_title)

    #After collecting all titles, print the list of book titles.
    print("\nList of Book Titles:")
    for book in book_titles:
        print(book)

    #Once all tiles are collected, saves them to a new list, then sorts them alphabetically.
    books_sorted = sorted(book_titles)
    print("\nSorted List of Book Titles:")
    for book in books_sorted:
        print(book)
#Call the main function to execute the program.
if __name__ == "__main__":
    main()

