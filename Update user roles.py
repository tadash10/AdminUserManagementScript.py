def update_user_role(user_id, new_role):
    url = f"{API_BASE_URL}/users/{user_id}/role"
    data = {'role': new_role}
    response = send_request(url, method='PUT', data=data)
    
    if response is not None and response.status_code == 200:
        print("User role updated successfully!")
    else:
        print("Failed to update user role.")
