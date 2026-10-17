import random

# Predefined Rates and Routes
cab_rates = {
    1: {"name": "Auto", "rate": 12},
    2: {"name": "Sedan", "rate": 18},
    3: {"name": "SUV", "rate": 25}
}

routes = {
    1: {"source": "Pune Station", "dest": "Shivajinagar", "dist": 5},
    2: {"source": "Swargate", "dest": "Kothrud", "dist": 8},
    3: {"source": "Hinjawadi", "dest": "Wakad", "dist": 10}
}

while True:
    # Step 1: Main Menu
    print("\n--- Cab Booking Chatbot ---")
    print("1. Book Ride")
    print("2. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        # Step 2: Choose cab type
        print("\nChoose cab type:")
        print("1. Auto - Rs 12/km")
        print("2. Sedan - Rs 18/km")
        print("3. SUV - Rs 25/km")
        cab_choice = input("Enter cab type (1-3): ")

        if cab_choice not in ['1','2','3']:
            print("Invalid cab type! Returning to main menu.")
            continue

        cab_choice = int(cab_choice)
        selected_cab = cab_rates[cab_choice]

        # Step 3: Choose route
        print("\nChoose route:")
        print("1. Pune Station -> Shivajinagar (5 km)")
        print("2. Swargate -> Kothrud (8 km)")
        print("3. Hinjawadi -> Wakad (10 km)")
        route_choice = input("Enter route (1-3): ")

        if route_choice not in ['1','2','3']:
            print("Invalid route! Returning to main menu.")
            continue

        route_choice = int(route_choice)
        selected_route = routes[route_choice]

        # Step 4: Calculate fare
        distance = selected_route["dist"]
        rate = selected_cab["rate"]
        fare = distance * rate

        print("\n--- Booking Details ---")
        print(f"Route: {selected_route['source']} to {selected_route['dest']}")
        print(f"Distance: {distance} km")
        print(f"Cab Type: {selected_cab['name']}")
        print(f"Rate: Rs {rate}/km")
        print(f"Total Fare: Rs {fare}")

        # Step 5: Cancellation before OTP
        print("\n1. Confirm & Share OTP")
        print("2. Cancel Ride")
        confirm = input("Enter choice: ")

        if confirm == '2':
            print("Ride cancelled. Returning to main menu.")
            continue
        elif confirm == '1':
            # Step 6: OTP and ride lock
            otp = random.randint(1000, 9999)
            print(f"\nBooking Confirmed! Your OTP is: {otp}")
            print(f"Driver is on the way. OTP has been shared.")
            print("Note: Ride cannot be cancelled after OTP sharing.")
        else:
            print("Invalid choice. Returning to main menu.")

    elif choice == '2':
        # Step 7: Exit
        print("Thank you for using Cab Booking Chatbot. Goodbye!")
        break
    else:
        print("Invalid choice! Please enter 1 or 2.")

