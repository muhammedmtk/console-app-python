from utils import load_data, save_data, generate_project_id, get_valid_date, get_valid_target, get_valid_details
import validators
from models import create_project as make_project
def create_project(title,details,target,start_date,end_date):
    db = load_data()
    
    if not db["login"]:
        print("Error: You must be logged in to create a project!")
        return False
    
    owner_id = db["login"][0]
    
    project_id = generate_project_id(db["projects"]) 
    new_project = make_project(
        project_id, 
        owner_id, 
        title, 
        details, 
        target, 
        start_date, 
        end_date
    )
    db["projects"].append(new_project)
    save_data(db)
    print(f"Project '{title}' created successfully!")
    return True
    
    
def view_all_projects():
    db=load_data()
    if "projects" in db:
        all_projects = db["projects"]
    else:
        all_projects = []
        
    if len(all_projects) == 0:
        print("No projects found yet!")
        return
    
    print("\n" + "Current Projects".center(80, "="))    
    header = f"{'ID':<5} | {'Title':<15} | {'Target':<10} | {'Start':<12} | {'End':<12} | {'Owner':<5}"
    print(header)
    print("-" * len(header))
    
    for project in all_projects:
        print(f"{project['id']:<5} | "
              f"{project['title'][:15]:<15} | " 
              f"{project['target']:<10} | "
              f"{project['start_date']:<12} | "
              f"{project['end_date']:<12} | "
              f"{project['owner_id']:<5}")
    
    print("=" * 80 + "\n")
        


def edit_project(project_id):
    db=load_data()
    
    if not db["login"]:
        print("Error: You must be logged in first!")
        return
    
    current_user_id = db["login"][0]
    
    if "projects" in db:
        all_projects = db["projects"]
    else:
        print("No projects found yet!")
        return
            
    for project in all_projects:
        if project_id == project["id"]:
            if project["owner_id"] != current_user_id:
                        print("Permission Denied: You can only edit your own projects!")
                        return
            print(f"--- Editing: {project['title']} ---")
            print("1. Title | 2. Details | 3. Target | 4. Start Date | 5. End Date")
            choice = input("What would you like to change? ")
            
            if choice == "1":
                project["title"] = input("New Title: ")
            elif choice == "2":
                project["details"] = get_valid_details("New Details: ")
            elif choice == "3":
                project["target"] = get_valid_target("New Target: ")  
            elif choice == "4":
                new_start = get_valid_date("Enter new start date (YYYY-MM-DD): ")
                if validators.is_end_after_start(new_start, project["end_date"]):
                    project["start_date"] = new_start
                else:
                    print("Start date must be before the end date. Keeping original.")
                    return
            elif choice == "5":
                new_end = get_valid_date("Enter new end date (YYYY-MM-DD): ")
                if validators.is_end_after_start(project["start_date"], new_end):
                    project["end_date"] = new_end
                else:
                    print("End date must be after the start date. Keeping original.")
                    return
            
            else:
                print("Invalid Choice.")
                return
            save_data(db)
            print("Changes saved successfully!")
            return

    print(f"Error: Project ID {project_id} not found.")
        
    


def delete_project(project_id):
    db = load_data()
    
    if not db["login"]:
        print("Error: Please login first!")
        return
    
    current_user_id = db["login"][0]

    for project in db.get("projects", []):
        if project["id"] == project_id:
            
            # 3. فحص الملكية (Security Check)
            if project["owner_id"] != current_user_id:
                print("Permission Denied: You cannot delete someone else's project!")
                return

          
            confirm = input(f"Are you sure you want to delete '{project['title']}'? (y/n): ")
            if confirm.lower() == 'y':
                db["projects"].remove(project) 
                save_data(db)
                print("Project deleted successfully!")
            else:
                print("Deletion cancelled.")
            return

    print(f"Error: Project ID {project_id} not found.")