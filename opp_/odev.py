# Input data: List of dictionaries
employee_list = [
   {"id": 12345, "name": "John", "department": "Kitchen"},
   {"id": 12456, "name": "Paul", "department": "House Floor"},
   {"id": 12478, "name": "Sarah", "department": "Management"},
   {"id": 12434, "name": "Lisa", "department": "Cold Storage"},
   {"id": 12483, "name": "Ryan", "department": "Inventory Mgmt"},
   {"id": 12419, "name": "Gill", "department": "Cashier"}
]


# Function to be passed to the map() function. Do not change this.
def mod(employee_list):
   temp = employee_list['name'] + "_" + employee_list["department"]
   return temp

def to_mod_list(employee_list):
    
    return list(map(mod,employee_list))

    # mod_list = []
    # name_list = []
    # department_list = []
    # liste = map(lambda a : a , employee_list)
    # for x in liste:
    #     idx,name,department = x.items()
        
    #     name_list.append(name[1])
    #     department_list.append(department[1])
        
    #     mod_list.append((f"{name[1]}  {department[1]}"))
    # # print(name_list,department_list)
    # return mod_list
   
    
""" Modifies the employee list of dictionaries into list of employee-department strings

   [IMPLEMENT ME] 
      1. Use the map() method to apply mod() to all elements in employee_list

   Args:
      employee_list: list of employee objects

   Returns:
      list - A list of strings consisting of name + department.
   """
   ### WRITE YOUR CODE HERE ###

def generate_usernames(mod_list):
    new_list = [x.replace(" ","_") for x in mod_list]
    return new_list
    """ Generates a list of usernames 

   [IMPLEMENT ME] 
      1. Use list comprehension to replace space characters with underscores

   Args:
      mod_list: list of employee-department strings

   Returns:
      list - A list of usernames consisting of name + department delimited by underscores.
   """
   ### WRITE YOUR CODE HERE ###

def map_id_to_initial(employee_list):
    # emp_list = [i["name"][0] for i in employee_list]
    
    new_list = {ch["name"][0]:ch["id"] for ch in employee_list}
    return new_list
    
    pass
    """ Maps employee id to first initial

   [IMPLEMENT ME] 
      1. Use dictionary comprehension to map each employee's id (value) to the first letter in their name (key)

   Args:
      employee_list: list of employee objects

   Returns:
      dict - A dictionary mapping an employee's id (value) to their first initial (key).
   """
   ### WRITE YOUR CODE HERE ###

def main():
    # print(to_mod_list(employee_list))
    # print(mod(employee_list))
    mod_emp_list = to_mod_list(employee_list)
    print("Modified employee list: " + str(mod_emp_list) + "\n")

    print(f"List of usernames: {generate_usernames(mod_emp_list)}\n")

    print(f"Initials and ids: {map_id_to_initial(employee_list)}")

if __name__ == "__main__":
   main()
