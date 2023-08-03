from django.shortcuts import redirect

def check_login(view):
    def wrapper(*args, **kwargs):
        request = args[0]
        if not request.session.get('user_id'):
            return redirect('login')

        result = view(*args, **kwargs)
        return result
    return wrapper
