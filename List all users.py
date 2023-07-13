def list_users():
    url = f"{API_BASE_URL}/users"
    response = send_request(url)
    
    if response is not None and response.status_code == 200:
        users = response.json()
        print("User List:")
        for user in users:
            print(f"Username: {user['username']}")
            print(f"Email: {user['email']}")
            print(f"Role: {user['role']}")
            print("--------------------")
    else:
        print("Failed to retrieve user list.")
