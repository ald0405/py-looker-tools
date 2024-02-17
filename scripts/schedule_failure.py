import looker_sdk
from looker_sdk import models
import os
import json
sdk = looker_sdk.init40()


def check_schedule_failures(days: int) -> dict:
    """This function prints a list of schedules that have failed in the past day.
            This has been taken from the brilliant Henry package but be re-created with
            a bit of flexibility
            Parameters:
            days (int): The number of days to look in the past.
            Returns:
            A dictionary of failed schedules, where the keys are the names of the schedules and the values are the counts
    of failures.
    """
    num_days = str(days) + " days"
    sdk = looker_sdk.init40()
    if days < 0:
        raise ValueError("days must be a non negative integer.")
    print(f"\bTest for failing schedules {days} day(s)")
    request = models.WriteQuery(
        model="i__looker",
        view="scheduled_plan",
        fields=["scheduled_job.name", "scheduled_job.count"],
        filters={
            "scheduled_job.created_date": num_days,
            "scheduled_job.status": "failure",
        },
        sorts=["scheduled_job.count desc"],
        limit=500,
    )
    failed_schedules = list()
    result = sdk.run_inline_query("json", request)
    failed_schedules = json.loads(result)
    print(json.dumps(failed_schedules, indent=4))

check_schedule_failures(days=1)
