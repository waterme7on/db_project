from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.hashers import make_password, check_password
from django.views.decorators.http import require_http_methods
from django import forms

from qqa.models.User import User
from qqa.models.Student import Student
from qqa.models.Teacher import Teacher
from qqa.models.SchoolAdmin import SchoolAdmin


class LoginForm(forms.Form):
    account = forms.CharField(max_length=30)
    password = forms.CharField(max_length=100)

@require_http_methods(["GET", "POST"])
def index(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['account'])
            print(form.cleaned_data['password'])
            try:
                user = User.objects.get(account=form.cleaned_data['account'])
            except User.DoesNotExist:
                # 登录失败, 页面提示alert 登陆失败
                message = "用户不存在! 登陆失败"
                return render(request,'common/login.html',{'form': form, 'message' : message})
                pass
            if check_password(form.cleaned_data['password'],user.password):
                request.session['account'] = user.account
                request.session['no'] = user.x_no
                request.session['character'] = user.character
                request.session.set_expiry(0) #当浏览器关闭后，用户会话 cookie 将过期。
                #返回登录成功, 重定向到相应角色的首页
                if user.character == 'student':
                    request.session['name'] = Student.objects.get(pk=user.x_no).student_name
                    return redirect('/qqa/student/courseSelect')
                elif user.character == 'teacher':
                    request.session['name'] = Teacher.objects.get(pk=user.x_no).teacher_name
                    return redirect('/qqa/teacher/index')
                else:
                    request.session['name'] = SchoolAdmin.objects.get(pk=user.x_no).admin_name
                    return redirect('/qqa/admin/courseChoose')
                #return 
                pass 
            else:
                #返回登录失败
                message = "用户密码不匹配! 登录失败"
                return render(request,'common/login.html',{'form': form, 'message' : message})
                pass
    else:
        form = LoginForm()
    return render(request,'common/login.html',{'form': form})


def register(request):
    pass

def logout(request):
    if not request.session.get('account', None):
        # 如果本来就未登录，也就没有登出一说
        return redirect('/qqa/index')
    request.session.flush()
    return redirect('/qqa/index')