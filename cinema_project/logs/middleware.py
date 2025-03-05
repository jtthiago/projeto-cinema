from .models import ActionLog

class ActionLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if request.user.is_authenticated and request.method in ['POST', 'PUT', 'DELETE']:
            action = f"{request.method} {request.path}"
            ActionLog.objects.create(user=request.user, action=action)

        return response
        
        