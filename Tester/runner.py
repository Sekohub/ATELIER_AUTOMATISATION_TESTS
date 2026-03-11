from tester.client import call_api
from tester.tests import *

def run():

    response = call_api()

    results = {
        "status": response["status"],
        "latency": response["latency"],
        "test_status": test_status(response),
        "test_radar": test_radar_exists(response),
        "test_frames": test_past_frames(response),
        "test_time": test_time_field(response)
    }

    return results
