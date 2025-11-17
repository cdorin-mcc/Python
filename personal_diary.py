def main():
    #Writing user input to a file.
    current_date_time = input("Enter the current date and time: ")
    diary_entry = input("Write your diary entry: ")

    #Creates a file in append mode.
    with open("Diary/diary.txt", "a") as diary_file:
        #Writes the date, time, and diary entry to the file
        diary_file.write(f"{current_date_time}\n")
        diary_file.write(f"{diary_entry}\n")
        diary_file.write("\n")  # Add a newline for better readability
        #Closes the file using close() method
        diary_file.close()
main()
