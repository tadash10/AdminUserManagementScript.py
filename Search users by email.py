def search_users_by_email(email):
    url = f"{API_BASE_URL}/users?email={email}"
    response = send_request(url)
    
    if response is not None and response.status_code == 200:
        users = response.json()
        if len(users) > 0:
            print(f"Users found with email '{email}':")
            for user in users:
                print(f"Username: {user['username']}")
                print(f"Email: {user['email']}")
                print(f"Role: {user['role']}")
                print("--------------------")
        else:
            print(f"No users found with email '{email}'.")
    else:
        print("Failed to search users.")
