import json

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from datetime import datetime
from backend.utils import json_response
from backend.blog.models import Post
from backend.blog.post_manipulation import paragraphs_json_to_string
from backend.utils import token_required

def specific_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return json_response(post.as_dict())

def newest(request):
    post = Post.objects.all().order_by('-date')[0]
    return json_response(
        {"slug": post.slug},
        status=200
    )

@token_required
def create_post(request):
    if request.method == "POST":
        postData = json.loads(request.body)
        print(type(postData), postData)
        Post(
            title = postData['title'],
            author = postData['author'],
            date = datetime.fromtimestamp(postData['date_unix_seconds']),
            tags = ",".join(postData['tags']),
            content = paragraphs_json_to_string(postData['paragraphs'])
        ).save()
        return HttpResponse(status=200)
    
    return HttpResponse(status=405)

def posts(request):
    if request.method == "GET":
        return HttpResponse(
            content=json_response([ post.as_dict(with_content=False) for post in Post.objects.all() ]),
            content_type=None,
            status=200
        )
    elif request.method == "POST":
        return create_post(request)
