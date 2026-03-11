from tester.client import call_api
from tester.tests import *

def run():

    response = call_api()

    results = {
        "status": response["status"],
        "latency": response["latency"],
        "status_test": test_status(response),
        "content_type_test": test_content_type(response),
        "radar_test": test_radar_field(response),
        "frames_test": test_past_frames(response),
        "time_test": test_time_type(response)
    }

    return results
