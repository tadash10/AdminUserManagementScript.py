def count_users():
    url = f"{API_BASE_URL}/users/count"
    response = send_request(url)
    
    if response is not None and response.status_code == 200:
        count_result = response.json()
        total_users = count_result['count']
        print(f"Total number of users: {total_users}")
    else:
        print("Failed to count users.")
