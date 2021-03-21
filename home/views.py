from django.shortcuts import render
from django.template import loader
from features.models import Members
from .forms import UserLogin,UserReg
from django.contrib import auth
from django.contrib.auth import authenticate,login
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views import View
# Create your views here.
def index(request):
    return render(request,'features/home.html')

def home(request):
    return render(request,'features/home.html')

class Register(View):


    def get(self, request):
        return render(request, "features/register.html")

    def post(self,request):
        postData = request.POST
        username = postData.get('uname')
        email = postData.get('email')
        password = postData.get('psw')


        # validation
        value = {'username': username, 'email': email}
        member = Members(username=username, email=email, password=password)
        err_msg = self.validateMember(member)

        # saving
        if not err_msg:
            member.password = make_password(member.password)
            member.register()
            request.session['username'] = member.username
            request.session['member'] = member.id
            return redirect('home')
        else:
            data = {'error': err_msg, 'values': value}
            return render(request, "register.html",data)

    def validateMember(self,member):
        err_msg = None
        if (not member.username):
            err_msg = "Name Required!"
        elif not member.validateEmail():
            err_msg = 'Enter valid email'
        elif not member.password:
            err_msg = "please create a password"
        elif len(member.password) < 6:
            err_msg = "Password must be 6 char long"
        elif member.doExists():
            err_msg = 'Email Address Already registered..'
        return err_msg


class Login(View):
    def get(self, request):
        Login.return_url = request.GET.get('return_url')
        return render(request, "login.html")

    def post(self, request):

        username = request.POST.get('uname')
        password = request.POST.get('psw')
        member = Members.get_member_by_uname(username)
        print(username,password)
        print(member)
        err_msg = None
        if member:
            print(member.password)
            flag = check_password(password, member.password)
            print(flag)
            if flag:
                request.session['username'] = member.username
                request.session['member'] = member.id
                if Login.return_url:
                    return HttpResponseRedirect(Login.return_url)
                else:

                    Login.return_url = None
                    return redirect('home')
            else:
                err_msg = 'Username or Password invalid1'
        else:
            err_msg = 'Username or Password invalid2'
        return render(request, 'login.html', {'error': err_msg})


def logout(request):
    request.session.clear()
    return redirect('index')

