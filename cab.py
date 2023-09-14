from vehicles import *

# variables

vehicleCount = 0

constraints = {
    'car': [3, 4],
    'van': [6, 8],
    'threewheeler': [],
    'truck': [7, 12],
    'lorry': [2500, 3500],
    }
parameters = {
    'car': 'PassengerCapacity',
    'van': 'PassengerCapacity',
    'threewheeler': 'PassengerCapacity',
    'truck': 'Size',
    'lorry': 'MaxLoad',
    }
types = ['car', 'van', 'threewheeler', 'truck', 'lorry']
vehicles = []
availableVehicles = []
assignedVehicles = []

# -------------------------------------------------------------------------------
# secondary functions

# function to get parameter inputs
def getParameter(type, msg, errorMsg):
    while True:
        parameter = int(input(f"Enter the {msg} >>> "))
        if -1 < parameter < len(constraints[type]):
            break
        else:
            print(f"\nInvalid {errorMsg}!")
            continue
    parameter = constraints[type][parameter]
    return parameter

# function to choose details
def chooseOptions():
    # get vehicle type
    while True:
        type = int(input("Enter the type of vehicle: car - 0 ,van - 1 ,threewheel - 2 ,truck - 3 ,lorry - 4 >>> "))
        if -1 < type < len(constraints):
            break
        else:
            print("\nInvalid vehicle type!")
            continue
    # find type string
    type = types[type]
    # get parameter
    if type == 'car':
        parameter = getParameter(type, "number of passengers: 3 passengers - 0, 4 passengers - 1", "passenger size")
    elif type == 'van':
        parameter = getParameter(type, "number of passengers: 6 passengers - 0, 8 passengers - 1", "passenger size")
    elif type == 'threewheeler':
        parameter = 3
    elif type == 'truck':
        parameter = getParameter(type, "size: 7 ft - 0 ,12 ft - 1", "size")
    else:
        parameter = getParameter(type, "max load: 2500kg - 0, 3500kg - 1", "max load size")

    return type, parameter

# fuction to create objects
def createObject(type, parameter, id):
    classString = type.title()
    # create a vehicle object
    object = eval(classString)(type, id, parameter)
    # add vehicle object to vehicles
    vehicles.append(object)
    # add new vehicle object to available vehicles
    availableVehicles.append(object)

# ------------------------------------------------------------------------------
# add new vehicle to the system

def add():
    # change global variable inside function
    global vehicleCount
    # choose vehicle type and parameter
    type, parameter = chooseOptions()
    # create id using current count
    id = vehicleCount
    # create and add object
    createObject(type, parameter, id)
    # increment count
    vehicleCount += 1
    # success message
    print(f"\n# Successfully added the {type} with the id of {id}!")

# -----------------------------------------------------------------------------
# show available vehicles

def checkAvailable():
    # choose vehicle type and parameter
    type, parameter = chooseOptions()
    # get method string
    getMethod = f"i.get{parameters[type]}()"
    print()
    count = 0
    for i in availableVehicles:
        if i.getType() == type and eval(getMethod) == parameter:
            print(f"Vehicle {count+1} -->")
            print(f"id: {i.getId()}")
            print(f"type: {type}")
            print(f"{parameters[type]}: {eval(getMethod)}")
            count += 1
    if count == 0:
        print("\nNo vehicles available!")


# -----------------------------------------------------------------------------
# show assigned vehicles

def checkAssigned():
    print()
    if len(assignedVehicles) == 0:
        print("No vehicles assigned!")
    else:
        for i in assignedVehicles:
            type = i.getType() # type of i elemetn
            id = i.getId() # id of i elemetn
            getMethod = f"i.get{parameters[type]}()" # get method string
            # print values
            print(f"Vehicle {assignedVehicles.index(i)+1} -->") # print vehicle sequence
            print(f"id: {id}")
            print(f"type: {type}")
            print(f"{parameters[type]}: {eval(getMethod)}")


# ----------------------------------------------------------------------------
# assign a job

def assign():
    # choose vehicle type and parameter
    type, parameter = chooseOptions()
    # get method string
    getMethod = f"i.get{parameters[type]}()"
    count = 0
    for i in availableVehicles:
        index = availableVehicles.index(i) # current index
        if i.getType() == type and eval(getMethod) == parameter:
            assignedVehicle = availableVehicles.pop(index)
            assignedVehicles.append(assignedVehicle)
            count += 1
            # success msg
            print(f"\n# Successfully assigned the {type} with the id of {i.getId()}")
            break
    if count == 0:
        print("\nNo vehicles available!")

# ----------------------------------------------------------------------------
# release vehicles

def release():
    # check if vehicles assigned
    if len(assignedVehicles) == 0:
        print("\nNo vehicles assigned!")
    else:
        while True:
            # choose vehicle id to release
            id = int(input("Enter the id of the vehicle to release >>> "))
            flag = False
            for i in assignedVehicles:
                index = assignedVehicles.index(i) # current index
                if i.getId() == id:
                    releasedVehicle = assignedVehicles.pop(index)
                    availableVehicles.append(releasedVehicle)
                    flag = True
                    # success msg
                    print(f"\n# Successfully released the {i.getType()} with the id of {i.getId()}")
                    break
            if flag:
                break
            else:
                print("\nInvalid vehicle Id!")
                continue

# ----------------------------------------------------------------------------
# remove vehicle

def remove():
    # check if vehicles are added
    if len(vehicles) == 0:
        print("No vehicles added!")
    else:
        while True:
            # choose vehicle id to remove
            id = int(input("Enter the id of the vehicle to remove >>> "))
            flag = False
            for i in vehicles:
                index = vehicles.index(i) # current index
                if i.getId() == id:
                    # remove from vehicles
                    del vehicles[index]
                    # remove from availableVehicles list / assignedVehicles list
                    if i in availableVehicles:
                        del availableVehicles[index]
                    elif i in assignedVehicles:
                        del assignedVehicles[index]
                    flag = True
                    print(f"\n# Successfully removed the {i.getType()} with the id of {id}!")
                    break
            if flag:
                break
            else:
                print("\nInvalid vehicle Id!")
                continue



# ---------------------------------------------------------------------------

#Test methods
# def show_available():
#     print("")
#     for i in availableVehicles:
#         print(i.getId(), end=", ")
# def show_assigned():
#     print("")
#     for i in assignedVehicles:
#         print(i.getId(), end=", ")
# def show_vehicles():
#     print("")
#     for i in vehicles:
#         print(i.getId(), end=", ")
