class Officer:
    def __init__(self, first_name="", surname="", birth_date="", phone_number = "", officer_id=-1):
        self.first_name = first_name
        self.surname = surname
        self.birth_date = birth_date
        self.phone_number = phone_number
        self.officer_id = officer_id
    #give values   
    def from_dict(self, officer_dict):
        self.first_name = officer_dict["first_name"]
        self.surname = officer_dict["surname"]
        self.birth_date = officer_dict["birth_date"]
        self.phone_number = officer_dict["phone_number"]
        self.officer_id = officer_dict["officer_id"]
    #create a dictionary
    def to_dict(self):
        officer_dict = {"first_name": self.first_name,
                        "surname": self.surname,
                        "birth_date": self.birth_date,
                        "birth_date": self.birth_date,
                        "phone_number": self.phone_number,
                        "officer_id":self.officer_id}
        return officer_dict
    #print
    def __str__(self):
        string = f"Name        : {self.first_name}".center(5,":")
        string += "\n" + f"Surname     : {self.surname}".center(5,":")
        string += "\n" + f"Birth_date  : {self.birth_date}".center(5,":")
        string += "\n" + f"Phone_number: {self.phone_number}".center(5,":")
        string += "\n" + f"Officer_id  : {self.officer_id}".center(5,":")
        return string