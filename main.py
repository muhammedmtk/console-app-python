import auth 
import project_ops 
import json 
from utils import (load_data, get_valid_name, get_valid_email, 
                   get_valid_password, get_valid_mobile, get_valid_dates, 
                   get_valid_target, get_valid_details)

def main_menu():
    while True:
        db = load_data()
        if not db["login"]:
            current_user_id = None
        else:
            current_user_id = db["login"][0]
            
        print("\n" + "="*30)
        if not current_user_id:
            print("--- Welcome to CrowdFunding ---")
            print("1. Register")
            print("2. Login")
            print("3. Exit")
        else:
            print(f"--- Welcome Back (User ID: {current_user_id}) ---")
            print("1. Create Project")
            print("2. Edit My Project")
            print("3. Delete My Project")
            print("4. View All Projects")
            print("5. Logout")
            print("6. Exit")
        
        choice = input("\nChoose an option: ")
        
        if not current_user_id:
            if choice == "1":
                f_name = get_valid_name("First Name: ")
                l_name = get_valid_name("Last Name: ")
                email = get_valid_email("Email: ", check_duplicate=True)
                password = get_valid_password("Password: ")
                mobile = get_valid_mobile("Mobile: ")
                auth.register(f_name, l_name, email, password, mobile)
            
            elif choice == "2":
                email = get_valid_email("Email: ")
                password = get_valid_password("Password: ")
                auth.login(email, password)
                   
            elif choice == "3":
                break
            
        else:
            if choice == "1":
                title = input("Project Title: ")
                details = get_valid_details("Details: ")
                target = get_valid_target("Target Amount: ")
                start_date, end_date = get_valid_dates(
                    "Start Date (YYYY-MM-DD): ",
                    "End Date (YYYY-MM-DD): "
                )
                project_ops.create_project(title, details, target, start_date, end_date)

            elif choice == "2":
                p_id = int(input("Enter Project ID to edit: "))
                project_ops.edit_project(p_id)

            elif choice == "3":
                p_id = int(input("Enter Project ID to delete: "))
                project_ops.delete_project(p_id)

            elif choice == "4":
                project_ops.view_all_projects()

            elif choice == "5":
                auth.logout()
                continue
            
            elif choice == "6":
                break

if __name__ == "__main__":
    main_menu()