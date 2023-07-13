import requests

API_BASE_URL = "https://api.example.com"  # Replace with your API server's base URL

# Utility function to send API requests with authentication headers
def send_request(url, method='GET', data=None):
    headers = {
        'Authorization': 'Bearer <access_token>',  # Replace with your authentication token
        'Content-Type': 'application/json'
    }
    
    if method == 'GET':
        response = requests.get(url, headers=headers)
    elif method == 'POST':
        response = requests.post(url, json=data, headers=headers)
    elif method == 'PUT':
        response = requests.put(url, json=data, headers=headers)
    elif method == 'DELETE':
        response = requests.delete(url, headers=headers)
    else:
        raise ValueError(f"Unsupported HTTP method: {method}")
    
    return response

# User creation function
def create_user(username, email, password, role):
    user_data = {
        'username': username,
        'email': email,
        'password': password,
        'role': role
    }
    url = f"{API_BASE_URL}/users"
    response = send_request(url, method='POST', data=user_data)
    
    if response.status_code == 201:
        print("User created successfully!")
    else:
        print("Failed to create user.")

# User update function
def update_user(user_id, updated_data):
    url = f"{API_BASE_URL}/users/{user_id}"
    response = send_request(url, method='PUT', data=updated_data)
    
    if response.status_code == 200:
        print("User updated successfully!")
    else:
        print("Failed to update user.")

# User deletion function
def delete_user(user_id):
    url = f"{API_BASE_URL}/users/{user_id}"
    response = send_request(url, method='DELETE')
    
    if response.status_code == 204:
        print("User deleted successfully!")
    else:
        print("Failed to delete user.")

# Usage example
def main():
    # Creating a new user
    create_user("john.doe", "john.doe@example.com", "password123", "user")

    # Updating an existing user
    user_id = 123  # Replace with the actual user ID
    updated_data = {
        'email': 'updated_email@example.com',
        'role': 'admin'
    }
    update_user(user_id, updated_data)

    # Deleting a user
    user_id = 123  # Replace with the actual user ID
    delete_user(user_id)

if __name__ == '__main__':
    main()
