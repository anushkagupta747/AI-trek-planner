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

if __name__ == "__main__":
    trip_details = get_user_input()
    print("\nTrip Details:")
    print(trip_details)