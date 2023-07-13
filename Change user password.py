def change_password(user_id, new_password):
    url = f"{API_BASE_URL}/users/{user_id}/password"
    data = {'new_password': new_password}
    response = send_request(url, method='PUT', data=data)
    
    if response is not None and response.status_code == 200:
        print("Password changed successfully!")
    else:
        print("Failed to change password.")

