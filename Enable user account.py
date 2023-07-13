def enable_user(user_id):
    url = f"{API_BASE_URL}/users/{user_id}/enable"
    response = send_request(url, method='PUT')
    
    if response is not None and response.status_code == 200:
        print("User account enabled successfully!")
    else:
        print("Failed to enable user account.")
