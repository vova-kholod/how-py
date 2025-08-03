days = {
    1 : "Monday",
    2 : "Tuesday",
    3 : "Wensday",
    4 : "Thirsday",
    5 : "Friday",
    6 : "Sataday",
    7 : "Sunday"
}

def day_from_dic(day):
    if day in days:
        return days[day]
    else:
        return "There are only 7 days in a week."

def day_of_week(day):
    match day:
        case 1:
            return "Monday"
        case 2:
            return "Tuesday"
        case 3:
            return "Wensday"
        case 4:
            return "Thirsday"
        case 5:
            return "Friday"
        case 6:
            return "Sataday"
        case 7:
            return "Sunday"
        case _:
            return "There are only seven days in a week."


day = day_from_dic(0)
print("Day of week: ", day)
