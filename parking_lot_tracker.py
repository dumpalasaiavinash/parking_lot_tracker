available_spots = {"A": list(range(1, 21)), "B": list(range(21, 41))}
vehicle_spot_map = {}

def assign_parking_spot(vehicle_number):
    for level, spots in available_spots.items():
        if spots:
            spot = spots.pop(0)
            vehicle_spot_map[vehicle_number] = {"level": level, "spot": spot}
            return f"Allocated spot: {level}-{spot}"
    return "Sorry, parking lot is full."

def retrieve_parking_spot(vehicle_number):
    if vehicle_number in vehicle_spot_map:
        spot = vehicle_spot_map[vehicle_number]
        return {"level": spot["level"], "spot": spot["spot"]}
    else:
        return "Vehicle not found in parking lot."


def main():
    while True:
        print("\Parking Lot Tracker:")
        print("1. Assign a parking lot to a new vehicle.")
        print("2. Retrieve parking spot number of a particular vehicle.")
        print("3. Exit")

        choice = input("Enter the operation number (1, 2, or 3): ")

        if choice == "1":
            vehicle_number = input("Enter the vehicle number: ")
            print(assign_parking_spot(vehicle_number))
        elif choice == "2":
            vehicle_number = input("Enter the vehicle number: ")
            print(retrieve_parking_spot(vehicle_number))
        elif choice == "3":
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

main()