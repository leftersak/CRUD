from soldier import Soldier
import json



# functions
class Soldiers:
    def __init__(self):
        try:
            with open("soldiers.json", "r") as f:
                soldiers_list = json.load(f) 
                
            self.soldiers = []
            for soldier_dict in soldiers_list:
                s = Soldier()
                s.from_dict(soldier_dict)
                self.soldiers += [s]    
        except FileNotFoundError:
            self.soldiers = []       


    def save_soldiers_data(self):
        list_to_write = []
        for soldier in self.soldiers:
            list_to_write += [soldier.to_dict()]

        with open("soldiers.json", "w") as f:
            json.dump(list_to_write, f)


    def __str__(self):
        str = ""
        for soldier in self.soldiers:
            str += str(soldier)
        return str
    
    #checks if the input is integer        
    def is_digit(self):
        soldier_id = input("Give id: ")
        while not(soldier_id.isdigit()):
            soldier_id = input("Give an integer id: ")
        return soldier_id
    #calculates next sodier_id
    def next_id(self):
        if not self.soldiers:
            return 1001
        else:
            ids = []
            for s in self.soldiers:
                ids.append(s.soldier_id)
            return max(ids) + 1
    #creation of a soldier
    def create_soldier(self):
        first_name = input("Give name: ").capitalize()
        surname = input("Give surname: ").capitalize()
        fathers_name = input("Give father's name: ").capitalize()

        for s in self.soldiers:
            if first_name == s.first_name and surname == s.surname and fathers_name == s.fathers_name:
                print("This soldier already exists.")
                ch = input("Do you want to continue? (y-yes, n-no): ")
                if ch == "n":
                    return None

        birth_date = input("Give birth date: ")
        phone_number = int(input("Give phone_number: "))
        id_card = input("Does he/she has an id card: (y-true, n-false): ")
        if id_card == "y":
            id_number = input("Give id card number: ")
        else:
            id_number = None
            
        soldier = Soldier(first_name, surname, fathers_name, birth_date, phone_number, id_number, self.next_id())
        
        self.soldiers.append(soldier)
       
        return soldier

    #search for a soldier with a given id
    def search_soldier_by_id(self, soldier_id):
        for soldier in self.soldiers:
            if int(soldier_id) == soldier.soldier_id:
                return soldier
        return None
    
    def print_soldiers(self):
        i = 0
        for soldier in self.soldiers:
            i += 1
            print(f"{i}.")
            print(soldier)
        

    #prints first name, first letter of fathers name and last name
    def print_soldiers_names(self):
        for soldier in self.soldiers:
            print(f"{soldier.first_name} {soldier.fathers_name[0]}. {soldier.surname}")

    #search for a soldier with a given surname
    def search_soldier_by_surname(self, surname):
        match_soldiers = []
        for soldier in self.soldiers:
            if surname == soldier.surname:
                match_soldiers.append(soldier)
        return match_soldiers

    #update
    def soldier_update(self, soldier):
        print(soldier)
        print("=" * 15)
        print("1-first name")
        print("2-surname")
        print("3-father's name")
        print("4-birth date")
        print("5-phone number")
        print("6-id card")
        print("=" * 15)
        update_choice = int(input("Pick something to update: "))
        if update_choice == 1:
            soldier.first_name = input("Give new first name: ").capitalize()
        elif update_choice == 2:
            soldier.surname = input("Give new surname: ").capitalize()
        elif update_choice == 3:
            soldier.fathers_name = input("Give new father's name: ").capitalize()
        elif update_choice == 4:
            soldier.birth_date = input("Give new birth date: ")
        elif update_choice == 5:
            soldier.phone_number = input("Give new phone number: ")
        elif update_choice == 6:
            soldier.id_card = input("Give new id card: ")

        print("=" * 15)
        print(soldier)
        print("Soldier updated! ")

    #delete a soldier with a given soldier id
    def delete_soldier_by_id(self, soldier_id):
        for i in range(len(self.soldiers)):
            if int(soldier_id) == self.soldiers[i].soldier_id:
                self.soldiers.pop(i)
                return


    