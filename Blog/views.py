from django.shortcuts import render, redirect, reverse
from .models import Post, BlogUser
from .forms import PostForm, BlogUserForm


# Create your views here.

def posts(request):
    queryset = Post.objects.all()
    context = {"posts": queryset}
    return render(request, "posts.html", context=context)


def add_post(request):
    context = {"form": PostForm}
    if request.method == "POST":
        form_data = PostForm(data=request.POST, files=request.FILES)
        if form_data.is_valid():
            post = form_data.save(commit=False)
            post.user_id = request.user.id
            post.save()
            return redirect('posts')
        else:
            return render(request, "add_post.html", context=context)
    else:
        return render(request, "add_post.html", context=context)


def blocked_users(request):
    queryset = BlogUser.objects.filter(user=request.user)
    context = {"users": queryset, "form": BlogUserForm}
    if request.method == "POST":
        form_data = BlogUserForm(data=request.POST, files=request.FILES)
        if form_data.is_valid():
            user = form_data.save(commit=False)
            user.user = request.user
            user.save()
            return redirect('blocked_users')
        else:
            return render(request, "blocked_users.html", context=context)
    else:
        return render(request, "blocked_users.html", context=context)


def profile(request):
    queryset = BlogUser.objects.filter(user=request.user)
    post_by_user = Post.objects.filter(author__user=request.user)
    context = {"user": queryset, "form": BlogUserForm, "posts": post_by_user}
    return render(request, "profile.html", context=context)
