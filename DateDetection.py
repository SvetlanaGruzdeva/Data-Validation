#! python3 
# dateDetection.py - validates date. 
 
import pyperclip, re 
 
# Set regex.
# TODO: Figure out how to check dates like 1/1/20
dateRegex = re.compile(r'''( 
    (\d{1,2})                   # day 
    (/|-|.)?                    # separator 
    (\d{1,2})                   # month 
    (/|-|.)?                    # separator 
    (\d{2,4})               # year 
    )''', re.VERBOSE)

# Find matches in clipboard text.
text = str(pyperclip.paste())
dates = []
for groups in dateRegex.findall(text):
    dates.append(groups[0])

# Identify invalid dates.
invalidDates = []
validDates = []
for element in dates:
    day = element[:2]
    month = element[3:5]
    year = element[6:]
    
    # TODO: set ranges as variables.
    if int(day) in range(1,31) and int(month) in range(1,12) and int(year) in range(1000,2999):
        if month in ('04', '06', '09', '11') and day == '31':
            invalidDates.append(element)
        if month == '02':
            if int(year) % 4 == 0:
                if int(year) % 100 == 0 and int(year) % 400 != 0 and day in ('29', '30', '31'): #не високосный год
                    invalidDates.append(element)
                else: #високосный год
                    if day in ('30', '31'):
                        invalidDates.append(element)
            else:#не високосный
                if day in ('29', '30', '31'):
                    invalidDates.append(element)

        if element not in invalidDates:
            validDates.append(element)
    else:
        invalidDates.append(element)

print(f"following dates are invalid: {', '.join(invalidDates)}")
# print(validDates)