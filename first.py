print("naglaa") 
class Ticket:
    def __init__(self):
        self.tickets =[]
    def __init__(self, number, creator, staff_id, email, description, response=None, status="Open"):
    
        # Initializes a Ticket with a unique number, description,staff_id, email, response AND status(default is open)
        self.number = number
        self.creator = creator
        self.staff_id = staff_id
        self.email = email
        self.description = description
        self.response = response
        self.status = status  

        while True:
            print("Options:")
            print("1. Create a new Ticket")
            print("2. Display ticket statistics")
            print("3. open ticket")
            print("4 .ticket statistics")
            print("5. Exit")

            choice = input("Select an option 1, 2,3,4, 5 \n")

            if choice == "1":
                number= input("Enter ticket number:")
                creator = input(" Enter ticket creator name:")
                staff_id = input("Enter staff ID:")
                email= input("Enter email:")
                description= input("Enter description:")
                new_ticket = Ticket(number, creator,staff_id, email, description )
                self.tickets.append(new_ticket)
                print("Ticket created successfully \n")
            
            elif choice == "5":
                print("Exit the code")
                break
            else:
                print("Please select a valid option")
                  
class TicketingSystem:
    def __init__(self):
        # Initialize an empty list to store tickets.
        self.tickets = []
        self.created_tickets = 0
        self.open_tickets = 0
        self.resolved_tickets = 0

    def create_ticket(self, creator, email, description):
        ticket_number = len(self.tickets) +1
        ticket = Ticket(ticket_number, creator, f"JOHNA", email, description,)
        self.tickets.append(ticket)
        self.created_tickets +=1
        self.open_tickets +=1

       # Check if the description contains "Password Change" to generate a new password
        if "Password Change" in description:
            self.reset_password("staff_id", creator)

    def solve_ticket(self, ticket_number, response):
        # Resolve a ticket by changing its status to 'Resolved'.
        for ticket in self.tickets:
            if ticket.number == ticket_number and ticket.status == "Open":
                ticket.status = "Resolved"
                ticket.response = response
                self.open_tickets -= 1
                self.resolved_tickets += 1
                break
        else:
            print("Ticket not found or already resolved.")

    def get_statistics(self):
        print(f"Tickets created: {self.created_tickets}")
        print(f"Tickets to solve: {self.open_tickets}")
        print(f"Tickets resolved: {self.resolved_tickets}")

    def display_tickets(self):
        for ticket in self.tickets:
            print(f"Staff ID: {ticket.staff_id}")
            print(f"Ticket Number: {ticket.number}")
            print(f"Ticket Creator: {ticket.creator}")
            print(f"Email Address: {ticket.email}")
            print(f"Description: {ticket.description}")
            print(f"Response: {ticket.response}")
            print(f"Status: {ticket.status}")


            print()
    def reset_password(self, staff_id, ticket_creator_name):
        # Extract the first two characters of staff ID and the first three characters of ticket creator name
         new_password = staff_id[:2] + ''.join(ticket_creator_name.split()[:3])
         print("New password:", new_password)

# Usage example
ticket_system = TicketingSystem()

# Creating tickets
ticket_system.create_ticket("John", "johndoe@example.com", "Network issue")
ticket_system.create_ticket("Jane" , "janesmith@example.com", "password change requested")
ticket_system.create_ticket("Alice", "alicejohnson@example.com", "My monitor stopped working")

# Solving a ticket
ticket_system.solve_ticket( 1,"Issue resolved by rebooting router.")
ticket_system.solve_ticket(2, "New password generated JAjoh.")


# Displaying tickets and statistics
# display all tickets in the system.
ticket_system.display_tickets()
ticket_system.get_statistics()



