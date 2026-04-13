def create_user(user_id, first_name, last_name, email, password, mobile):
    return {
        "id": user_id,
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "password": password,
        "mobile": mobile
    }
    
def create_project(project_id, owner_id, title, details, target, start_date, end_date):
    return {
        "id": project_id,
        "owner_id": owner_id,
        "title": title,
        "details": details,
        "target": target,
        "start_date": start_date,
        "end_date": end_date
    }