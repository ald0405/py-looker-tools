
import pandas as pd
import looker_sdk 
from looker_sdk import models

def get_users() -> pd.DataFrame:
    """
    Fetch all users from Looker instance.

    This function retrieves all users from the Looker instance using the Looker SDK.
    It then processes the user data and returns a pandas DataFrame containing information
    about each user.

    Returns:
        pandas.DataFrame: A DataFrame with the following columns:
            - 'looker_user_id': The unique identifier for each Looker user.
            - 'first_name': The first name of the user.
            - 'last_name': The last name of the user.
            - 'email': The email address of the user.
            - 'roles': A comma-separated string listing the role IDs assigned to the user.
            - 'groups': A comma-separated string listing the group IDs the user belongs to.
            - 'is_disabled': A boolean indicating whether the user account is disabled.

    Example:
        >>> df = get_users()
"""
    
    # Prepare data for DataFrame
    data = []

        # Fetch all users
    users = sdk.all_users()
    for user in users:
        user_data = {
            'looker_user_id': user.id,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
            'roles': ', '.join(map(str, user.role_ids)),
            'groups': ', '.join(map(str, user.group_ids)),
            'is_disabled' : user.is_disabled,
        }
        data.append(user_data)

    # Create a pandas DataFrame
    df = pd.DataFrame(data)
    
    return df
