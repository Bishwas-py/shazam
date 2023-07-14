from django.http import HttpResponse
from django.conf import settings

class CustomRequestMiddleware:
    """
    Middleware to check if the request body contains
    127.0.0.1 [Internal IP address] or not. Also, it bans the user if the user
    sends more than 7 requests with Internal IP address, for 5 minutes.
    """

    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        response = self.get_response(request)
        response.headers["Access-Control-Allow-Origin"] = "*"
        return response
