import json
import os
import config

# Global variable to hold user data in memory after loading
_user_data = {}

def load_user_data():
    """Loads user data from the JSON file, or sets defaults."""
    global _user_data
    if os.path.exists(config.USER_DATA_FILE):
        try:
            with open(config.USER_DATA_FILE, 'r', encoding='utf-8') as f:
                _user_data = json.load(f)
            print(f"Loaded user data from {config.USER_DATA_FILE}")
        except json.JSONDecodeError:
            print(f"Error decoding JSON from {config.USER_DATA_FILE}. Starting with default data.")
            _user_data = {}
        except Exception as e:
            print(f"Unexpected error: {e}. Starting with default data.")
            _user_data = {}
    else:
        print(f"User data file {config.USER_DATA_FILE} not found. Creating with default values.")
        _user_data = {}

    # Ensure required fields exist
    if "assistant_name" not in _user_data:
        _user_data["assistant_name"] = "Nova"
    if "creator_name" not in _user_data:
        _user_data["creator_name"] = "Neha Giri Goswami"

    save_user_data(_user_data)
    return _user_data

def save_user_data(data):
    """Saves user data to the JSON file."""
    try:
        with open(config.USER_DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)
        print(f"Saved user data to {config.USER_DATA_FILE}")
    except Exception as e:
        print(f"Error saving user data: {e}")

def update_user_profile(key, value):
    """Updates a key-value pair in the user profile."""
    global _user_data
    _user_data[key] = value
    save_user_data(_user_data)
    print(f"User profile updated: {key} = {value}")

def get_user_profile(key, default=None):
    """Gets a user profile value."""
    return _user_data.get(key, default)

# Load on import
load_user_data()
