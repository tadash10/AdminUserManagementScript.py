

import requests

API_BASE_URL = "https://api.example.com"  # Replace with your API server's base URL

# Utility function to send API requests with authentication headers
def send_request(url, method='GET', data=None):
    headers = {
        'Authorization': 'Bearer <access_token>',  # Replace with your authentication token
        'Content-Type': 'application/json'
    }
    
    try:
        response = requests.request(method, url, json=data, headers=headers)
        response.raise_for_status()  # Raise an exception for non-2xx status codes
        return response
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return None

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
    
    if response is not None and response.status_code == 201:
        print("User created successfully!")
    else:
        print("Failed to create user.")

# User update function
def update_user(user_id, updated_data):
    url = f"{API_BASE_URL}/users/{user_id}"
    response = send_request(url, method='PUT', data=updated_data)
    
    if response is not None and response.status_code == 200:
        print("User updated successfully!")
    else:
        print("Failed to update user.")

# User deletion function
def delete_user(user_id):
    url = f"{API_BASE_URL}/users/{user_id}"
    response = send_request(url, method='DELETE')
    
    if response is not None and response.status_code == 204:
        print("User deleted successfully!")
    else:
        print("Failed to delete user.")

# Retrieve user information by ID
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

# List all users
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

# Change user password
def change_password(user_id, new_password):
    url = f"{API_BASE_URL}/users/{user_id}/password"
    data = {'new_password': new_password}
    response = send_request(url, method='PUT', data=data)
    
    if response is not None and response.status_code == 200:
        print("Password changed successfully!")
    else:
        print("Failed to change password.")

# Validate user credentials
def validate_credentials(username, password):
    url = f"{API_BASE_URL}/users/validate"
    data = {'username': username, 'password': password}
    response = send_request(url, method='POST', data=data)
    
    if response is not None and response.status_code == 200:
        validation_result = response.json()
        if validation_result['valid']:
            print("Credentials are valid.")
        else:
            print("Credentials are invalid.")
    else:
        print("Failed to validate credentials.")

# Search users by email
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

# Update user roles
def update_user_role(user_id, new_role):
    url = f"{API_BASE_URL}/users/{user_id}/role"
    data = {'role': new_role}
    response = send_request(url, method='PUT', data=data)
    
    if response is not None and response.status_code == 200:
        print("User role updated successfully!")
    else:
        print("Failed to update user role.")

# Validate user email uniqueness
def validate_email_uniqueness(email):
    url = f"{API_BASE_URL}/users/validate-email"
    data = {'email': email}
    response = send_request(url, method='POST', data=data)
    
    if response is not None and response.status_code == 200:
        validation_result = response.json()
        if validation_result['unique']:
            print("Email is unique.")
        else:
            print("Email is not unique.")
    else:
        print("Failed to validate email uniqueness.")

# Disable user account
def disable_user(user_id):
    url = f"{API_BASE_URL}/users/{user_id}/disable"
    response = send_request(url, method='PUT')
    
    if response is not None and response.status_code == 200:
        print("User account disabled successfully!")
    else:
        print("Failed to disable user account.")

# Enable user account
def enable_user(user_id):
    url = f"{API_BASE_URL}/users/{user_id}/enable"
    response = send_request(url, method='PUT')
    
    if response is not None and response.status_code == 200:
        print("User account enabled successfully!")
    else:
        print("Failed to enable user account.")

# Count total number of users
def count_users():
    url = f"{API_BASE_URL}/users/count"
    response = send_request(url)
    
    if response is not None and response.status_code == 200:
        count_result = response.json()
        total_users = count_result['count']
        print(f"Total number of users: {total_users}")
    else:
        print("Failed to count users.")

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

    # Retrieving user information
    user_id = 456  # Replace with the actual user ID
    get_user(user_id)

    # Listing all users
    list_users()

    # Changing user password
    user_id = 789  # Replace with the actual user ID
    new_password = "newpassword123"
    change_password(user_id, new_password)

    # Validating user credentials
    username = "johndoe"
    password = "password123"
    validate_credentials(username, password)

    # Searching users by email
    search_email = "john.doe@example.com"
    search_users_by_email(search_email)

    # Updating user role
    user_id = 123  # Replace with the actual user ID
    new_role = "editor"
    update_user_role(user_id, new_role)

    # Validating email uniqueness
    email = "test@example.com"
    validate_email_uniqueness(email)

    # Disabling user account
    user_id = 123  # Replace with the actual user ID
    disable_user(user_id)

    # Enabling user account
    user_id = 123  # Replace with the actual user ID
    enable_user(user_id)

    # Counting total number of users
    count_users()

if __name__ == '__main__':
    main()
