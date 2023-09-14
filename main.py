from cab import *

# main function
def main():
    while True:
        print("-------------------------------------------MAIN MENU-------------------------------------------")
        option = int(input("Select an option: \nAdd vehicle - 0\nRemove vehicle - 1\nAssign vehicle - 2\nRelease vehicle - 3\nCheck available vehicles - 4\nCheck assigned vehicles - 5\nExit program - 6\n>>> "))
        # get only valid inputs
        if option < 0 or option > 6:
            print("\nInvalid Input!")
            continue
        # exit program
        elif option == 6:
            exit()
        else:
            if option == 0: # add vehicle
                print()
                print("-------------------------------------------ADD VEHICLE-------------------------------------------")
                add()
                print()
            elif option == 1: # remove vehicle
                print()
                print("-------------------------------------------REMOVE VEHICLE-------------------------------------------")
                remove()
                print()
            elif option == 2: # assign vehicle
                print()
                print("-------------------------------------------ASSIGN VEHICLE-------------------------------------------")
                assign()
                print()
            elif option == 3: # release vehicle
                print()
                print("-------------------------------------------RELEASE VEHICLE-------------------------------------------")
                release()
                print()
            elif option == 4: # check available vehicles
                print()
                print("-------------------------------------------AVAILABLE VEHICLE-------------------------------------------")
                checkAvailable()
                print()
            elif option == 5: # check assigned vehicles
                print()
                print("-------------------------------------------ASSIGNED VEHICLE-------------------------------------------")
                checkAssigned()
                print()
            continue

# invoke main
if __name__ == '__main__':
    main()




# Test codes
# show_vehicles()
# show_available()
# show_assigned()