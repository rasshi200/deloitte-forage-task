import datetime

def convertFromFormat1(jsonObject):
    locationParts = jsonObject["location"].split("/")

    dt = datetime.datetime.strptime(
        jsonObject["timestamp"],
        "%Y-%m-%dT%H:%M:%S.%fZ"
    )

    return {
        "deviceID": jsonObject["deviceID"],
        "deviceType": jsonObject["deviceType"],
        "timestamp": int(dt.timestamp() * 1000),
        "location": {
            "country": locationParts[0],
            "city": locationParts[1],
            "area": locationParts[2],
            "factory": locationParts[3],
            "section": locationParts[4]
        },
        "data": jsonObject["data"]
    }


def convertFromFormat2(jsonObject):
    return {
        "deviceID": jsonObject["deviceID"],
        "deviceType": jsonObject["deviceType"],
        "timestamp": jsonObject["timestamp"],
        "location": jsonObject["location"],
        "data": jsonObject["data"]
    }


def main(jsonObject):
    if isinstance(jsonObject["location"], dict):
        return convertFromFormat2(jsonObject)
    return convertFromFormat1(jsonObject)
