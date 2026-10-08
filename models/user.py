class User:
    def __init__(self,name,email,phone,education):
        self.name = name
        self.email = email
        self.phone = phone
        self.education = education
    def display(self):
        print("-" * 40)
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"Phone: {self.phone}")
        print(f"Education: {self.education}")
        print("-" * 40)
    