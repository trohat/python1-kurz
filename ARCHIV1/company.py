company = [
    {
        "id" : "os1",
        "full_name": "Jan Novák",
        "room_number": 3,
        "phone": "+420 777 123 456",
        "email": "jan.novak@company.cz"
    },
    {
        "full_name": "Pavel Černý",
        "room_number": 7,
        "phone": "+420 777 654 321",
        "email": "pavel.cerny@company.cz"
    },
    {
        "full_name": "Jiří Smrk",
        "room_number": 7,
        "phone": "+420 777 555 555",
        "email": "jiri.smrk@company.cz"
    }
]

id = 3

def add_employee(full_name, room_number, phone, email = "all@company.cz"):
    employee = {
        "full_name": full_name,
        "room_number": room_number,
        "phone": phone,
        "email": email
    }
    global id
    id += 1
    company[f"os{id}"] = employee
    return employee

new_employee = add_employee("Dan Morávek", 5, "774 558 993", "nemam.email@company.cz")



def del_employee(employee_id: str):
    """
    Deletes an employee
    employee_id: string - id of the employee
    """
    deleted_employee = company[employee_id]
    del company[employee_id]
    return deleted_employee

del_employee("os2")

print(company)

def find_employee_with_phone(phone):
    for employee in company.values():
       if phone == employee["phone"]:
           return f"Employee with phone {phone} is {employee['full_name']}"
    return f"Employee with phone {phone} not found"

print(find_employee_with_phone("+420 777 123 456"))
print(find_employee_with_phone("neexistující telefon"))


def replace_employee_data(employee_id, data, new_value):
    """
    Replaces one thing about employee
    employee_id - id in format "os4"
    data - key to be replaced, eg. phone, room_number, etc.
    """
    #if employee_id not in company:
    #    return False
    #if data not in company[employee_id]:
    #    return False
    company[employee_id][data] = new_value
    return company[employee_id]

replace_employee_data("os3", "room_number", 8)
replace_employee_data("os3", "skype", 8)
print(company)


replace_employee_data("os2", "room_number", 8)
