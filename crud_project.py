from officers import Officers
from soldiers import Soldiers

    

def main():

    soldiers = Soldiers()
    officers = Officers()

    while True:
        print("\n===============")
        print("     MENU ")
        print("1 - Create soldier")
        print("2 - Read soldier")
        print("3 - Update soldier")
        print("4 - Delete soldier")
        print("5 - Create officer")
        print("6 - Read officer")
        print("7 - Update officer")
        print("8 - Delete officer")
        print("9 - Exit")
        choice = int(input("Pick one: "))

        if choice == 1:
            print("NEW soldier")
            print("===========")
            soldier = soldiers.create_soldier()
            #save changes
            soldiers.save_soldiers_data()
            if soldier is None:
                continue
            else:
                print("NEW soldier")
                print(soldier)

        elif choice == 2:
            print("\n===============")
            print("     SUB-MENU (PRINT) ")
            print("1 - Print soldier")
            print("2 - Print all soldiers (details)")
            print("3 - Print all soldiers (just the names)")
            print_choice = input("Give your choice: ")
            if print_choice.strip().isdigit():
                print_choice = int(print_choice)
            else:
                print("Wrong input!")
                continue

            if print_choice == 1:
                soldier_id = soldiers.is_digit()
                soldier = soldiers.search_soldier_by_id(soldier_id)
                if soldier is None:
                    print("Soldier  does not exist (with this id)")
                else:
                    print("   soldier   ")
                    print(soldier)

            elif print_choice == 2:
                soldiers.print_soldiers()
            
            elif print_choice == 3:
                soldiers.print_soldiers_names()
            else:
                print("Wrong input! ")
                continue

        elif choice == 3:
            print("\n===============")
            print("     SUB-MENU (UPDATE) ")
            print("1 - Update soldier (search by id)")
            print("2 - Update soldier (search by surname)")
            update_choice = input("Give your choice: ")
            if update_choice.strip().isdigit():
                update_choice = int(update_choice)
            else:
                print("Wrong input!")
                continue

            if update_choice == 1:
                soldier_id = soldiers.is_digit()
                soldier = soldiers.search_soldier_by_id(soldier_id)
                if soldier is None:
                    print("Error! There is no soldier with this id!")
                    continue
            elif update_choice == 2:
                surname = input("Give surname: ").capitalize()
                matching_soldiers = soldiers.search_soldier_by_surname(surname)
                if not matching_soldiers:
                    print("No matching soldiers with this surname!")
                    continue
                elif len(matching_soldiers) == 1:
                    soldier = matching_soldiers[0]
                else:
                    for p in matching_soldiers:
                        print(p)
                        print(f"id = {p.soldier_id}")
                        print("-" * 15)
                    soldier_id = soldiers.is_digit()
                    soldier = soldiers.search_soldier_by_id(soldier_id)
            else:
                print("The choice you put doesn't exist!")
                continue

            # soldier: update
            soldiers.soldier_update(soldier)
            #save changes
            soldiers.save_soldiers_data()

        elif choice == 4:
            print("\n===============")
            print("     SUB-MENU (DELETE) ")
            print("1 - Delete soldier (search by id)")
            print("2 - Delete soldier (search by surname)")
            delete_choice = input("Give your choice: ")
            if delete_choice.strip().isdigit():
                delete_choice = int(delete_choice)
            else:
                print("Wrong input!")
                continue
            #delete with id
            if delete_choice == 1:
                soldier_id = soldiers.is_digit()
                soldier = soldiers.search_soldier_by_id(soldier_id)
                if soldier is None:
                    print("Error! There is no soldier with this id!")
                    continue
            #delete with surname
            elif delete_choice == 2:
                surname = input("Give surname: ").capitalize()
                matching_soldiers = soldiers.search_soldier_by_surname(surname)
                if not matching_soldiers:
                    print("No matching soldiers with this surname!")
                    continue
                elif len(matching_soldiers) == 1:
                    soldier_id = matching_soldiers[0].soldier_id
                else:
                    for p in matching_soldiers:
                        print(p)
                        print(f"id = {p.soldier_id}")
                        print("-" * 15)
                    soldier_id = int(input("Give id: "))
                    soldier = soldiers.search_soldier_by_id(soldier_id)
            else:
                print("The choice you put doesn't exist!")
                continue
            # soldier: delete
            soldiers.delete_soldier_by_id(soldier_id)
            #save changes
            soldiers.save_soldiers_data()
        #Creates an officer
        elif choice==5:
            first_name = input("Give name: ").capitalize()   
            surname = input("Give surname: ").capitalize()
            birth_date = input("Give your birthday: ")
            phone_number = input("Give your telephone: ")
            officers.create_officer(first_name, surname, birth_date, phone_number)
            officers.save_officers_data() #saves in json file new object ("w")
        #print officer choices
        elif choice==6:
            officer_id = officers.is_digit() #checks if the input is digit
            surname = input("Give surname: ").capitalize()
            officers.read_officer(officer_id, surname)
            officers.save_officers_data()
        #makes update
        elif choice==7:
            officer_id = officers.is_digit() #checks if the input is digit
            surname = input("Give the Surname: ").capitalize()
            officers.update_officer(officer_id, surname)
            officers.save_officers_data()
        #deletes an officer
        elif choice==8:
            officer_id = officers.is_digit() #checks if the input is digit
            officer_surname = input("Give the Surname: ").capitalize()
            officers.delete_officer(officer_id, officer_surname)
            officers.save_officers_data()
        #exit
        elif choice==9:
            print("Thank you for your time!")
            officers.save_officers_data()
            soldiers.save_soldiers_data()
            break


main()