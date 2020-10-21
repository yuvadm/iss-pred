def chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i : i + n]


def seconds_to_minutes(secs):
    return f"{secs // 60}:{secs % 60:02}"


def normalize_lat_lng(lat, lng):
    if lat[0] not in "NS" or lng[0] not in "EW":
        raise Exception("Lat/lng must be formatted as N12.345 and E67.890")
    nlat = float(lat[1:]) * (-1 if lat[0] == "S" else 1)
    nlng = float(lng[1:]) * (-1 if lng[0] == "W" else 1)
    return nlat, nlng


def display_lat_lng(lat, lng):
    dlat = str(abs(lat)) + "°" + ("N" if lat > 0 else "S")
    dlng = str(abs(lng)) + "°" + ("E" if lng > 0 else "W")
    return dlat, dlng


def deg_to_cardinal(deg):
    cardinals = [
        "N",
        "NNE",
        "NE",
        "ENE",
        "E",
        "ESE",
        "SE",
        "SSE",
        "S",
        "SSW",
        "SW",
        "WSW",
        "W",
        "WNW",
        "NW",
        "NNW",
    ]
    n = len(cardinals)
    degs = 360 / n
    return cardinals[round((deg % 360) / degs) % n]


class Location(object):
    def __init__(self, lat, lng):
        self.lat = lat
        self.lng = lng

    @classmethod
    def from_labelled(cls, lat, lng):
        if lat[0] not in "NS" or lng[0] not in "EW":
            raise Exception("Lat/lng must be formatted as N12.345 and E67.890")
        nlat = float(lat[1:]) * (-1 if lat[0] == "S" else 1)
        nlng = float(lng[1:]) * (-1 if lng[0] == "W" else 1)
        return cls(nlat, nlng)
