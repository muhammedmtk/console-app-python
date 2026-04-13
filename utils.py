import json
import os
import validators


DB_FILE = "db.json"
def load_data():
    if not os.path.exists(DB_FILE):
        initial_structure = {"users": [], "projects": [], "login": []}
        save_data(initial_structure)
        return initial_structure
    
    with open(DB_FILE, "r") as f:
        try:
            database = json.load(f)
            if "login" not in database:
                database["login"] = []
            if "projects" not in database:
                database["projects"] = []
            if "users" not in database:
                database["users"] = []
                
            return database
        except json.JSONDecodeError:
            return {"users": [], "projects": [], "login": []}       
    
    
def save_data(data):
    json_str = json.dumps(data, indent=4)
    with open("db.json", "w") as f:
        f.write(json_str)
    
    

def generate_user_id(users_list):
    if not users_list:
        return 1
    
    ids = []
    for user in users_list:
        ids.append(user["id"])
    
    return max(ids) + 1
  
    
def generate_project_id(projects_list):
    if not projects_list:
        return 1
    
    id_projects = []
    for project in projects_list:
        id_projects.append(project["id"])
    
    return max(id_projects) + 1


# ============ INPUT VALIDATION FUNCTIONS ============
# These functions data the user repeatedly until valid input is received

def get_valid_name(data):
    """Get a valid name from user (letters only, at least 2 characters)"""
    while True:
        name = input(data)
        if validators.is_valid_name(name):
            return name
        print("Please try again.")

def get_valid_email(data, check_duplicate=False):
    """Get a valid email from user. If check_duplicate=True, ensures it's not already registered."""
    while True:
        email = input(data)
        if validators.is_valid_email(email):
            if check_duplicate:
                db = load_data()
                for user in db["users"]:
                    if user["email"] == email:
                        print("Error: This email is already registered!")
                        print("Please try again.")
                        continue
            return email
        print("Please try again.")

def get_valid_password(data):
    """Get a valid password from user (at least 8 characters)"""
    while True:
        password = input(data)
        if validators.is_valid_password(password):
            return password
        print("Please try again.")

def get_valid_mobile(data):
    """Get a valid mobile number from user (Egyptian format: 01[0125]xxxxxxxx)"""
    while True:
        mobile = input(data)
        if validators.is_valid_mobile(mobile):
            return mobile
        print("Please try again.")

def get_valid_date(data):
    """Get a valid date from user (format: YYYY-MM-DD)"""
    while True:
        date_str = input(data)
        if validators.is_valid_date(date_str):
            return date_str
        print("Please try again.")

def get_valid_dates(start_data, end_data):
    """Get valid start and end dates where end date must be after start date"""
    while True:
        start_date = get_valid_date(start_data)
        end_date = get_valid_date(end_data)
        if validators.is_end_after_start(start_date, end_date):
            return start_date, end_date
        print("End date must be after start date. Please try again.")

def get_valid_target(data):
    """Get a valid target amount from user (positive number)"""
    while True:
        target = input(data)
        if validators.is_valid_target(target):
            return target
        print("Please try again.")

def get_valid_details(data):
    """Get valid project details from user (at least 10 characters)"""
    while True:
        details = input(data)
        if validators.is_valid_details(details):
            return details
        print("Please try again.")