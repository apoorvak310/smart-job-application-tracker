def title():
    print("-"*40)
    print(" "*6+"Smart job application system"+" "*6)
    print("-"*40)

def show_menu():
    print()
    print("1. Add application")
    print("2. View applications")
    print("3. Exit")
    print("4. About\n")
applications = []

def add_application():
    company = input("Enter company name: ")
    role = input("Enter job role: ")
    #status = input("Enter application status: ")
    #print(f"Application for {role} at {company} added successfully!")
    application = Application(company, role)
    print("Status:", application.status)
    applications.append(application)

def states():
    return ["Assessment","HR Round","Withdrawn","Interview", "Offer", "Rejected", "Applied"]

class Application:
    def __init__(self, company, role, status="Applied",job_url=None, work_mode = None, location = None, salary = None, notes = None, interview_date = None, follow_up_date = None, date_applied = None):
        self.company = company
        self.role = role
        self.status = status
        self.job_url = job_url
        self.work_mode = work_mode
        self.location = location
        self.salary = salary
        self.notes = notes
        self.interview_date = interview_date
        self.follow_up_date = follow_up_date
        self.date_applied = date_applied
    def update_status(self,new_status):
        state = states()
        if new_status not in state:
            print(f"Invalid status. Please choose from: {state}")
            return
        else:
            print()
            print(f"Updating status from {self.status} to {new_status}....")
            print()
            print("Updated!")
        self.status = new_status
    def display(self):
        print(f"Company: {self.company}\nRole: {self.role}\nStatus: {self.status}")

def view_applications():
    for app in applications:
        app.display()

def show_about():
    return "Smart Job Application Tracker\nA Python CLI application for managing job applications.\n"

def main():
    title()
    while True:
        show_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            add_application()
        elif choice == "2":
            view_applications()
        elif choice == "3":
            print("Exiting the application")
            break
        elif choice == "4":
            print(show_about())
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()