import string , random
from django.shortcuts import render_to_response, render, redirect
from django.template.loader import get_template
from django.template import Context, Template, RequestContext
from django.http import Http404, HttpResponse , HttpResponseRedirect ,JsonResponse
from django.contrib.auth import logout, authenticate, login
from .forms import *
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from .models import Blog , User




def main_page(request):
    return render(request, 'main_page.html', { 'user': User, })


def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')


def token_generator(size=20 , chars= (string.ascii_uppercase + string.digits)):
   return ''.join(random.choice(chars) for _ in range(size))

#1
@csrf_protect
def register_page(request):

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            registered_user = User.objects.create(std_num=form.cleaned_data['std_num'],
                                            first_name=form.cleaned_data['first_name'],
                                            last_name=form.cleaned_data['last_name'],
                                            password=form.cleaned_data['password'],
                                            email=form.cleaned_data['email'],)
            default_blog = Blog.objects.create(user_owner=registered_user)
            registered_user.blog_id = default_blog.id
            registered_user.save()
            # redirect('login_page', request) TODO
            return JsonResponse(data={'status': 0 }, safe=False )
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
#             std_num, password = form.cleaned_data.get('std_num'), form.cleaned_data.get('password')
#             user = authenticate(std_num=std_num,
#                                 password=password)
#
#             login(request, user)
#             token = token_generator()
#             loged_user = User.objects.get(std_num=std_num)
#             loged_user.token = token
#             loged_user.save()
#             return JsonResponse(data={'status': 0,'token': token}, safe=False)
#         else:
#             return JsonResponse(data={'status': -1 } , safe=False)
#     else:
#         form = LoginForm()
#
#     return render(request, 'registration/login.html', {'form': form, })

@csrf_protect
@csrf_exempt
def login_page(request):
    user = User.objects.get(std_num=request.POST['std_num'])
    return JsonResponse(data={'status': str(user) }, safe=False)
    # if request.method == 'POST':
    #     user = authenticate(request.POST)
    #     if user is not None:
    #         login(request, user)
    #         token = token_generator()
    #         loged_user = User.objects.get(std_num=request.POST['std_num'])
    #         loged_user.token = token
    #         loged_user.save()
    #         return JsonResponse(data={'status': 0,'token': token}, safe=False)
    #     else:
    #         return JsonResponse(data={'status': 2}, safe=False)
    # else:
    #     return JsonResponse(data={'status': -1}, safe=False)


#8
def blog_id_get(request):
    token=request.META.__getitem__('HTTP_X_TOKEN')
    if request.method == 'GET':
        loged_user = User.objects.get(token=token)
        bloo_id=loged_user.blog_id
        return JsonResponse(data={'status': 0,'blog_id': bloo_id}, safe=False)
    else:
        return JsonResponse(data={'status': -1}, safe=False)

