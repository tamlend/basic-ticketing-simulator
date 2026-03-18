# Basic Ticketing Simulator - SOC Portfolio Project

class Ticket:
    def __init__(self, tid, title, severity, assignee="Unassigned"):
        self.tid = tid
        self.title = title
        self.severity = severity
        self.status = "Open"
        self.assignee = assignee
        self.notes = []

tickets = []

def create_ticket():
    print("\n[Type 'back' at any step to return to main menu without creating ticket]")
    
    title = input("\nEnter alert description (e.g. 'Brute force from 10.0.0.5'): ").strip()
    if title.lower() in ['back']:
        print("Ticket creation cancelled. Back to menu.\n")
        return
    
    while True:
        sev_input = input("Severity (Low / Med / High / Critical): ").strip().capitalize()
        if sev_input.lower() in ['back']:
            print("Ticket creation cancelled. Back to menu.\n")
            return
        
        valid_severities = ["Low", "Med", "High", "Critical"]
        if sev_input in valid_severities:
            severity = sev_input
            break
        else:
            print("Invalid severity. Please use Low, Med, High, or Critical.\n")
    
    tid = len(tickets) + 1001
    t = Ticket(tid, title, severity)
    tickets.append(t)
    print(f"Ticket #{tid} CREATED | Severity: {severity} | Status: Open\n")

def list_tickets():
    if not tickets:
        print("No tickets yet!\n")
        return
    print("\n ALL TICKETS:")
    for t in tickets:
        note_info = f" | {len(t.notes)} note(s)" if t.notes else ""
        print(f"#{t.tid} | {t.severity} | {t.status} | {t.assignee} | {t.title}{note_info}")

def assign_ticket():
    tid = int(input("\n Enter Ticket ID to assign (e.g. 1001): "))
    assignee = input("Who are you assigning? (your name or 'SOC Analyst 1'): ")
    for t in tickets:
        if t.tid == tid:
            t.assignee = assignee
            print(f"Ticket #{tid} assigned to {assignee} \n")
            return
    print("Ticket not found\n")

def close_ticket():
    tid = int(input("\n Enter Ticket ID to close: "))
    for t in tickets:
        if t.tid == tid:
            t.status = "Closed"
            note = input("Quick resolution note: ")
            t.notes.append(note)
            print(f"Ticket #{tid} CLOSED!\n")
            return
    print("Ticket not found\n")

def view_ticket_details():
    if not tickets:
        print("No tickets to view!\n")
        return
    try:
        tid = int(input("\n Enter Ticket ID to view details (e.g. 1001): "))
        for t in tickets:
            if t.tid == tid:
                print(f"\n TICKET #{t.tid} DETAILS")
                print(f"Title: {t.title}")
                print(f"Severity: {t.severity}")
                print(f"Status: {t.status}")
                print(f"Assignee: {t.assignee}")
                print("\n Notes:")
                if t.notes:
                    for i, note in enumerate(t.notes, 1):
                        print(f"  {i}. {note}")
                else:
                    print("  No notes added yet.")
                print("")
                return
        print("Ticket not found\n")
    except ValueError:
        print("Please enter a valid number\n")

def show_menu():
    while True:
        print("\n" + "="*50)
        print("SOC Ticketing Simulator")
        print("="*50)
        print("1. Create new SIEM alert ticket")
        print("2. List all tickets")
        print("3. Assign ticket")
        print("4. Close ticket + add note")
        print("5. View ticket details (incl. notes)")
        print("6. Exit")
        choice = input("\nChoose 1-6: ")
        
        if choice == "1": create_ticket()
        elif choice == "2": list_tickets()
        elif choice == "3": assign_ticket()
        elif choice == "4": close_ticket()
        elif choice == "5": view_ticket_details()
        elif choice == "6":
            print("Simulator saved.")
            break
        else:
            print("Must type 1-6")

# Auto start the simulator
if __name__ == "__main__":
    print("Welcome to my first portfolio project! Let's simulate a real SOC shift.")
    show_menu()