import rest_framework_simplejwt
from rest_framework_simplejwt import authentication
from Credy.views import increment_counter


class JWTAuthMiddleware():
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        increment_counter()

        try:
            user = authentication.JWTAuthentication().authenticate(request)
            if user:
                request.user = user
        except rest_framework_simplejwt.exceptions.InvalidToken:
            pass
