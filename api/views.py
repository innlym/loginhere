from django.http import HttpResponse
from oauth2_provider.decorators import protected_resource
from oauth2_provider.models import AccessToken
import simplejson as json


@protected_resource(scopes=['read'])
def user(request):
    token = request.META['HTTP_AUTHORIZATION'].split(' ')[1]
    user = AccessToken.objects.get(token=token).user
    data = json.dumps({
        'username':user.username,
        'nickname': user.nickname,
        'realname': user.realname,
        'gender': user.gender,
        'email': user.email,
        'mobile': user.mobile,
        'birthday': user.birthday and user.birthday.strftime("%Y-%m-%d"),
        'mydesc': user.mydesc,
        })
    return HttpResponse(data)
