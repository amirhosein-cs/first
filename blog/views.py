from django.shortcuts import render,get_object_or_404,redirect
from blog.forms import CommentForm
from django.contrib import messages
from blog.models import Post,Comment
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
# Create your views here.
def blog_view(request,**kwargs):
    Posts = Post.objects.filter(status=1)
    if kwargs.get('cat_name') != None:
        Posts = Posts.filter(category__name=kwargs['cat_name'])
    if kwargs.get('author_username') != None :
        Posts = Posts.filter(author__username=kwargs['author_username'])
    if kwargs.get('tag_name') != None:
        Posts = Posts.filter(tag__name__in=[kwargs['tag_name']])
    Posts = Paginator(Posts,3)
    try:
        page_number = request.GET.get('page')
        Posts = Posts.page(page_number)
    except (PageNotAnInteger,EmptyPage):
        Posts = Posts.page(1)
    context = {'Posts': Posts}
    return render(request,'blog/blog-home.html',context)

def blog_single(request,pid):
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,  "Thank you! Your message has been sent.")
            return redirect("blog:single",pid)
        else:
            messages.error(request,"Oops! Please check the form and try again.")
            return redirect("blog:single",pid)
    Posts = Post.objects.filter(status=1)
    post = get_object_or_404(Posts,pk=pid)
    comments = Comment.objects.filter(post=post.id,approved=True)
    AllPosts = list(Posts)
    Total = len(Posts)
    try:
        index = AllPosts.index(post)
    except ValueError:
        index = -1
    Prev_post = AllPosts[index-1] if index > 0 else None #اینجا رو جوری بنویس که اگه پستی موجود نبود بنویسه یا بیاره از اول template  ها رو هم درست کن
    Next_post = AllPosts[index+1] if index < (Total-1) else None #اینجا رو جوری بنویس که اگه پستی موجود نبود بنویسه یا بیاره از اول template  ها رو هم درست کن
    context = {
        'post':post,
        'Prev_post':Prev_post,
        'Next_post':Next_post,
        'AllPosts':AllPosts,
        'Total':Total,
        'Comments':comments,
        'form':form,
    }
    return render(request,'blog/blog-single.html',context)

def test(request):
    return render(request,'test.html')

def blog_category(request,cat_name):
    posts = Post.objects.filter(status=1, category__name=cat_name)
    context = {'Posts':posts}
    return render(request,'blog/blog-home.html',context)

def blog_search(request):
    Posts = Post.objects.filter(status=1)
    if request.method == 'GET':
        if s := request.GET.get('s'):
            Posts = Posts.filter(content__contains=s)
    context = {'Posts': Posts}
    return render(request,'blog/blog-home.html',context)
