# AdminUserManagementScript.py
is a Python script that provides a convenient way to manage user accounts through an API server. It offers functionality such as creating users, updating user information, deleting users, retrieving user information, listing all users, changing user passwords, validating user credentials, searching users by email, updating user roles, validating email uniqueness, disabling user accounts, enabling user accounts, and counting the total number of users.
Prerequisites

Before running the User Management Script, ensure that you have the following prerequisites:

    Python 3.x installed
    Required Python packages: requests (install using pip install requests)

Installation

To install and set up the User Management Script, follow these steps:

    Clone the repository or download the script files.
    Install the required Python packages by running the following command:

    pip install requests

Usage

The User Management Script can be used through the command line interface (CLI). Follow the instructions below to use the script and its functions:

    Open a terminal or command prompt.
    Navigate to the directory where the script files are located.
    Run the script using the following command:

    python user_management_script.py

Available Functions

The User Management Script provides the following functions:

    create_user(username, email, password, role): Creates a new user with the specified username, email, password, and role.

    update_user(user_id, updated_data): Updates the information of an existing user with the specified user ID. Provide the updated user data as a dictionary.

    delete_user(user_id): Deletes the user with the specified user ID.

    get_user(user_id): Retrieves and displays the information of a user with the specified user ID.

    list_users(): Retrieves and lists all the users in the system.

    change_password(user_id, new_password): Changes the password of the user with the specified user ID to the provided new password.

    validate_credentials(username, password): Validates the credentials (username and password) of a user.

    search_users_by_email(email): Searches for users with the specified email and displays their information.

    update_user_role(user_id, new_role): Updates the role of the user with the specified user ID to the provided new role.

    validate_email_uniqueness(email): Validates if the provided email is unique among the existing users.

    disable_user(user_id): Disables the user account with the specified user ID.

    enable_user(user_id): Enables the user account with the specified user ID.

    count_users(): Counts and displays the total number of users in the system.

Examples
  
Here are some examples of using the User Management Script:
create_user("john.doe", "john.doe@example.com", "password123", "user")


