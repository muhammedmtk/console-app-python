import re
from datetime import datetime
def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(pattern, email):
        return True
    else:
        print("email must follow example@gmail.com")
        return False

def is_valid_mobile(mobile):
    pattern = r'^01[0125][0-9]{8}$'
    if re.match(pattern, mobile):
        return True
    else:
        print("Error: Invalid mobile. Must be 11 digits starting with 010, 011, 012, or 015.")
        return False
    
def is_valid_date(date_text):
    try:
        datetime.strptime(date_text, '%Y-%m-%d')
        return True
    except ValueError:
        print("Error: Invalid date format. Use YYYY-MM-DD (e.g., 2026-04-05).")
        return False
    
def is_end_after_start(start_date_str, end_date_str):
    start = datetime.strptime(start_date_str, '%Y-%m-%d')
    end = datetime.strptime(end_date_str, '%Y-%m-%d')
    
    if end > start:
        return True
    else:
        print("Error: Project end date must be after the start date.")
        return False
    
def is_valid_password(password):
    if len(password) >= 8:
        return True
    else:
        print("Error: Password is too short. It must be at least 8 characters long.")
        return False
    
def is_valid_name(name):
    if name.isalpha() and len(name) > 1:
        return True
    else:
        print(f"Error: '{name}' is invalid. Names must contain only letters and be at least 2 characters long.")
        return False
    
    
def is_valid_target(target):
    try:
        target_value = float(target)
        if target_value > 0:
            return True
        else:
            print("Error: Target must be a positive number.")
            return False
    except ValueError:
        print("Error: Target must be a numeric value (e.g., 5000 or 100.5).")
        return False
    
    
def is_valid_details(details):
    clean_details = details.strip()
    
    if len(clean_details) >= 10: 
        return True
    else:
        print("Error: Details are too short. Please provide at least 10 characters.")
        return False