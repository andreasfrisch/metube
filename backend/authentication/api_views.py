import json

from django.contrib import auth
from django.http import HttpResponse
from backend.auth.models import Token
from backend.utils import json_response, token_required

def login(request):
    if request.method == 'POST':
        print("GOT A POST")
        print(">> body: %s" % request.body)
        print(">> POST: %s" % request.POST)
        parsed_body = json.loads(request.body)
        print("parsed that shit")
        username = parsed_body["username"]
        password = parsed_body["password"]

        print("read that shit")
        if username is not None and password is not None:
            print("authenticating")
            try:
                user = auth.authenticate(username=username, password=password)
            except Exception as e:
                print(e)
            print("authenticated that shit")
            if user is not None:
                if user.is_active:
                    try:
                        token, created = Token.objects.get_or_create(user=user)
                        return json_response({
                            'token': token.token,
                            'username': user.username
                        })
                    except Exception as e:
                        print(e)
                else:
                    print("invalid user")
                    return json_response({
                        'error': 'Invalid User'
                    }, status=400)
            else:
                print("invalid username/password")
                return json_response({
                    'error': 'Invalid Username/Password'
                }, status=400)
        else:
            print("invalid data")
            return json_response({
                'error': 'Invalid Data'
            }, status=400)
    elif request.method == 'OPTIONS':
        return json_response({})
    else:
        return json_response({
            'error': 'Invalid Method'
        }, status=405)

@token_required
def logout(request):
    if request.method == 'POST':
        request.token.delete()
        return json_response({
            'status': 'success'
        })
    elif request.method == 'OPTIONS':
        return json_response({})
    else:
        return json_response({
            'error': 'Invalid Method'
        }, status=405)
        
@token_required
def verify(request):
    return HttpResponse(status=200)