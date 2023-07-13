def get_user(user_id):
    url = f"{API_BASE_URL}/users/{user_id}"
    response = send_request(url)
    
    if response is not None and response.status_code == 200:
        user_data = response.json()
        print("User information:")
        print(f"Username: {user_data['username']}")
        print(f"Email: {user_data['email']}")
        print(f"Role: {user_data['role']}")
    else:
        print("Failed to retrieve user information.")
