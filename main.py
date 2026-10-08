from database.schema import create_tables

from services.application_service import (
    save_application,
    get_applications,
    update_status,
    delete_application_by_id,
    search,
    filter_status,
    sort_applications_service
)

from util.validators import (
    validate_required,
    validate_date,
    validate_salary,
    validate_work_mode,
    validate_job_url,
    validate_location,
    validate_notes,
    VALID_SORT_FIELDS
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
    print("5. Delete Application")
    print("6. About")
    print("7. Search applications")
    print("8. Filter applications by status")
    print("9. Sort applications")


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

    interview_date = input(
        "Enter interview date (ignore if not known, YYYY-MM-DD): "
    ).strip()

    valid_interview = validate_date(interview_date)

    if valid_interview is False:
        print("Enter a valid date.")
        return

    follow_up_date = input(
        "Enter the follow-up date (ignore if not known, YYYY-MM-DD): "
    ).strip()

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

    # Save application through service layer
    save_application(application)

    print("Application saved successfully.")
    print("Application ID:", application.id)


def view_applications():
    # Get applications through service layer
    applications = get_applications()

    if len(applications) == 0:
        print("No applications found.")
        return

    print(f"\nTotal Applications: {len(applications)}")

    for application in applications:
        application.display()


def update_application_status():
    applications = get_applications()

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

    # Update through service layer
    success = update_status(application_id, new_status)

    if success:
        print(f"Status updated to {new_status}")
    else:
        print("Invalid status or application ID not found.")


def delete_application_cli():
    applications = get_applications()

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

    application_id = input(
        "\nEnter application ID to delete: "
    ).strip()

    if not application_id.isdigit():
        print("Invalid application ID.")
        return

    application_id = int(application_id)

    success = delete_application_by_id(application_id)

    if success:
        print("Application deleted successfully.")
    else:
        print("Application ID not found.")

def search_applications_cli():
    search_term = input("Enter search term: ").strip()
    applications = search(search_term)
    if len(applications) == 0:
        print("No applications found.")
    else:
        print(f"Search results for '{search_term}':")
        for application in applications:
            application.display()

def filter_applications_cli():
    status = input("Enter status to filter by: ").strip()
    applications = filter_status(status)
    if len(applications) == 0:
        print(f"No applications found with status '{status}'.")
    else:
        print(f"Applications with status '{status}':")
        for application in applications:
            application.display()

def sort_applications_cli():
    
    sort_by = input(
        "Enter field to sort by (company, role, date, salary): ").strip().lower()
    if sort_by not in VALID_SORT_FIELDS:
        print("Invalid sort field. Please choose from company, role, date, or salary.")
        return
    descending_input = input(
        "Order (Type Asc/Desc): ").strip().lower()
    if descending_input == "desc":
        descending = True
    elif descending_input == "asc":
        descending = False
    else:
        print("Invalid order. Please enter 'asc' or 'desc'.")
        return
    order = "descending" if descending else "ascending"
    applications = sort_applications_service(sort_by, descending)
    if len(applications) == 0:
        print("No applications found.")
    else:
        print(f"Applications sorted by '{sort_by}' ({order}):")
        for application in applications:
            application.display()

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
            delete_application_cli()

        elif choice == "6":
            print(show_about())

        elif choice == "7":
            search_applications_cli()
        elif choice == "8":
            filter_applications_cli()
        elif choice == "9":
            sort_applications_cli()
        else:
            print("Invalid choice. Enter between 1-9.")


if __name__ == "__main__":
    main()