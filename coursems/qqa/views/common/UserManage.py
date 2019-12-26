from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.hashers import make_password, check_password
from django.views.decorators.http import require_http_methods
from qqa.models.User import User
from django import forms

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
                request.session['no'] = user.x_no
                request.session['character'] = user.character
                request.session.set_expiry(0) #当浏览器关闭后，用户会话 cookie 将过期。
                #返回登录成功, 重定向到相应角色的首页
                if user.character == 'student':
                    return redirect('/qqa/student/index')
                elif user.character == 'teacher':
                    return redirect('/qqa/teacher/index')
                else:
                    return redirect('/qqa/admin/index')
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
    try:
        request.session.flush()
    except:
        pass
    pass
        