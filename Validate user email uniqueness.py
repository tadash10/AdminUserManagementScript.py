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
