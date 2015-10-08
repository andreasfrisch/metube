import json

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from datetime import datetime
from backend.blog.models import Post
from backend.blog.post_manipulation import paragraphs_json_to_string

def specific_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return HttpResponse(
        content=json.dumps(post.as_dict()),
        content_type=None,
        status=200
    )


def create_post(request):
    postData = json.loads(request.body)
    print(type(postData), postData)
    Post(
        title = postData['title'],
        author = postData['author'],
        date = datetime.fromtimestamp(postData['date_unix_seconds']),
        tags = ",".join(postData['tags']),
        content = paragraphs_json_to_string(postData['paragraphs'])
    ).save()
    return HttpResponse(
        status=200
    )

def posts(request):
    if request.method == "GET":
        return HttpResponse(
            content=json.dumps([ post.as_dict(with_content=False) for post in Post.objects.all() ]),
            content_type=None,
            status=200
        )
    elif request.method == "POST":
        return create_post(request)
    