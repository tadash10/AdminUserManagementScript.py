def disable_user(user_id):
    url = f"{API_BASE_URL}/users/{user_id}/disable"
    response = send_request(url, method='PUT')
    
    if response is not None and response.status_code == 200:
        print("User account disabled successfully!")
    else:
        print("Failed to disable user account.")
