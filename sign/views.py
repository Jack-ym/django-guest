from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    #return HttpResponse("Hello Django!")
    return render(request,"index.html")

#登录动作
def login_action(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user) #登录
        #if username =='admin' and password == 'admin123':
            #return HttpResponse('login success!')
            #return HttpResponseRedirect('/event_manage/')
            response = HttpResponseRedirect('/event_manage/')
            #response.set_cookie('user',username, 3600)
            #添加浏览器cookie,三个参数的意义：写入浏览器的cookie名，用户输入的用户名，cookie在浏览器的保存时间（秒）
            request.session['user'] = username #记录session到浏览器
            return response
        else:
            return render(request,'index.html',{'error':'username or password error!'})


#发布会管理
@login_required
def event_manage(request):
    #return render(request,"event_manage.html")
    #username = request.COOKIES.get('user', '') #读取浏览器cookie
    username = request.session.get('user', '')#读取浏览器session
    return render(request,"event_manage.html", {"user": username})