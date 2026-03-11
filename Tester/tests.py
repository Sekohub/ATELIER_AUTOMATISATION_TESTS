def test_status(response):
    return response["status"] == 200


def test_radar_exists(response):

    data = response["json"]

    return "radar" in data


def test_past_frames(response):

    radar = response["json"]["radar"]

    return "past" in radar and len(radar["past"]) > 0


def test_time_field(response):

    frame = response["json"]["radar"]["past"][0]

    return "time" in frame
