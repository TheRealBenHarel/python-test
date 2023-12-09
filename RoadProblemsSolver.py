
vehicle_number = input("Please choose one of the two options...\nThis VPS is designed to assist only in up to 2 vehicle problems\n \
    Are there 2 vehicles in the problem, or 1?\n")

if vehicle_number == 1:
    print("1 it is!")
    



match vehicle_number:
    case "1":
        print("Good! It makes things easier.")
    case "2": 
        print("Ok, we can manage.")
    case _:
        matching_recursion()

    

