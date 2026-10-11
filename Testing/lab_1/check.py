def check_number(number):
    assert number > 0, "Число має бути більшим за нуль!"
    return number


print(check_number(5))   
print(check_number(-1))  