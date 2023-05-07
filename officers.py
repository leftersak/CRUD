import json
from officer import Officer



class Officers:
    def __init__(self):
        try:
            with open("officers.json", "r") as f:
                officers_list = json.load(f)

            self.officers = []
            for officer_dict in officers_list:
                t = Officer()
                t.from_dict(officer_dict)
                self.officers += [t]
        except FileNotFoundError:
            self.officers = []
    #saves the changes in a json file
    def save_officers_data(self):
        list_to_write = []
        for officer in self.officers:
            list_to_write += [officer.to_dict()]

        with open("officers.json", "w") as f:
            json.dump(list_to_write, f)
    #checks if the input is an integer    
    def is_digit(self):
        officer_id = input("Give id: ")
        while not(officer_id.isdigit()):
            officer_id = input("Give an integer id: ")
        return officer_id
    #calculates next officer_id
    def next_id(self):
        if not self.officers:
            return 1001
        else:
            ids = []
            for t in self.officers:
                ids.append(t.officer_id)
            return max(ids) + 1
    #creation of an officer
    def create_officer(self,first_name, surname, birth_date, phone_number):
        for officer in self.officers:
            if officer.first_name == first_name and officer.surname == surname:#checks if this first-name and surname already exists
                print("Error. officer already exists with the current information! ")
                print(officer)
                return None

        t = Officer(first_name, surname, birth_date, phone_number, self.next_id())
        self.officers.append(t)
        return t
    #print
    def read_officer(self, officer_id, surname):
        for officer in self.officers:
            if int(officer_id) == officer.officer_id or surname == officer.surname:
                print(officer)
                print("=" * 40)
                return 
        else:
            print("False input!")
            return None
    #update
    def update_officer(self, officer_id, surname):
        for officer in self.officers:
            if int(officer_id) == officer.officer_id or surname == officer.surname:
                print(officer)
                choice = int(input("Update 1-name, 2-surname: , 3 birth-date:c, 4-telephone: "))
                if choice == 1:
                    officer.first_name = input("Give new name: ").capitalize()
                elif choice == 2:
                    officer.surname = input("Give new surname: ").capitalize()
                elif choice == 3:
                    officer.birth_date = input("Give new birth-date: ")
                elif choice == 4:
                    officer.phone_number = input("Give new telephone: ")    
                return
        else:
            print("Error!Your inputs don't not exist!")
    #delete
    def delete_officer(self, officer_id, officer_surname):
        for i in range(len(self.officers)):
            if int(officer_id) == self.officers[i].officer_id or officer_surname == self.officers[i].surname:
                self.officers.pop(i)
                return
        else:
            print("No officer with this id!")