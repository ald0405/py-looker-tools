import looker_sdk
from looker_sdk import models
import pandas as pd
import os
import json
import tdqm

sdk = looker_sdk.init40()

#  Get looks
looks = sdk.all_looks()
looks_ids = [look["id"] for look in looks]
looks_data_list = []

# Wrap your dashboard_ids with tqdm for a progress bar
for look_id in tqdm(looks_ids, desc="Processing Looks"):
    looks_data = sdk.look(look_id=str(look_id))
    looks_data_list.append(looks_data)

looks_data_list[0].keys()

looks_data_list[0]["url"]

# Define a list to hold the extracted data
extracted_look_data = []

# Loop through each dashboard data item
for look_data in tqdm(looks_data_list, desc="Looks"):
    # Extract the keys of interest and create a new dictionary
    data = {
        "last_updater_id": look_data.get("last_updater_id", "N/A"),
        "user_id": look_data.get("user_id"),
        "look_title": look_data.get("title"),
        "look_url": look_data.get("public_url"),
        "last_viewed_at": look_data.get("last_viewed_at", "N/A"),
        "last_accessed_at": look_data.get("last_accessed_at", "N/A"),
        "view_count": look_data.get("view_count", "N/A"),
        "created_at": look_data.get("created_at", "N/A"),
        "is_deleted": look_data.get("deleted"),
        "folder": look_data.get("folder_id"),
    }
    # Add the new dictionary to the list
    extracted_look_data.append(data)

# Now extracted_data contains all the information you wanted from each dashboard
df_look = pd.DataFrame(extracted_look_data)
df_look.info()
