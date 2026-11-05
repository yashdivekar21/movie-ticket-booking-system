# Movie Ticket Booking System

movies = {
    1: {"name": "Avengers", "price": 200},
    2: {"name": "Inception", "price": 180},
    3: {"name": "Interstellar", "price": 250}
}

# Available seats for each movie
seats = {
    1: ["A1", "A2", "A3", "A4", "A5"],
    2: ["B1", "B2", "B3", "B4", "B5"],
    3: ["C1", "C2", "C3", "C4", "C5"]
}

booked_seats = {
    1: [],
    2: [],
    3: []
}


def display_movies():
    print("\n----- AVAILABLE MOVIES -----")

    for number, movie in movies.items():
        print(number, ".", movie["name"],
              "- Rs.", movie["price"])


def book_ticket():
    display_movies()

    try:
        choice = int(input("\nEnter movie number: "))

        if choice not in movies:
            print("Invalid movie selection!")
            return

        print("\nAvailable seats:", seats[choice])

        selected_seats = input(
            "Enter seat numbers separated by commas: "
        ).upper().replace(" ", "").split(",")

        # Check whether the seats exist
        for seat in selected_seats:
            if seat not in seats[choice]:
                print("Invalid seat:", seat)
                return

        # Check whether the seats are already booked
        for seat in selected_seats:
            if seat in booked_seats[choice]:
                print("Seat", seat, "is already booked!")
                return

        # Book the selected seats
        for seat in selected_seats:
            booked_seats[choice].append(seat)

        total = len(selected_seats) * movies[choice]["price"]

        print("\n----- BOOKING CONFIRMED -----")
        print("Movie:", movies[choice]["name"])
        print("Seats:", ", ".join(selected_seats))
        print("Total Amount: Rs.", total)
        print("Thank you for booking!")

    except ValueError:
        print("Please enter a valid number!")


def main():
    while True:
        print("\n===== MOVIE TICKET BOOKING =====")
        print("1. View Movies")
        print("2. Book Tickets")
        print("3. Exit")

        try:
            option = int(input("Enter your choice: "))

            if option == 1:
                display_movies()

            elif option == 2:
                book_ticket()

            elif option == 3:
                print("Thank you! Visit again.")
                break

            else:
                print("Invalid choice! Try again.")

        except ValueError:
            print("Please enter a valid number!")


main()