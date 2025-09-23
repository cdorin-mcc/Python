#Create a list representing 20 seats, numbered 1 to 20.
seats = list(range(1, 21))
#Display the list of available seats to the customer.
print(seats)
#Prompt the customer to select a seat by entering a seat number. Entering 0 ends the purchasing process.
#Removes the selected seat from the list of available seats and updated the list.
#Also prompts customer with an error message if seat is invalid or already booked.
while True:
    seat_number = int(input("Input a seat number 1-20 to book your ticket, or enter 0 to end: "))
    if seat_number == 0:
        print("Exiting the booking process.")
        break
    elif seat_number < 1 or seat_number > 20:
        print("Invalid seat number. Please choose a number between 1 and 20.")
    elif seat_number not in seats:
        print("Seat has already been booked. Please choose a different seat.")
    else:
        seats.remove(seat_number)
        print(f"Seat {seat_number} booked successfully.")
        print("Remaining seats available:", seats)


