import binascii
from django.shortcuts import render_to_response, render, redirect
from django.template.loader import get_template
from django.template import Context, Template, RequestContext
from .models import User, Blog
from django.http import Http404, HttpResponse , HttpResponseRedirect ,JsonResponse
from django.contrib.auth import logout, authenticate, login
from .forms import *
from django.views.decorators.csrf import csrf_protect





def main_page(request):
    template = get_template('main_page.html')
    variables = Context({ 'user': request.user })
    output = template.render(variables)
    return HttpResponse(output)


def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')

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
                                            email=form.cleaned_data['email'])
            registered_user.save()
            # redirect('login_page', request) TODO
            return JsonResponse(data={'status': 0 }, safe=False )
        else:
            return JsonResponse(data={'status': -1 } , safe=False)

    else:
        form = RegisterForm()

    return render(request, 'registration/register.html', {'form': form,})

# binascii.hexlify(User)

#2
def login_page(request):
    if request.method == 'POST':
        print(request.POST)
        form = LoginForm(request.POST)
        if form.is_valid():
            std_num, password = form.cleaned_data.get('std_num'), form.cleaned_data.get('password')
            user = authenticate(std_num=std_num,
                                password=password)

            login(request, user)
            token = 1  #token_generator.make_token(user) #TODO
            loged_user = User.objects.get(std_num=std_num)
            loged_user.token = token
            loged_user.save()
            return JsonResponse(data={'status': 0,'token': token}, safe=False)
        else:
            return JsonResponse(data={'status': -1 } , safe=False)
    else:
        form = LoginForm()

    return render(request, 'registration/login.html', {'form': form, })