from .models import User

def get_auth_user(request):
    id = request.session.get('user_id')
    if id:
        user = User.objects.filter(pk=id)
        return user.first() if user.exists() else None
    else:
        return None

def user_context(request):
    context = {
        'auth_user': get_auth_user(request)
    }
    return context