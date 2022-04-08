from datetime import datetime

dt = datetime.today()
d = dt.date()
print('please press day example ' + str(d))
day = input()
print("search of the", day)

dtday = datetime.strptime(day, '%Y-%m-%d') - datetime(1899, 12, 31)
serial = dtday.days + 1
print(serial)
#Add to the flow of each group
print(serial+ 6)
print(hex(serial+ 6))
char = hex(serial+6)
length = len(hex(serial+6))
char02 = char[length - 1]
print(char02)

threeshiftswork = {"1":"甲①","2":"甲②","3":"甲③","4":"甲④","5":"休","6":"乙①","7":"乙②","8":"乙③","9":"乙④","a":"休","b":"丙①","c":"丙②","d":"丙③","e":"丙④","f":"休","0":"休",}

if char02 in threeshiftswork:
    val = threeshiftswork[char02]
    print(val)
    