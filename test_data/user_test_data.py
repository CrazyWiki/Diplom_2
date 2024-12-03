from faker import Faker

class UserData:

    # Example of correct user data
    data_user_exist = {
        "email": 'example_user@example.com',
        "password": "SecurePass123!",
        "name": "USER"
    }
    data_user_correct = {
        "email": 'example_user_1@example.com',
        "password": "SecurePass123!",
        "name":"USER"
    }

    # Example of negative user data for invalid email
    data_user_fail = {
        "email": 'invalid_email@domain',
        "password": "WeakPass"
    }

    # Example of duplicate user data with same email
    data_user_duplicate = {
        "email": 'example_user@example.com',
        "password": "SecurePass123!",
        "name": "DuplicateUser"
    }

    # Example of missing email
    data_user_without_email = {
        "email": '',
        "password": "ValidPass123",
        "name": "MissingEmailUser"
    }

    # Example of missing password
    data_user_without_password = {
        "email": 'new_user@example.com',
        "password": "",
        "name": "MissingPasswordUser"
    }

    # Example of missing name
    data_user_without_name = {
        "email": 'test_user@example.com',
        "password": "ValidPass123!",
        "name": ""
    }

    # Example of updated user data
    data_updated = {
        "email": 'updated_user@example.com',
        "password": "NewSecurePass456!",
        "name": "UpdatedUser"
    }

    @staticmethod
    def create_random_data_user():
        faker = Faker()
        random_data = {
            "email": faker.email(),
            "password": faker.password(),
            "name": faker.name()
        }
        return random_data

