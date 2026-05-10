def get_user_input():
    trek_name = input("Enter trek name: ")
    difficulty = input("Enter difficulty (easy/moderate/hard): ")
    duration_days = int(input("Enter number of days: "))
    month = input("Enter month of trek: ")
    trek_style = input("Enter trek style (camping/teahouse/day trek): ")

    return {
        "trek_name": trek_name,
        "difficulty": difficulty,
        "duration_days": duration_days,
        "month": month,
        "trek_style": trek_style
    }

def generate_packing_list(trip):
    packing_list = []

    packing_list.extend([
        "Trekking Shoes",
        "Backpack",
        "Water bottle",
        "First aid kit"
    ])

    if trip["difficulty"].lower() in ["moderate", "hard"]:
        packing_list.append("Trekking poles")

    if trip["duration_days"] > 4:
        packing_list.append("extra pair of clothes")

    if trip["month"].lower() in ["june", "july", "august"]:
        packing_list.append("Rain jacket")
    else:
        packing_list.append("Snow jacket")

    if trip["trek_style"].lower() == "camping":
        packing_list.extend(["Sleeping bag", "Tent"])
    
    return packing_list

if __name__ == "__main__":
    trip_details = get_user_input()
    print("\nTrip Details:")
    print(trip_details)

    packing_list = generate_packing_list(trip_details)

    print("\nRecommended Packing List:")
    for item in packing_list:
        print(f"- {item}")