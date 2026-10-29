class Patient:
    def __init__(self, name, bill_amount):
        self.__name = name
        self.__bill_amount = bill_amount

    def get_name(self):
        return self.__name

    def get_bill_amount(self):
        return self.__bill_amount

    def set_name(self, name):
        self.__name = name

    def set_bill_amount(self, bill_amount):
        self.__bill_amount = bill_amount

    def calculate_bill(self):
        return self.__bill_amount


class Senior_Patient(Patient):
    def __init__(self, name, bill_amount):
        super().__init__(name, bill_amount)

    def calculate_bill(self):
        return self.get_bill_amount() * 0.80


class PhilHealth_Patient(Patient):
    def __init__(self, name, bill_amount):
        super().__init__(name, bill_amount)

    def calculate_bill(self):
        return self.get_bill_amount() * 0.85


patient1 = Patient("Myke", 15000)
patient2 = Senior_Patient("Kaiza", 15000)
patient3 = PhilHealth_Patient("Prince", 15000)

print("Hospital Billing System\n")

patients = [patient1, patient2, patient3]

for patient in patients:
    print("Patient Name:", patient.get_name())
    print("Original Bill: ₱{:,.2f}".format(
        patient.get_bill_amount()))
    print("Final Bill: ₱{:,.2f}".format(
        patient.calculate_bill()))
    print()
