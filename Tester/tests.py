def test_status(response):
    return response["status"] == 200


def test_content_type(response):

    content_type = response["headers"].get("Content-Type", "")

    return "application/json" in content_type


def test_radar_field(response):

    data = response["json"]

    return "radar" in data


def test_past_frames(response):

    return "past" in response["json"]["radar"]


def test_time_type(response):

    frame = response["json"]["radar"]["past"][0]

    return isinstance(frame["time"], int)
