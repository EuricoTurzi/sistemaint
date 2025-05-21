
class PermissionDebugMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if response.status_code == 403:
            print(f"User: {request.user}")
            print(f"Permissions: {request.user.get_all_permissions()}")
        return response