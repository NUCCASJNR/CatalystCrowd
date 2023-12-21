# middleware.py

from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required


class NextMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        if view_func.__name__ == 'login' and 'next' in request.GET:
            # Store the 'next' parameter in the session
            request.session['next'] = request.GET['next']

        return None

    def process_template_response(self, request, response):
        # Check if the user is authenticated and if there's a stored 'next' parameter
        if request.user.is_authenticated and 'next' in request.session:
            # Get the stored 'next' parameter and remove it from the session
            next_url = request.session.pop('next')
            # Redirect the user to the stored 'next' URL
            return redirect(next_url)

        return response
