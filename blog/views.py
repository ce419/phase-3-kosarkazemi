from django.http import JsonResponse
from author.models import Blog, BlogUser
from .models import Post, Comment


#3
def get_posts(request, blog_id):
    try:
        token=request.META['HTTP_X_TOKEN']
        if token is None:
            return JsonResponse(data={'status': -1, 'message' : 'no/wrong token'}, safe=False)
        logged_in_user = BlogUser.objects.get(user=request.user)
        if token != logged_in_user.token:
            return JsonResponse(data={'status': -1, 'message': 'no/wrong token'}, safe=False)

        blog = Blog.objects.filter(id=blog_id)
        if request.method == 'GET':
            lst = []
            if request.GET['count']:
                count = request.GET['count']
            else:
                count = Post.objects.filter(blog=blog).count()

            if request.GET['offset']:
                offset = request.GET['offset']
            else:
                offset = 0

            for post in Post.objects.filter(blog=blog)[offset:offset + count]:
                lst.append(post.get_map())
            return JsonResponse(data={'status': 0, 'posts': lst}, safe=False)
        else:
            return JsonResponse(data={'status': -1}, safe=False)

    except:
        return JsonResponse(data={'status': -1}, safe=False)

#4  #5
def post(request,blog_id):
    try:
        blog = Blog.objects.get(id=blog_id)

        token=request.META['HTTP_X_TOKEN']
        if token is None:
            return JsonResponse(data={'status': -1, 'message' : 'no/wrong token'}, safe=False)

        logged_in_user = BlogUser.objects.get(user=request.user)
        if token != logged_in_user.token:
            return JsonResponse(data={'status': -1, 'message': 'no/wrong token'}, safe=False)

        if request.method == 'GET':
            id=request.GET['id']
            post = Post.objects.get(id=id)
            return JsonResponse(data={'status': 0,'post': post.get_map()}, safe=False)
        if request.method == 'POST':
            post = Post()
            post.blog = blog
            post.title = request.POST['title']
            post.sum = request.POST['summary']
            post.text = request.POST['text']
            post.save()

            return JsonResponse(data={'status': 0}, safe=False)
        else:
            return JsonResponse(data={'status': -1}, safe=False)

    except:
        return JsonResponse(data={'status': -1}, safe=False)

#6
def get_comments(request, blog_id):
    try:
        token=request.META['HTTP_X_TOKEN']
        if token is None:
            return JsonResponse(data={'status': -1, 'message' : 'no/wrong token'}, safe=False)
        logged_in_user = BlogUser.objects.get(user=request.user)
        if token != logged_in_user.token:
            return JsonResponse(data={'status': -1, 'message': 'no/wrong token'}, safe=False)

        blog = Blog.objects.filter(id=blog_id)
        if request.method == 'GET':
            lst = []
            if request.GET['count']:
                count = request.GET['count']
            else:
                count = Comment.objects.filter(blog=blog).count()

            if request.GET['offset']:
                offset = request.GET['offset']
            else:
                offset = 0

            for comment in Comment.objects.filter(blog=blog)[offset:offset + count]:
                lst.append(comment.get_map())
            return JsonResponse(data={'status': 0, 'comments': lst}, safe=False)
        else:
            return JsonResponse(data={'status': -1}, safe=False)

    except:
        return JsonResponse(data={'status': -1}, safe=False)



#7
def comment(request,blog_id):
    try:
        blog = Blog.objects.get(id=blog_id)

        token=request.META['HTTP_X_TOKEN']
        if token is None:
            return JsonResponse(data={'status': -1, 'message' : 'no/wrong token'}, safe=False)

        logged_in_user = BlogUser.objects.get(user=request.user)
        if token != logged_in_user.token:
            return JsonResponse(data={'status': -1, 'message': 'no/wrong token'}, safe=False)

        if request.method == 'POST':
            comment=Comment()
            comment.post=Post.objects.get(blog=blog)
            comment.text=request.POST['text']
            comment.save()

            return JsonResponse(data={'status': 0}, safe=False)
        else:
            return JsonResponse(data={'status': -1}, safe=False)

    except:
        return JsonResponse(data={'status': -1}, safe=False)







