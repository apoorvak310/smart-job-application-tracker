from database.schema import create_tables

from models.user import User
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
    VALID_SORT_FIELDS,
    validate_email,
    validate_phone, 
)

from models.application import Application
from services.user_service import save_user, get_users, edit_user, remove_user
from services.skill_service import save_skill, view_skills

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
    print("10. Create User Profile")
    print("11. View User Profiles")
    print("12. Update User Profile")
    print("13. Delete User Profile")
    print("14. Add a Skill")
    print("15. View Your Skills")


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

def create_user_profile():
    name = input("Enter your name: ").strip()
    email = input("Enter your email: ").strip()
    phone = input("Enter your phone: ").strip()
    education = input("Enter your education: ").strip()
    email = validate_email(email)
    if email is None:
        print("Email cannot be empty.")
        return
    elif email is False:
        print("Invalid email address.")
        return
    phone = validate_phone(phone)
    if phone is None:
        print("Phone number cannot be empty.")
        return
    elif phone is False:
        print("Invalid phone number.")
        return
    user = User(name=name, email=email,phone=phone,education=education)
    save_user(user)
    print("User profile created successfully.")

def view_user_profiles():
    users = get_users()
    if len(users) == 0:
        print("No user profiles found.")
        return
    for user in users:
        print("-" * 40)
        #print(f"ID: {user.id}")
        print(f"Name: {user.name}")
        print(f"Email: {user.email}")
        print(f"Phone: {user.phone}")
        print(f"Education: {user.education}")
        print("-" * 40)

def update_user_profile():
    users = get_users()
    if not users:
        print("No user profiles found.")
        return
    print("\n---User Profiles---")
    for user in users:
        print(f"ID: {user.id} | Name : {user.name} | Email: {user.email}")
    try:
        user_id = int(input("Enter ID of the profile to update: "))
    except ValueError:
        print("Please enter a valid numeric ID.")
        return
    user = next((u for u in users if u.id == user_id),None)
    if user is None:
        print("User profile not found.")
        return
    print("Press enter to keep the existing value.")
    name = input(f"Name [{user.name}]: ").strip()
    email = input(f"Email [{user.email}]: ").strip()
    phone = input(f"Phone [{user.phone}]: ").strip()
    education = input(f"Education [{user.education}]: ").strip()

    user.name = name or user.name
    email = email or user.email
    phone = phone or user.phone
    education = education or user.education

    email = validate_email(email)
    if email is None:
        print("Email cannot be empty.")
        return
    elif email is False:
        print("Invalid email address.")
        return

    phone = validate_phone(phone)
    if phone is None:
        print("Phone number cannot be empty.")
        return
    elif phone is False:
        print("Invalid phone number.")
        return

    user.email = email
    user.phone = phone
    user.education = education

    try:
        updated = edit_user(user)
    except Exception as error:
        print(f"Could not update profile: {error}")
        return

    if updated:
        print("User profile updated successfully.")
    else:
        print("No profile was updated.")

def delete_user_profile():
    users = get_users()
    if len(users) == 0:
        print("No user profiles found.")
        return
    for user in users:
        print(f"ID: {user.id} | Name : {user.name} | Email: {user.email}")
    try:
        user_id = int(input("Enter the user's ID to delete: "))
    except ValueError:
        print("Enter a valid ID")
        return
    
    if any(user.id == user_id for user in users):
        yes = input(
            "Confirm deleting the user. Once deleted you cannot get it back. (y/n) "
        ).strip().lower()

        if yes == "y":
            confirm = remove_user(user_id)
            if confirm:
                print("User profile deleted successfully.")
            else:
                print("Could not delete user profile.")
        else:
            print("Deletion cancelled.")
    else:
        print("The user profile does not exist.")

def add_skills_to_profile():
    users = get_users()
    if len(users) == 0:
        print("No users found.")
        return
    for user in users:
        print(f"ID: {user.id} | Name: {user.name}")
    try:
        user_id = int(input("Enter the user's id to add the skill: "))
    except ValueError:
        print("Enter a valid ID.")
        return
    if any(user.id == user_id for user in users):
        skill = input("Enter the skill: ").strip()
        if not skill:
            print("Enter a valid skill.")
            return
        success = save_skill(user_id,skill)
        if success:
            print(f"'{skill}' added successfully.")
        else:
            print(f"'{skill}' already exists in this profile.")
    else:
        print(f"No user with{user_id}exists")
        return

def view_user_skills():
    users = get_users()
    if len(users) == 0:
        print("No user found.")
        return
    for user in users:
        print(f"ID: {user.id} | Name: {user.name}")
    try:
        user_id = int(input("Enter the user's id to View the skills: "))
    except ValueError:
        print("Enter a valid ID.")
        return
    if any(user.id == user_id for user in users):
        print("\nSkills:\n")
        skills = view_skills(user_id)
        if len(skills) == 0:
            print("No skills added to this profile yet.")
        for skill in skills:
            print(skill[2])
    else:
        print("No user with this ID exists.")

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
        elif choice == "10":
            create_user_profile()
        elif choice == "11":
            view_user_profiles()
        elif choice == "12":
            update_user_profile()
        elif choice == "13":
            delete_user_profile()
        elif choice == "14":
            add_skills_to_profile()
        elif choice == "15":
            view_user_skills()
        else:
            print("Invalid choice. Enter between 1-15.")


if __name__ == "__main__":
    main()