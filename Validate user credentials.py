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
