from .models import User

def get_auth_user(request):
    id = request.session.get('user_id')
    if id:
        user = User.objects.filter(pk=id)
        return user.first() if user.exists() else None
    else:
        return None

def get_url_name(request):
    url_name = request.resolver_match.url_name
    return url_name if url_name else None

def user_context(request):
    context = {
        'auth_user': get_auth_user(request),
        'url_name': get_url_name(request)
    }
    return context