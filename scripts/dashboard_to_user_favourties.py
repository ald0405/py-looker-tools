import looker_sdk
from looker_sdk import models
import os
import json

sdk = looker_sdk.init40()

sdk.user
response_users = sdk.all_users()
def add_dashboards_to_users(dashboard_id: str, users_id: list):

  """ Add a specific dashboard to the list of favorite contents for a list of user
  
  Args: 
    dashboard_id (str): id of a Looker dashboard (https://company.looker.com/dashboards/id)
    users_id (list): a list of users in the form of a native Python list
  
  Returns: "Successfully added!" (str)
  
  Raises: N/A (does not explicitly raise an exception); Looker SDK will raise an error.
  """
 
  """ This statement is using sdk.dashboard() to retrieve content_metadata_id, 
  which is used as a parameter for sdk.create_content_favorite()""" 
  content_metadata_id = sdk.dashboard(dashboard_id=dashboard_id)['content_metadata_id'] 

  """An admin can not update the list of favorite contents for users, 
  `sdk.auth.login_user()` and `sdk.auth.logout()` are called to sudo as each user to call 
`create_content_favorite()"""
  for i in users_id: 
    sdk.auth.login_user(i)
    params = {}
    params["user_id"] = i 
    params["content_metadata_id"] = content_metadata_id
    sdk.create_content_favorite(params)
    sdk.auth.logout() 

  return (f"Successfully {sdk.dashboard(dashboard_id=dashboard_id)['title']} added!")

# You can either change the parameter directly, or upload files to Google Colab and use open() and read() to read data 
from files
add_dashboards_to_users(dashboard_id = "290", users_id = [28])

