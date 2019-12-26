from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.hashers import make_password, check_password
from qqa.models.User import User

def index(request):
    return render(request,'common/login.html',{})

def login(request):
    try:
        user = User.objects.get(account=request.POST['account'])
    except User.DoesNotExist:
        # 登录失败, 页面提示alert 登陆失败
        pass
    if check_password(request.POST['password'],user.password):
        request.session['user_id'] = user.user_id
        request.session['no'] = user.x_no
        request.session['character'] = user.character
        request.session.set_expiry(0) #当浏览器关闭后，用户会话 cookie 将过期。
        #返回登录成功, 重定向到相应角色的首页
        pass 
    else:
        #返回登录失败
        pass


def register(request):

    pass

def logout(request):
    try:
        request.session.flush()
    except:
        pass
    pass
        