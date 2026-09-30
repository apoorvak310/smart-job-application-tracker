from database.schema import create_tables
from repositories.application_repository import (
    add_application as save_application,
    get_all_applications, update_application_status as update_status_in_db
)
from util.validators import (
    validate_required,
    validate_date,
    validate_salary,
    validate_work_mode,
    validate_job_url,
    validate_location,
    validate_notes,
    validate_status
)
from models.application import Application
def title():
    print("-" * 40)
    print(" " * 6 + "Smart Job Application System" + " " * 6)
    print("-" * 40)

def show_menu():
    print()
    print("1. Add Application")
    print("2. View Applications")
    print("3. Update Application Status")
    print("4. Exit")
    print("5. About\n")

def add_application():
    company = input("Enter company name: ").strip()
    if not validate_required(company):
        print("Company cannot be empty. Please try again.")
        return
    role = input("Enter job role: ").strip()
    if not validate_required(role):
        print("Role cannot be empty. Please try again.")
        return
    date_applied = input("Enter date applied (YYYY-MM-DD): ")
    validated_date = validate_date(date_applied)
    if validated_date is False:
        print("Invalid date format. Please use YYYY-MM-DD.")
        return
    salary = input("Enter expected salary: ").strip()
    validated_salary = validate_salary(salary)
    if validated_salary is None:
        print("Invalid salary. Please enter a positive number.")
        return
    work_mode = input("Enter the work mode: ").strip()
    work = validate_work_mode(work_mode)
    if work is None:
        print("Invalid work mode. Please try again.")
        return
    job_url = input("Enter the Job URL (optional): ")
    validated_job_url = validate_job_url(job_url)
    if validated_job_url is False:
        print("Invalid URL. Please enter a valid HTTP/HTTPS URL.")
        return
    location = input("Enter job location (optional): ")
    validated_location = validate_location(location)
    interview_date = input("Enter interview date (ignore if not known, YYYY-MM-DD): ").strip()
    valid_interview = validate_date(interview_date)
    if valid_interview is False:
        print("Enter a valid date.")
        return
    follow_up_date = input("Enter the follow-up date (ignore if not known, YYYY-MM-DD): ").strip()
    valid_follow_up = validate_date(follow_up_date)
    if valid_follow_up is False:
        print("Enter a valid follow-up date.")
        return
    notes = input("Enter notes (optional): ")
    validated_notes = validate_notes(notes)

    # Create Application object
    application = Application(
        company=company,
        role=role,
        date_applied=validated_date,
        interview_date=valid_interview,
        salary=validated_salary,
        work_mode=work,
        job_url=validated_job_url,
        location=validated_location,
        notes=validated_notes,
        follow_up_date=valid_follow_up
    )
    print("Status:", application.status)
    # Save application to SQLite
    save_application(application)
    print("Application saved successfully.")
    print("Application ID:", application.id)

def view_applications():
    # Get applications from SQLite
    applications = get_all_applications()
    if len(applications) == 0:
        print("No applications found.")
        return
    print(f"\nTotal Applications: {len(applications)}")
    for application in applications:
        application.display()

def update_application_status():
    applications = get_all_applications()

    if len(applications) == 0:
        print("No applications found.")
        return

    print("\nApplications:")

    for application in applications:
        print(
            f"ID: {application.id} | "
            f"Company: {application.company} | "
            f"Role: {application.role} | "
            f"Status: {application.status}"
        )

    application_id = input("\nEnter application ID: ").strip()

    if not application_id.isdigit():
        print("Invalid application ID.")
        return

    application_id = int(application_id)

    new_status = input("Enter new status: ").strip()

    updated_status = validate_status(new_status)

    if updated_status is None:
        print("Invalid status.")
        return

    success = update_status_in_db(application_id, updated_status)

    if success:
        print(f"Status updated to {updated_status}")
    else:
        print("Application ID not found.")

def show_about():
    return (
        "Smart Job Application Tracker\n"
        "A Python CLI application for managing job applications.\n"
    )
def main():
    # Make sure database tables exist
    create_tables()
    title()
    while True:
        show_menu()
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            add_application()
        elif choice == "2":
            view_applications()
        elif choice == "3":
            update_application_status()
        elif choice == "4":
            print("Exiting the application.")
            break
        elif choice == "5":
            print(show_about())
        else:
            print("Invalid choice. Enter between 1-5.")

if __name__ == "__main__":
    main()