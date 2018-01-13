from django.shortcuts import redirect

class FinishProfileMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user and \
        request.user.is_authenticated and \
        request.user.bio == None or \
        request.user.industry == None or \
        request.user.current_job == None or \
        request.user.desired_job == None:
            return redirect('accounts:finish-profile')

        return self.get_response(request)
