from django.shortcuts import render_to_response
from django.template.loader import get_template
from django.template import Context, Template, RequestContext
from .models import User, Blog
from django.http import Http404, HttpResponse , HttpResponseRedirect ,JsonResponse
from django.contrib.auth import logout, authenticate, login
from .forms import *




def main_page(request):
    template = get_template('main_page.html')
    variables = Context({ 'user': request.user })
    output = template.render(variables)
    return HttpResponse(output)


def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')

#1
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
            return JsonResponse(data={'status': 0 }, safe=False) #TODO ?? redirect('post_detail', pk=post.pk)
    else:
        form = RegisterForm()
        # variables = RequestContext(request, {'form': form})
    return JsonResponse(data={'status': -1 }, safe=False) #render_to_response('registration/register.html',variables)


#2
def login_page(request):
    if request.method == 'POST':
        print(request.POST)
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username, password = form.cleaned_data.get('username'), form.cleaned_data.get('password')
            user = authenticate(username=username,
                                password=password)

            login(request, user)
            token = 1#token_generator.make_token(user) #TODO
            loged_user = User.objects.get(username=username)
            loged_user.token = token
            loged_user.save()
            return JsonResponse(data={'status': 0,
                                      'token': token}, safe=False)
    else:
        return JsonResponse(data={'status': -1 } , safe=False)