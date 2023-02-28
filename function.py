def validate_number(number):
    if  type(number) != int:
        if type(number) == str:
            return "Input Integer"
        elif number >=1 and number <=12:
            return "Input Integer"
        else:
            return "Out of Range"
    elif number >=1 and number <=12:
        return number
    else:
        return "Out of Range"

def number_to_month(number):
    month = ["January","February","March","April","May","June","July","August","September","October","November","December"]
    return month[number-1]

def display_month(number):
    result = validate_number(number)
    if type(result) == int:
        return number_to_month(result)
    else:
        return result