print("""<<==========            Hello and Welcome to the Mystery Hotel!🏩            ==========>>
<<==========           Please enter your information to proceed.📝           ==========>>
<<==========     [Room R104, R108, R111, R113 and R117 are reserved.]🚪      ==========>>\n""")

name = input(">> 👤 Please enter your name: ")
address = input(">> 📍 Please enter your address: ")

def get_phoneNumber():
    while True:
        try:
            phone_number_str = input(">> 📱 Please enter your phone number: ")
            phone_number = int(phone_number_str)

            if len(phone_number_str) == 11:
                break
            else:
                print ("❎ Your phone number should consists of 11 (eleven) numbers.")
        except ValueError:
            print("❎ Invalid input. Please enter numbers for your phone number.")
get_phoneNumber()

def get_room_number(): 
    reserved_rooms = {'R104', 'R108', 'R111', 'R113', 'R117'}
    available_rooms = {'R101', 'R102', 'R103', 'R105', 'R106', 'R107', 'R109', 'R110', 'R112', 'R114', 'R115', 'R116', 'R118', 'R119', 'R120'}

    while True:
        try:
            room_number = input(">> 🚪 Please enter your room number (Format: R101 to R120): ")

            if room_number [0] == 'R' and ' ' not in room_number[1:] and 101 <= int (room_number [1:]) <= 120:
                if room_number in available_rooms:
                    print (f"✅ Room is available!")
                    return room_number
                else:
                    print (f"❎ Room entered '{room_number}' has already been reserved, please select another room!") 
            else:
                raise ValueError
        except ValueError:
            print (f"❎ Room entered '{room_number}' is not valid , please enter a valid room! ")
room_number = get_room_number()

def get_date_of_check_in():
    months_31Days = ("January", "March", "May", "July", "August", "October", "December")
    months_30Days = ("April", "June", "September", "November")
    month_28Days = ("February")

    while True:
        try:
            date_of_check_in = input(">> 📅 Please enter your date of check-in (e.g. February 14, 2023): ")

            month = date_of_check_in.split()[0]
            day = int(date_of_check_in.split()[1].replace(",", ""))
            year = int(date_of_check_in.split()[2])

            if month in months_31Days and 1 <= day <= 31 and year >= 2023:
                return date_of_check_in
            elif month in months_30Days and 1 <= day <= 30 and year >= 2023:
                return date_of_check_in
            elif month in month_28Days and 1 <= day <= 28 and year >= 2023:
                return date_of_check_in
            else:
                raise ValueError
        except (ValueError, IndexError):
            print(f"❎ '{date_of_check_in}' is not valid, please enter a valid date.")
date_of_check_in = get_date_of_check_in()

def get_days_of_staying():

    while True:
        try:
            days_of_staying = int(input(">> 📅 Please enter your how many days you will be staying (Format: 1 to 100):"))

            if 1 <= days_of_staying <= 100:
                return days_of_staying
            else:
                print ("❎ Days entered cannot be less than 1 or more then 100!")
        except ValueError:
            print("❎ You did not enter a valid number of days! ")
days_of_staying = get_days_of_staying()

print(f"""\n🏩 🎫 🎫 🎫 🎫 🎫    Mystery Hotel - Reservation Ticket   🎫 🎫 🎫 🎫 🎫 🏩
🏩 🎫 🎫 🎫 🎫 🎫   Your reservation has been processes!  🎫 🎫 🎫 🎫 🎫 🏩 """)
print(f">> 📌 Name: {name}")
print(f">> 📌 Room Number: {room_number}")
print(f">> 📌 Date of Check-in: {date_of_check_in}")
print(f">> 📌 Days Staying: {days_of_staying} days")



