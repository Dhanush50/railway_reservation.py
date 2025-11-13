"""
Railway Reservation System
A console-based application for managing train ticket bookings
"""

# Global variables
Id = 1001
passenger_detail = [] 
total_seats = 50
booked_seats = 0
avail_seats = 50
price = 2000


def register():
    """
    Register a new passenger and generate PNR number
    """
    global Id, passenger_detail
    name = input("Enter your name: ") 
    fname = input("Enter your father name: ")
    mno = int(input("Enter your mobile no: ")) 
    gender = input("Enter gender: ")
    password = input("Enter password: ")
    
    # Generate PNR number
    pnrno = name[0] + fname[-1] + gender[0] + str(Id)
    pnrno = pnrno.lower()
    
    status = False
    tickets = 0
    
    print("Registration successful!")
    print("Your PNR no is:", pnrno)
    
    # Store passenger details
    l = [pnrno, name, fname, mno, gender, password, status, tickets]
    passenger_detail.append(l)
    Id += 1


def login(): 
    """
    Login for existing passengers
    """
    global passenger_detail
    pn = input("Enter PNR NO: ")
    pw = input("Enter password: ")
    f = False
    c = 0
    
    # Verify credentials
    for j in passenger_detail:
        if pn == j[0] and pw == j[-3]:
            f = True
            break
        c += 1
    
    if f:
        print("Login successful")
        passenger_menu(c)
    else:
        print("Login Failed - Invalid PNR or Password")
        return login()


def passenger_menu(c):
    """
    Passenger menu after successful login
    """
    while True:
        print("\n--- Passenger Menu ---")
        print("1. Check availability")
        print("2. Ticket booking") 
        print("3. View status")
        print("4. Logout")
        
        try:
            a = int(input("Enter your choice: "))
            
            if a == 1:
                check_availablity()
            elif a == 2:
                ticket_booking(c)
            elif a == 3:
                view_status(c)
            elif a == 4:
                print('Logged out successfully')
                break
            else:
                print("Invalid option")
        except ValueError:
            print("Please enter a valid number")


def check_availablity():
    """
    Display available seats and pricing
    """
    global total_seats, avail_seats, booked_seats, price
    print("\n--- Seat Availability ---")
    print(f"Total seats: {total_seats}")
    print(f"Booked seats: {booked_seats}") 
    print(f"Available seats: {avail_seats}")
    print(f"Ticket price: ₹{price}")


def ticket_booking(c):
    """
    Book tickets for passenger
    """
    global booked_seats, total_seats
    try:
        bk = int(input("Enter number of seats: "))
        passenger_detail[c][-1] = bk 
        print(f"{bk} tickets added to your booking")
        view_status(c)
    except ValueError:
        print("Please enter a valid number")


def view_status(c): 
    """
    View booking status of passenger
    """
    status = passenger_detail[c][-2]
    tickets = passenger_detail[c][-1]
    
    print(f"\n--- Booking Status ---")
    print(f"PNR: {passenger_detail[c][0]}")
    print(f"Tickets booked: {tickets}")
    
    if status == True: 
        print('Status: Tickets Confirmed')
    elif status == False:
        print('Status: Waiting List')
    elif status == 'NA':
        print('Status: Tickets cancelled')


def passenger_portal(): 
    """
    Main passenger portal
    """
    while True:
        print("\n--- Passenger Portal ---")
        print("1. Register") 
        print("2. Login") 
        print("3. Go back")  
        
        try:
            a = int(input("Enter your choice: "))  
            if a == 1:
                register()
            elif a == 2: 
                login()
            elif a == 3: 
                break
        except ValueError:
            print("Please enter a valid number")


def view_passenger(): 
    """
    View all passenger details (Cashier function)
    """
    if not passenger_detail:
        print("No passengers registered yet")
        return
        
    print("\n--- All Passenger Details ---")
    for i in passenger_detail:
        print(f"PNR: {i[0]}, Name: {i[1]}, Tickets: {i[-1]}, Status: {i[-2]}")


def approve_ticket(): 
    """
    Approve ticket booking (Cashier function)
    """
    global passenger_detail, avail_seats, booked_seats
    pn = input("Enter PNR NO: ")
    found = False
    
    for i in passenger_detail:
        if pn == i[0] and i[-2] == False:
            found = True
            i[-2] = True
            
            if i[-1] <= avail_seats:
                avail_seats -= i[-1]
                booked_seats += i[-1]
                print("Ticket approved successfully") 
            else:
                print("Not enough seats available")
            break
            
    if not found:
        print('Invalid PNR No. or ticket already approved/cancelled')


def cancel_ticket():
    """
    Cancel ticket booking (Cashier function)
    """
    global passenger_detail, avail_seats, booked_seats
    pn = input("Enter PNR to cancel ticket: ")
    found = False
    
    for i in passenger_detail:
        if pn == i[0]:
            found = True
            if i[-2] == True:  # If ticket was confirmed, free up seats
                avail_seats += i[-1]
                booked_seats -= i[-1]
            
            i[-2] = 'NA'
            print("Ticket cancelled successfully")
            break
            
    if not found:
        print('Invalid PNR no.')


def cashier_portal():
    """
    Cashier login and menu
    """
    caid = input("Enter cashier id: ") 
    paswd = input("Enter password: ")
    
    if caid == 'DD' and paswd == '123':
        print("Login successful")
        cashier_menu()
    else:
        print("Invalid ID or Password")


def cashier_menu():
    """
    Cashier menu after successful login
    """
    while True: 
        print("\n--- Cashier Menu ---")
        print("1. View passengers") 
        print("2. Approve ticket") 
        print("3. Cancel ticket")
        print("4. Logout")
        
        try:
            a = int(input("Enter your choice: "))
            
            if a == 1: 
                view_passenger()
            elif a == 2: 
                approve_ticket()
            elif a == 3: 
                cancel_ticket()
            elif a == 4:
                print("Logout successful")
                break
            else:
                print("Invalid option")
        except ValueError:
            print("Please enter a valid number")


def main():
    """
    Main application loop
    """
    print("=== Railway Reservation System ===")
    
    while True:
        print("\n--- Main Menu ---")
        print("1. Passenger")
        print("2. Cashier")
        print("3. Exit")
        
        try:
            choice = int(input("Enter your choice: "))
            
            if choice == 1:
                passenger_portal()
            elif choice == 2:
                cashier_portal()
            elif choice == 3:
                print("Thank you for using Railway Reservation System!")
                break
            else:
                print("Invalid choice")
        except ValueError:
            print("Please enter a valid number")


if __name__ == "__main__":
    main()
