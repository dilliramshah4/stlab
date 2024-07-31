#2) Design, develop, code and run the program in any suitable language to implement the
#NextDate function. Analyse it from the perspective of equivalence class value testing,
#derive different test cases, execute these test cases and discuss the test results.





def next_date(year, month, day):
    # Validate the inputs
    if not (1 <= year <= 9999):
        raise ValueError("Invalid year")
    if not (1 <= month <= 12):
        raise ValueError("Invalid month")
    if not (1 <= day <= 31):
        raise ValueError("Invalid day")
    
    # Determine the next date
    if month in [1, 3, 5, 7, 8, 10, 12]: # Months with 31 days
        if day < 31:
            return year, month, day + 1
        else:
            if month == 12:  # Handle end of year transition
                return year + 1, 1, 1
            else:
                return year, month + 1, 1
    elif month == 2:  # February
        # Check for leap year
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            if day < 29:
                return year, month, day + 1
            else:
                return year, month + 1, 1
        else:
            if day < 28:
                return year, month, day + 1
            else:
                return year, month + 1, 1
    else:  # Months with 30 days
        if day < 30:
            return year, month, day + 1
        else:
            return year, month + 1, 1

# Test cases
print("Valid dates:")
print(next_date(2022, 6, 15)) # (2022, 6, 16)
print(next_date(2022, 6, 30)) # (2022, 7, 1)
print(next_date(2022, 12, 31)) # (2023, 1, 1)
print(next_date(2020, 2, 28)) # (2020, 2, 29)
print(next_date(2019, 2, 28)) # (2019, 3, 1)

print("\nInvalid dates:")
try:
    print(next_date(0, 6, 15)) # Error
except ValueError as e:
    print(e)
try:
    print(next_date(2022, 13, 15)) # Error
except ValueError as e:
    print(e)
try:
    print(next_date(2022, 6, 32)) # Error
except ValueError as e:
    print(e)
