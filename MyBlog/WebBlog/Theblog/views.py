from django.shortcuts import render,HttpResponse,redirect
from django.views.generic import ListView,DetailView
from django.views import View
from .models import Post
from .form import PostForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
def Introduce(request):
    return render(request,'Theblog/introduce.html')
class BlogList(ListView):
    model = Post
    template_name = 'Theblog/index.html'
    ordering = ['-date']

class BlogDetail(DetailView):
    model = Post
    template_name = 'Theblog/detail.html'

class BlogCreate(View):
    def get(self,request):
        form = PostForm()
        return render(request,'Theblog/create_post.html',{'form' : form})

    def post(self,request):
        form = PostForm(data = request.POST, files = request.FILES)
        if form.is_valid():
            form.save()
            return redirect('Theblog:home')

class BlogUpdate(View):
    def get(self,request,primarykey):
        p = Post.objects.get(pk = primarykey)
        form = PostForm(instance = p)
        return render(request,'Theblog/update_post.html',{'form':form,'id' : primarykey})
    def post(self,request,primarykey):
        p = Post.objects.get(pk=primarykey)
        form = PostForm(data = request.POST, files = request.FILES,instance = p)
        if form.is_valid():
            form.save()
            return redirect('Theblog:home')



class BlogDelete(View):
    def get(self,request,primarykey):
        p = Post.objects.get(pk=primarykey)
        return render(request,'Theblog/delete_post.html',{'p':p})
    def post(self,request,primarykey):
        p = Post.objects.get(pk=primarykey)
        messages.success(request,f"Bạn Vừa Xoá 1 Post Có Tiêu Đề {p.title}")
        p.delete()
        return redirect('Theblog:home')

class BlogLogin(View):
    def get(self,request):
        return render(request,'Theblog/login_post.html')
    def post(self,request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        my_user = authenticate(username=username, password=password)
        if my_user is None:
            messages.success(request,("Tài khoản hoặc mật khẩu không tồn tại"))
            return redirect('Theblog:login')
        login(request,my_user)
        return HttpResponse("Đăng nhập thành công")

