NUM_SEATS = 30
seats = [False] * NUM_SEATS

while True:
    print("\nCinema Seat Reservation System")
    print("1 - Reserve seat")
    print("2 - Cancel reservation")
    print("3 - Display seats")
    print("4 - Exit system")

    menu_option = input("\nChoose an option: ")

    if menu_option == '1':
        try:
            selected_seat = int(input("Enter the seat number to reserve (1 to 30): "))
            seat_index = selected_seat - 1

            if 0 <= seat_index < NUM_SEATS:
                if not seats[seat_index]:
                    seats[seat_index] = True
                    print(f"Seat {selected_seat} reserved!")
                else:
                    print(f"Seat {selected_seat} is already occupied.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    elif menu_option == '2':
        try:
            selected_seat = int(input("Enter the seat number to cancel (1 to 30): "))
            seat_index = selected_seat - 1

            if 0 <= seat_index < NUM_SEATS:
                if seats[seat_index]:
                    seats[seat_index] = False
                    print(f"Reservation for seat {selected_seat} cancelled.")
                else:
                    print(f"Seat {selected_seat} is already available.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    elif menu_option == '3':
        print("\n--- Seat Status ---")

        total_available = 0
        total_occupied = 0
        occupied_seats = ""

        for i in range(NUM_SEATS):
            if seats[i]:
                total_occupied += 1

                if occupied_seats != "":
                    occupied_seats += ", "

                occupied_seats += str(i + 1)
            else:
                total_available += 1

        print(f"Total available seats: {total_available}")
        print(f"Total occupied seats: {total_occupied}")

        if occupied_seats:
            print(f"Occupied seats: [{occupied_seats}]")
        else:
            print("No seats are occupied.")

    elif menu_option == '4':
        print("See you!")
        break

    else:
        print("Invalid option. Please choose an option from 1 to 4.")
