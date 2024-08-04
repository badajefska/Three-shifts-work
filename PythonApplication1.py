from datetime import datetime

def calculate_shift(day):
    dtday = datetime.strptime(day,'%Y-%m-%d') -datetime(1899,12,31)
    serial = dtday.days + 1
    char = hex(serial + 6)
    char02 = char[-1]

    threeshiftswork = {
            "1": "甲①", "2": "甲②", "3": "甲③", "4": "甲④", "5": "休",
        "6": "乙①", "7": "乙②", "8": "乙③", "9": "乙④", "a": "休",
        "b": "丙①", "c": "丙②", "d": "丙③", "e": "丙④", "f": "休", "0": "休",
    }

    if char02 in threeshiftswork:
        return threeshiftswork[char02]
    else:
        return None

day = input('Please enter a date (YYYY-MM-DD): ')
shift = calculate_shift(day)
print(f"The shift for {day} is : {shift}")

