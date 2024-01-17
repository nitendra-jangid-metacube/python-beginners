class Patient:
    def __init__(self, id, name, ssn):
        self.__id = id
        self.__name = name
        self.__ssn = ssn

    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_ssn(self):
        return self.__ssn

    def set_ssn(self, ssn):
        self.__ssn = ssn

# Create an object of class Patient
patient1 = Patient(12345, "Nitendra", "123-45-6789")

# Access the fields using getter methods
print("Patient ID:", patient1.get_id())
print("Patient Name:", patient1.get_name())
print("Patient SSN:", patient1.get_ssn())

# Modify the fields using setter methods
patient1.set_id(11111)
patient1.set_name("Nitendra Jangid")
patient1.set_ssn("987-65-4321")

# Access the modified fields using getter methods
print("Modified Patient ID:", patient1.get_id())
print("Modified Patient Name:", patient1.get_name())
print("Modified Patient SSN:", patient1.get_ssn())
