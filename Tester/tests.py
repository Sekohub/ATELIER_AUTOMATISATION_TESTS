def test_status(response):
    return response["status"] == 200


def test_content_type(response):

    content_type = response["headers"].get("Content-Type", "")

    return "application/json" in content_type


def test_radar_field(response):

    data = response["json"]

    return "radar" in data


def test_past_frames(response):

    radar = response["json"].get("radar", {})

    return "past" in radar


def test_time_type(response):

    def test_time_type(response):

    radar = response["json"].get("radar", {})
    past = radar.get("past", [])

    if not past:
        return False

    return isinstance(past[0].get("time"), int)
