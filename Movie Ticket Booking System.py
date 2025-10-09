# 🎬 Movie Ticket Booking System 

# Step 1: Setup Data
movies = [
    {"name": "Mirai", "price": 280, "rating": "UA", "seats": 60},
    {"name": "Hanuman", "price": 250, "rating": "U", "seats": 55},
    {"name": "Coolie", "price": 280, "rating": "A", "seats": 50},
    {"name": "Salaar", "price": 320, "rating": "A", "seats": 35},
    {"name": "They Call Him OG", "price": 260, "rating": "A", "seats": 30},
    {"name": "Bahubali 2", "price": 280, "rating": "U", "seats": 80},
    {"name": "Hi Nanna", "price": 260, "rating": "U", "seats": 50},
    {"name": "Dasara", "price": 280, "rating": "UA", "seats": 45},
    {"name": "Jersey", "price": 250, "rating": "U", "seats": 40}
]

# Step 2: Display Movies
def show_movies():
    print("\n Available Movies:")
    print("-" * 75)
    print(f"{'No.':<5}{'Movie Name':<30}{'Price':<10}{'Rating':<10}{'Seats Left'}")
    print("-" * 75)
    for i, movie in enumerate(movies, start=1):
        print(f"{i:<5}{movie['name']:<30}{movie['price']:<10}{movie['rating']:<10}{movie['seats']}")
    print("-" * 75)

#  Calculate Bill
def calculate_bill(price, tickets):
    subtotal = price * tickets
    gst = subtotal * 0.05
    total = subtotal + gst
    return subtotal, gst, total

# Step 3 & 4: Handle Booking
def book_tickets():
    show_movies()
    
    try:
        choice = int(input("👉 Enter the movie number you want to book: "))
        if choice < 1 or choice > len(movies):
            print(" Invalid movie selection.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return

    movie = movies[choice - 1]
    
    # Get ticket count
    try:
        tickets = int(input(f"️ How many tickets for '{movie['name']}'? "))
    except ValueError:
        print(" Please enter a valid number of tickets.")
        return

    # Booking rules
    if tickets > 6:
        print("️ You can book a maximum of 6 tickets per transaction.")
        return
    if tickets > movie['seats']:
        print(f"️ Only {movie['seats']} seats left. Try fewer tickets.")
        return
    
    # Age check for A-rated movies
    if movie['rating'] == "A":
        try:
            age = int(input(" Enter your age: "))
        except ValueError:
            print(" Please enter a valid age.")
            return
        if age < 18:
            print(" You must be 18+ to watch an A-rated movie.")
            return
    
    # Step 5: Calculate the bill
    subtotal, gst, total = calculate_bill(movie['price'], tickets)
    
    # Step 6: Update Seats
    movie['seats'] -= tickets
    
    # Step 7: Booking Summary
    print("\n Booking Successful!")
    print("-" * 60)
    print(f" Movie Name     : {movie['name']}")
    print(f"️ Tickets Booked : {tickets}")
    print(f" Subtotal       : ₹{subtotal:.2f}")
    print(f" GST (5%)       : ₹{gst:.2f}")
    print(f" Total Amount   : ₹{total:.2f}")
    print(f" Seats Left     : {movie['seats']}")
    print("-" * 60)
    print(" Enjoy your movie!\n")

# Step 8: Main System Loop
def movie_system():
    print("️ Welcome to CineMax Telugu Movie Booking System ️")
    while True:
        book_tickets()
        cont = input("Do you want to make another booking? (yes/no): ").strip().lower()
        if cont not in ("yes", "y"):
            print("\n Thank you for using CineMax! Have a great day!")
            break

# Run the system
if __name__ == "__main__":
    movie_system()
