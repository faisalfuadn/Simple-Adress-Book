import csv
import os
import re
from tabulate import tabulate

CONTACT_FILE = "Contact.csv"


class ContactManager:
    def __init__(self):
        self.contacts = []
        self.load_contacts()

    # ===== FILE HANDLING =====
    def load_contacts(self):
        try:
            if not os.path.exists(CONTACT_FILE):
                with open(CONTACT_FILE, "w", newline="") as f:
                    writer = csv.DictWriter(f, fieldnames=["Name", "Phone", "Email", "Address"])
                    writer.writeheader()
            with open(CONTACT_FILE, newline="") as f:
                reader = csv.DictReader(f)
                self.contacts = list(reader)
        except Exception as e:
            print(f"⚠️ Error loading contacts: {e}")

    def save_contacts(self):
        try:
            with open(CONTACT_FILE, "w", newline="") as f:
                writer = csv.DictWriter(f, fieldnames=["Name", "Phone", "Email", "Address"])
                writer.writeheader()
                writer.writerows(self.contacts)
        except Exception as e:
            print(f"⚠️ Error saving contacts: {e}")

    # ===== VALIDATION =====
    @staticmethod
    def is_valid_email(email):
        if not email.strip():
            return True  # allow empty email
        pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        return bool(re.match(pattern, email.strip()))

    @staticmethod
    def is_valid_phone(phone):
        if not phone.strip():
            return True  # allow empty phone
        pattern = r"^\+?\d{7,15}$"  # basic numeric or +countrycode
        return bool(re.match(pattern, phone.strip()))

    # ===== CORE METHODS =====
    def add_contact(self, name, phone, email, address):
        name = name.strip()
        if not name:
            print("❌ Name cannot be empty.")
            return
        # prevent duplicates (case-insensitive)
        if any(c["Name"].lower() == name.lower() for c in self.contacts):
            print("⚠️ Contact already exists.")
            return
        if not self.is_valid_phone(phone):
            print("❌ Invalid phone number format.")
            return
        if not self.is_valid_email(email):
            print("❌ Invalid email format.")
            return

        self.contacts.append({
            "Name": name.title(),
            "Phone": phone.strip() or "empty",
            "Email": email.strip() or "empty",
            "Address": address.strip() or "empty",
        })
        self.save_contacts()
        print("✅ Contact added successfully!")

    def list_contacts(self):
        if not self.contacts:
            print("No contacts found.")
            return
        print(tabulate(self.contacts, headers="keys", tablefmt="grid"))

    def search_contact(self, key, value):
        value = value.strip().lower()
        found = [c for c in self.contacts if value in c[key].lower()]
        if found:
            print(tabulate(found, headers="keys", tablefmt="grid"))
        else:
            print("❌ No matching contacts found.")

    def edit_contact(self, name, field, new_value):
        name = name.strip().lower()
        for c in self.contacts:
            if c["Name"].lower() == name:
                # validation depending on field
                if field == "Phone" and not self.is_valid_phone(new_value):
                    print("❌ Invalid phone number format.")
                    return
                if field == "Email" and not self.is_valid_email(new_value):
                    print("❌ Invalid email format.")
                    return
                c[field] = new_value.strip().title() if field == "Name" else new_value.strip()
                self.save_contacts()
                print(f"✅ {field} updated successfully!")
                return
        print("❌ Contact not found.")

    def delete_contact(self, name):
        name = name.strip().lower()
        for c in self.contacts:
            if c["Name"].lower() == name:
                self.contacts.remove(c)
                self.save_contacts()
                print("✅ Contact deleted.")
                return
        print("❌ Contact not found.")

    def reset_contacts(self):
        """Erase all contacts (confirmation handled in UI)."""
        self.contacts.clear()
        self.save_contacts()
        print("✅ All contacts have been erased.")


# ===== UI LOOP =====
def main():
    cm = ContactManager()
    print("\n=== Welcome to Contact Management System ===\n")

    menu = """
    [1] Add Contact
    [2] List Contacts
    [3] Search Contact
    [4] Edit Contact
    [5] Delete Contact
    [6] Reset All
    [0] Exit
    """

    while True:
        print(menu)
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            name = input("Name: ")
            phone = input("Phone: ")
            email = input("Email: ")
            address = input("Address: ")
            cm.add_contact(name, phone, email, address)

        elif choice == "2":
            cm.list_contacts()

        elif choice == "3":
            print("[1] Search by Name\n[2] Search by Phone")
            opt = input("Choose option: ")
            if opt == "1":
                value = input("Enter part of Name: ")
                cm.search_contact("Name", value)
            elif opt == "2":
                value = input("Enter part of Phone: ")
                cm.search_contact("Phone", value)
            else:
                print("Invalid choice.")

        elif choice == "4":
            name = input("Enter contact name to edit: ")
            print("[1] Name\n[2] Phone\n[3] Email\n[4] Address")
            field_choice = input("Choose field: ")
            field_map = {"1": "Name", "2": "Phone", "3": "Email", "4": "Address"}
            if field_choice in field_map:
                new_value = input(f"Enter new {field_map[field_choice]}: ")
                cm.edit_contact(name, field_map[field_choice], new_value)
            else:
                print("Invalid field choice.")

        elif choice == "5":
            name = input("Enter Name to delete: ")
            cm.delete_contact(name)

        elif choice == "6":
            confirm = input("⚠️  Are you sure you want to delete ALL contacts? (y/n): ")
            if confirm.lower() == "y":
                cm.reset_contacts()
            else:
                print("Reset cancelled.")

        elif choice == "0":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.")


if __name__ == "__main__":
    main()
