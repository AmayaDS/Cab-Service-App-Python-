print("Welcome to EASY Cabs!")
 
def userRequirments(vehicleType,noSeat,condition):
    print()
    print("vehicle type: " + vehicleType)
    print("Number of seats: ", noSeat)
    print("AC or non AC: ", condition)

vehicle = ["Car","Van","3 Wheeler","Truck","Lorry"]
AC_Cars =["AC01","AC02","AC03"]
nonAC_Cars =["NAC01","NAC02","NAC03"]
AC_vans =["VAC01","VAC02","VAC03"]
nonAC_vans =["NVAC01","NVAC02","NVAC03"]
ThreeWheelers =["3W01","3W02","3W03"]
Truck =["TS01","TS02","TS03"]
lorries =["LS01","LS02","LS03"]

#customer interface
print("\t01. Customer Interface")
print("\t02. Edit information\n")

part = input("If you want to hire a vehicle press \"01\":\nIf you want to edit vehicle info press\"02\":")


if (part =="01"):
    #user inputtiing info
    vehicleType = input("Enter Vehicle type you want: ")

    #
    if (vehicleType == "car"):
        vehicleType = "Car"

    #
    if (vehicleType == "van"):
        vehicleType = "Van"

    #
    if (vehicleType == "three Wheeler" or vehicleType == "Three wheeler" or
        vehicleType == "3 wheeler" or vehicleType == "three wheeler"):
        vehicleType = "3 Wheeler"

    #
    if (vehicleType == "lorry"):
        vehicleType = "Lorry"
    
    #
    if (vehicleType == "truck"):
        vehicleType = "Truck"

    #    
    if (vehicleType == vehicle[0]):
        noSeat = int(input("Enter number seats expected: "))
        while ( noSeat <= 0 or noSeat > 4):
            print("Cars can only carry 4 passangers!")
            noSeat = int(input("Try again!"))
            print()

        condition = int(input("Do you want AC or Non AC car\nInput 1 for \"AC\" or 2 for \"non AC\" "))
        while ( condition !=1 and condition !=2):
            print("Invalid input")
            condition = int(input("Try again!"))
            print()
            
        if (condition == 1):
            userRequirments(vehicleType,noSeat,condition)
            print ("Here is your car!")
            print("Car Number: " + AC_Cars[0])
            AC_Cars.remove(AC_Cars[0])
        elif (condition == 2):
            userRequirments(vehicleType,noSeat,condition)
            print ("Here is your car!")
            print("Car Number: " + nonAC_Cars[0])
            nonAC_Cars.remove(nonAC_Cars[0])
    
    elif (vehicleType == vehicle[1]):
        noSeat = int(input("Enter number seats expected: "))
        while ( noSeat <= 0 or noSeat > 8):
            print("Vans can only carry 8 passengers")
            noSeat = int(input("Try again!"))
            print()
        
        condition = int(input("Do you want AC or Non AC car\nPress 1 for \"AC\" or 2 for \"non AC\" "))
        while ( condition !=1 and condition !=2):
            print("Invalid input")
            condition = int(input("Try again!"))
            print()
            
        if (condition == 1):
            userRequirments(vehicleType,noSeat,condition)
            print ("Here is your Van!")
            print("Van Number: " + AC_vans[0])
            AC_vans.remove(AC_vans[0])
        elif (condition == 2):
            userRequirments(vehicleType,noSeat,condition)
            print ("Here is your Van!")
            print("Van Number: " + nonAC_vans[0])
            nonAC_vans.remove(nonAC_vans[0])
    
    elif (vehicleType == vehicle[2]):
        noSeat = int(input("Enter number seats expected: "))
        while ( noSeat <= 0 or noSeat > 3):
            print("Three Wheelers can only carry 3 passengers!")
            noSeat = int(input("Try again!"))
            print()
          
        condition = "Normal"
        userRequirments(vehicleType,noSeat,condition)
        print ("Here is your three wheeler!")
        print("Three Wheeler Number: " + ThreeWheelers[0])
        ThreeWheelers.remove(ThreeWheelers[0])

        
    elif (vehicleType == vehicle[3]):
        size = int(input("What is the size of the truck? "))
        while ( size <= 0 or size > 12):
            print("Maximun length of a truck is 12ft !")
            size = int(input("Try again!"))
            print()
            
        
        if (size<=12):
            print()
            print("Vehicle type: " + vehicleType)
            print("Size of the Truck: ", size)
            print("Here is your Truck!")
            print("Truck Number: " + Truck[0])
            Truck.remove(Truck[0])
        else:
            quit()

    elif (vehicleType == vehicle[4]):
        size = int(input("How many KGs do you expects to carry? "))
        while ( size <= 0 or size > 3500):
            print("Lorries can carry only upto 3500kg")
            size = int(input("Try again!"))
            print()

        if (size <= 0 or size > 3500):
            print()
            print("Vehicle type: " + vehicleType)
            print("Load the lorry is carrying: ", size)
            print("Here is your lorry!")
            print("Lorry Number: " + lorries[0])
            lorries.remove(lorries[0])
        else:
            quit()

        
    else:
        #owner can add and remove cars
        print("\t1. Add a Vehicle")
        print("\t2. Remove a Vehicle")
        print("\t3. Assign a job")
        print("\t4. Available vehicle list")
        
    ownerChoice = input("What do you want to do?: ")
        
    if (ownerChoice=="1" or ownerChoice=="01"):
        print("\nWhat vehicle do you want to Add? \n")
        print("\t1. Car")
        print("\t2. Van")
        print("\t3. Three Wheeler")
        print("\t4. Truck")
        print("\t5. Lorry")

    addVehicle = input("\nChoose from above: ")
    #add a car
    if (addVehicle =="01" or addVehicle=="1"):
        print("\nChoose the car type \n")
        print("\t1. AC Cars")
        print("\t2. non-AC Cars")

    carType = int(input("AC or non AC: "))
    if (carType ==1):
        newCar = input("Enter the Car number: ")
        AC_Cars.append(newCar)
    if (carType ==2):
        newCar = input("Enter the Car number: ")
        nonAC_Cars.append(newCar)

    # add a van
    if (addVehicle =="02" or addVehicle=="2"):
        print("\nChoose the van type \n")
        print("\t1. AC vans")
        print("\t2. non-AC vans")

    vanType = int(input("AC or non AC: "))

    if (vanType ==1):
        newvan = input("Enter the Van number: ")
        AC_vans.append(newvan)
    if (vanType ==2):
        newvan = input("Enter the Van number: ")
        nonAC_vans.append(newvan)

    # add a ThreeWheeler
    if (addVehicle =="03" or addVehicle=="3"):
        newThreeWheelers = input("Enter the Three Wheeler number: ")
        ThreeWheelers.append(newThreeWheelers)

    #add a Truck
    if (addVehicle =="04" or addVehicle=="4"):
        newTruck = input("Enter the Truck number: ")
        Truck.append(newTruck)

    #add a lorry
    if (addVehicle =="05" or addVehicle=="5"):
        newlorry = input("Enter the Lorry number: ")
        lorries.append(newlorry)


    #to remove vehicles
    if (ownerChoice=="2" or ownerChoice=="02"):
        print("\nChoose the vehicle type you wants to remove \n")
        print("\t1. Car")
        print("\t2. Van")
        print("\t3. 3 Wheeler")
        print("\t4. Truck")
        print("\t5. Lorry")

    addVehicle = input("\nWhat do you want to remove? ")
                            
    #remove a car
    if (addVehicle =="01" or addVehicle=="1"):
        newCar = input("Enter the car number: ")
        AC_Cars.remove(newCar)

    if (carType ==2):
        newCar = input("Enter the car number: ")
        nonAC_Cars.remove(newCar)
        
    #remove a van
    if (addVehicle =="02" or addVehicle=="2"):
        print("\nChoose the van type \n")
        print("\t1. AC vans")
        print("\t2. non-AC vans")

    vanType = int(input("Ac or non AC: "))
                
    if (vanType ==1):
        newvan = input("Enter the van number: ")
        AC_vans.remove(newvan)

    if (vanType ==2):
        newvan = input("Enter the van number: ")
        nonAC_vans.remove(newvan)

    #remove a ThreeWheeler
    if (addVehicle =="03" or addVehicle=="3"):
        newThreeWheelers = input("Enter the Three Wheeler number: ")
        ThreeWheelers.remove(newThreeWheelers)

    #remove a Truck
    if (addVehicle =="04" or addVehicle=="4"):
        newTruck = input("Enter the Truck number: ")
        TruckS.remove(newTruck)

    #remove a lorry
    if (addVehicle =="05" or addVehicle=="5"):
        newlorry = input("Enter the lorry number: ")
        lorries.remove(newlorry)
car
         