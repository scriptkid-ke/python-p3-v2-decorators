def check_working_hours(func):
    def wrapper(time):
        if 1100 < time < 2100:
            func(time)
            else:
                print("I am off Duty!")
    return wrapper

@check_working_hours
def swipping_floors(time):
    print("Sweping the floors")

@check_working_hours
def washing_clothes(time):
    print("Washing clothes")

swipping_floors(800)
