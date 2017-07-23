import string , random
from django.shortcuts import  render
from django.http import HttpResponseRedirect ,JsonResponse
from django.contrib.auth import logout, authenticate, login
from .forms import *
from django.views.decorators.csrf import csrf_exempt
from .models import *
import re



def main_page(request):
    return render(request, 'main_page.html')


def logout_page(request):
    user = request.user
    logged_in_user = BlogUser.objects.filter(user=user)
    logged_in_user.token = None
    # logged_in_user.save()
    logout(request)
    return render(request, 'P2/login.html')


def token_generator(size=20 , chars= (string.ascii_uppercase + string.digits)):
   return ''.join(random.choice(chars) for _ in range(size))

#1
# @csrf_protect
def register_page(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(username=form.cleaned_data['username'], email=form.cleaned_data['email'])
            user.set_password(form.cleaned_data['password'])
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.is_staff = True
            user.save()

            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])

            registered_user = BlogUser()
            registered_user.user = user

            default_blog = Blog()
            default_blog.save()

            registered_user.blog_id = default_blog.id
            registered_user.save()

            default_blog.owner = registered_user
            default_blog.title = str(str(registered_user['first_name']+' '+str(registered_user['first_name'])+' \'s first blog!'))
            default_blog.save()

            login(request, user)
            return render(request, 'P2/login.html') #JsonResponse(data={'status': 0}, safe=False )
        else:
            return JsonResponse(data={'status': -1 } , safe=False)

    else:
        form = RegisterForm()

    return render(request, 'registration/register.html', {'form': form,})

#2
@csrf_exempt
def login_page(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            token = token_generator()
            logged_in_user = BlogUser.objects.get(user=user)
            logged_in_user.token = token
            logged_in_user.save()
            return JsonResponse(data={'status': 0,'token': token}, safe=False)
        else:
            return JsonResponse(data={'status': -1}, safe=False)
    else:
        return JsonResponse(data={'status': -1}, safe=False)


#8
def blog_id_get(request):
    token=request.META.__getitem__('HTTP_MYTOKEN') ##'HTTP_X_TOKEN']
    if request.method == 'GET':
        logged_in_user = BlogUser.objects.get(token=token)
        blog_id=logged_in_user.blog_id
        return JsonResponse(data={'status': 0,'blog_id': blog_id}, safe=False)
    else:
        return JsonResponse(data={'status': -1}, safe=False)







###########################################Celery


@csrf_exempt
def search(request):

    if request.method == 'POST':
        words=request.POST['q']
        searchReg = re.compile('^(\w+\s+){1,9}\w+(\s)*$')
        if bool(re.search( searchReg , words )):
            WS = WordsString()
            blogs = WS.search_blogs(words)
            blogsStr = blog_box(blogs)
            print(blogsStr)
            return render(request, 'results.html', {'blogsStr': blogsStr, 'words': words})
        else:
            return render(request , 'search.html', {'msg': 'Please enter 2-10 words in acceptable format \n (For example: mall ball tall)' ,})
    else:
        print('get!!!!!')
        return render(request, 'search.html' , {'msg': None, })



def blog_box(blogs):
    blogBox = []
    for item in blogs:
        if int(item[1]) > 0 :
            bs = str(str(item[0].id) +"-          "+str(item[0].title)+"-score:"+str(item[1]))
            blogBox.append(bs)
    return blogBox



################################################static

def login_page_static(request):
    return render(request, 'P2/login.html')



def blog_by_id(request,blog_id):
    return render(request, 'P2/Blog.html', {'blog_id': blog_id})


def write_post(request,blog_id):
    return render(request, 'P2/writePost.html', {'blog_id': blog_id})

def blog_more(request,blog_id):
    return render(request, 'P2/Blog-more.html', {'blog_id': blog_id})
