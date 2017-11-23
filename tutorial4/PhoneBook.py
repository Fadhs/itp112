class PhoneBook():
    def __init__(self):
        self.contact_details = {}

    def add_contact(self, name, number):
        self.contact_details[name] = number

    def remove_contact(self, name):
        if name in self.contact_details:
            del self.contact_details[name]
        else:
            print("Contact not available")

    def get_contact_number(self, name):
        if name in self.contact_details:
            return self.contact_details.get(name, None)
        else:
            print("Contact not available")
