class Soldier:
    def __init__(self, first_name="", surname="", fathers_name= "", birth_date="", phone_number = "", id_card = "", soldier_id = -1):
        self.first_name = first_name
        self.surname = surname
        self.fathers_name = fathers_name
        self.birth_date = birth_date
        self.phone_number = phone_number
        self.id_card = id_card
        self.soldier_id = soldier_id
        
    #give values     
    def from_dict(self, soldier_dict):
        self.first_name = soldier_dict["first_name"]
        self.surname = soldier_dict["surname"]
        self.fathers_name = soldier_dict["fathers_name"]
        self.birth_date = soldier_dict["birth_date"]
        self.phone_number = soldier_dict["phone_number"]
        self.id_card = soldier_dict["id_card"]
        self.soldier_id = soldier_dict["soldier_id"]
        
    #create a dictionary    
    def to_dict(self):
        soldier_dict = {"first_name": self.first_name,
                        "surname": self.surname,
                        "fathers_name": self.fathers_name,
                        "birth_date": self.birth_date,
                        "phone_number": self.phone_number,
                        "id_card" : self.id_card,
                        "soldier_id":self.soldier_id}
        return soldier_dict
    #print
    def __str__(self):
        string = f"Name        : {self.first_name}".center(5,":")
        string += "\n" + f"Surname     : {self.surname}".center(5,":")
        string += "\n" + f"Fathers_name: {self.fathers_name}".center(5,":")
        string += "\n" + f"Birth_date  : {self.birth_date}".center(5,":")
        string += "\n" + f"Phone_number: {self.phone_number}".center(5,":")
        string += "\n" + f"Id_card     : {self.id_card}".center(5,":")
        string += "\n" + f"Soldier_id  : {self.soldier_id}".center(5,":")
        return string
        
    