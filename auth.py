from utils import load_data, save_data, generate_user_id, get_valid_email, get_valid_password, get_valid_name, get_valid_mobile
import validators
from models import create_user

def register(first_name, last_name, email, password, mobile):
    db = load_data()
    
    for user in db["users"]:
        if email == user["email"]:
            print("Error: This email is already registered!")
            return False
        
    new_id = generate_user_id(db["users"])
    new_user = create_user(new_id, first_name, last_name, email, password, mobile)
    
    db["users"].append(new_user)
    save_data(db)
    print("Registration Successful! Welcome", first_name)
    return True
    
    

def login(email, password):
    db = load_data()
    for user in db["users"]:
        if user["email"] == email and user["password"] == password :
            print(f"Welcome back, {user['first_name']}!")
            db["login"] = [user["id"]]
            save_data(db)
            return user
        
    print("Error: Invalid email or password.")
    return False


def is_login(user_id):
    db = load_data()
    if user_id in db["login"]:
        return True
    else:
        return False
    

def logout():
    db = load_data()
    db["login"] = []
    save_data(db)       
    print("Logged out successfully. See you soon!")
    return True