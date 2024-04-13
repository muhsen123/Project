import random
import string

# Set to store unique booking references
booking_references = set()

def generate_booking_reference():
    """Generates a unique 8-character alphanumeric booking reference."""
    while True:
        reference = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
        if reference not in booking_references:
            booking_references.add(reference)
            return reference
        

# seats = {
#     # Passenger seats ( 'F' for free seats initially)
#     **{f"{row}{col}": 'F' for row in range(1, 81) for col in ['A', 'B', 'C', 'D', 'E', 'F']},
#     # Aisle seats ( 'X' for all aisles)
#     **{f"{row}X": 'X' for row in range(1, 81)},
#     # Storage spaces ( 'S' for all storage)
#     **{f"{row}S": 'S' for row in range(1, 81)}
# }

seats = {
    seat: {'status': 'F', 'reference': None, 'customer': None}
    for seat in ['{}{}'.format(row, col) for row in range(1, 81) for col in ['A', 'B', 'C', 'D', 'E', 'F']]
}

# Update certain rows for storage (S) according to the given pattern
for storage_row in [79, 80]:
    for col in ['D', 'E', 'F']:
        seats[f"{storage_row}{col}"] = 'S'


def check_availability(seat):
    """Check if the specified seat is available for booking."""
    # Check if the seat exists in the layout and if it is free (F)
    if seat in seats and seats[seat] == 'F':
        print(f"Seat {seat} is available.")
        return True
    elif seat in seats:
        print(f"Seat {seat} is not available for booking.")
        return False
    else:
        print(f"Seat {seat} does not exist in the aircraft layout.")
        return False

# Function to book a seat with customer details
def book_seat(seat, customer_details):
    """Books a seat with provided customer details."""
    if seat in seats and seats[seat]['status'] == 'F':
        reference = generate_booking_reference()
        seats[seat]['status'] = 'R'
        seats[seat]['reference'] = reference
        seats[seat]['customer'] = customer_details
        print(f"Seat {seat} booked with reference {reference}.")
    else:
        print(f"Seat {seat} is not available or does not exist.")

# Function to free a booked seat
def free_seat(seat):
    """Frees up a seat and clears the associated booking details."""
    if seat in seats and seats[seat]['status'] == 'R':
        seats[seat]['status'] = 'F'
        print(f"Booking {seats[seat]['reference']} for seat {seat} cancelled.")
        seats[seat]['reference'] = None
        seats[seat]['customer'] = None
    else:
        print(f"Seat {seat} is not booked or does not exist.")
  # Function to check seat availability, updated to work with the new data structure
def check_availability(seat):
    """Check if the specified seat is available for booking."""
    if seat in seats and seats[seat]['status'] == 'F':
        print(f"Seat {seat} is available.")
        return True
    elif seat in seats:
        print(f"Seat {seat} is not available for booking.")
        return False
    else:
        print(f"Seat {seat} does not exist in the aircraft layout.")
        return False

# Function to display the booking state of all seats
def show_booking_state():
    """Display the booking state of all the seats in the aircraft."""
    for seat, info in seats.items():
        if info['status'] != 'X' and info['status'] != 'S':
            print(f"Seat {seat}: {'Booked' if info['status'] == 'R' else 'Available'}")

# Main menu function, updated to include a prompt for customer details
def main_menu():
    """Provide a command-line menu interface for the seat booking application."""
    while True:
        print("\nMenu:")
        print("1. Check Seat Availability")
        print("2. Book a Seat")
        print("3. Free a Seat")
        print("4. Show Booking State")
        print("5. Exit")
        choice = input("Enter option: ")

        if choice == '1':
            seat = input("Enter seat number to check (e.g., 1A): ").upper()
            check_availability(seat)
        elif choice == '2':
            seat = input("Enter seat number to book (e.g., 1A): ").upper()
            if check_availability(seat):
                # Simulate capturing customer details
                customer_details = {
                    'passport_number': input("Enter passport number: "),
                    'first_name': input("Enter first name: "),
                    'last_name': input("Enter last name: ")
                }
                book_seat(seat, customer_details)
        elif choice == '3':
            seat = input("Enter seat number to free up (e.g., 1A): ").upper()
            free_seat(seat)
        elif choice == '4':
            show_booking_state()
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid option. Please try again.")

main_menu()

