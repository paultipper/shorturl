import json


def healthcheck(event, context):
    body = {
        "message": "The Python URL shortening service is healthy!"
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "The Python URL shortening service is healthy!",
        "event": event
    }
    """
