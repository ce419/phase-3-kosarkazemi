import string , random
from django.shortcuts import render_to_response, render, redirect
from django.template.loader import get_template
from django.template import Context, Template, RequestContext
from django.http import Http404, HttpResponse , HttpResponseRedirect ,JsonResponse
from django.contrib.auth import logout, authenticate, login
from .forms import *
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.contrib.auth.models import User
from .models import Blog , BlogUser




def main_page(request):
    return render(request, 'main_page.html')


def logout_page(request):
    user = request.user
    logged_in_user = BlogUser.objects.filter(user=user)
    logged_in_user.token = None
    logged_in_user.save()

    logout(request)
    return HttpResponseRedirect('/')


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
            default_blog.save()

            login(request, user)
            # redirect('login_page', request) TODO
            return JsonResponse(data={'status': 0}, safe=False )
        else:
            return JsonResponse(data={'status': -1 } , safe=False)

    else:
        form = RegisterForm()

    return render(request, 'registration/register.html', {'form': form,})


#2
# def login_page(request):
#     if request.method == 'POST':
#         print(request.POST)
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             username, password = form.cleaned_data.get('username'), form.cleaned_data.get('password')
#             user = authenticate(username=username,
#                                 password=password)
#
#             login(request, user)
#             token = token_generator()
#             loged_user = User.objects.get(username=username)
#             loged_user.token = token
#             loged_user.save()
#             return JsonResponse(data={'status': 0,'token': token}, safe=False)
#         else:
#             return JsonResponse(data={'status': -1 } , safe=False)
#     else:
#         form = LoginForm()
#
#     return render(request, 'registration/login.html', {'form': form, })

@csrf_exempt
def login_page(request):
    # user = authenticate(username=request.POST['username'] , password=request.POST['password'])
    # if user is None:
    #     print('ridim')
    # else:
    #     print('naridim')
    # user = authenticate(username="man" , password='12345678')
    # i= request.POST['password']
    # user = User.objects.get(password=i)
    # return JsonResponse(data={'status': str(user) }, safe=False)
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
            return JsonResponse(data={'status': 2}, safe=False)
    else:
        return JsonResponse(data={'status': -1}, safe=False)


#8
def blog_id_get(request):
    token=request.META.__getitem__('HTTP_X_TOKEN')
    if request.method == 'GET':
        logged_in_user = BlogUser.objects.get(token=token)
        blog_id=logged_in_user.blog_id
        return JsonResponse(data={'status': 0,'blog_id': blog_id}, safe=False)
    else:
        return JsonResponse(data={'status': -1}, safe=False)

