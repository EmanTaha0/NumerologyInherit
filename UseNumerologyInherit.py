from NumerologyLifePathDetails import NumerologyLifePathDetails

def is_valid_date(date_str):
    cleaned = date_str.replace("-", "").replace("/", "")
    return cleaned.isdigit() and len(cleaned) == 8

def main():

    name = input("Enter your full birth name: ").strip()
    dob = input("Enter your date of birth (mm-dd-yyyy or mm/dd/yyyy): ").strip()

    if not name:
        print("Error: Name cannot be empty.")
        return

    if not is_valid_date(dob):
        print("Error: Date must contain 8 digits in mm-dd-yyyy or mm/dd/yyyy format.")
        return

    client = NumerologyLifePathDetails(name, dob)

    print("\n--- Numerology Reading ---")
    print(f"Name: {client.Name}")
    print(f"Birthdate: {client.Birthdate}")
    print(f"Attitude Number: {client.Attitude}")
    print(f"Birth Day Number: {client.BirthDay}")
    print(f"Life Path Number: {client.LifePath}")
    print(f"Soul Number: {client.Soul}")
    print(f"Personality Number: {client.Personality}")
    print(f"Power Name Number: {client.PowerName}")
    print(f"Life Path Description: {client.LifePathDescription}")

main()
