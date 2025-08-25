def is_leap(year) : 
    if year % 4 == 0 : 
        if year % 100 == 0 : 
            if year % 400 == 0 :
                return f"It is a leap year"
    else : 
        return f"It is not a leap year"
print(is_leap(2005))