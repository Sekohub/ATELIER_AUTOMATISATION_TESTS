import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from Tester.client import call_api
from Tester.tests import *
from storage import save_run, init_db 

def run():
    print("RUN OK")
    init_db()

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

    save_run(response["status"], response["latency"])

    return results

if __name__ == "__main__":
    run()
