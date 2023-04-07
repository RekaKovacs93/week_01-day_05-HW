def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]

def add_or_remove_cash(pet_shop, num):
    pet_shop["admin"]["total_cash"] += num

def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]

def increase_pets_sold(pet_shop, num):
    pet_shop["admin"]["pets_sold"] += num

def get_stock_count(pet_shop):
    return len(pet_shop["pets"])

def get_pets_by_breed(pet_shop, breed):
    pets = []
    for pet in pet_shop["pets"]:
        if breed == pet["breed"]:
            pets.append(pet)
    return pets

def find_pet_by_name(pet_shop, name):
    for pet in pet_shop["pets"]:
        if name == pet["name"]:
            return pet
        
def remove_pet_by_name(pet_shop, name):
    for pet in pet_shop["pets"]:
        if name == pet["name"]:
            pet_shop["pets"].remove(pet)

def add_pet_to_stock(pet_shop, new_pet):
    pet_shop["pets"].append(new_pet)

def get_customer_cash(customer):
    return customer["cash"]

def remove_customer_cash(customer, num):
    customer["cash"] -= num
    return customer["cash"]

def get_customer_pet_count(customer):
    return len(customer["pets"])

def add_pet_to_customer(customer, new_pet):
    customer["pets"].append(new_pet)

def customer_can_afford_pet(customer, new_pet):
    if customer["cash"] >= new_pet["price"]:
        return True
    else : 
        return False
    
def sell_pet_to_customer(pet_shop, pet, customer):
    if pet in pet_shop["pets"] and customer["cash"] >= pet["price"]:
        pet_shop["pets"].remove(pet)
        customer["pets"].append(pet)
        customer["cash"] -= pet["price"]
        pet_shop["admin"]["total_cash"] += pet["price"]
        pet_shop["admin"]["pets_sold"] += 1
    else:
        pass