from _ast import arg
from django import template
from blog.models import Post,Comment
from blog.models import Category
register = template.Library()

@register.inclusion_tag('blog/blog-popular-post-widget.html')
def LatestPosts(arg=3):
    posts = Post.objects.filter(status=1).order_by('-published_date')[:arg]
    return {'posts': posts}
@register.inclusion_tag('blog/blog-category-widget.html')
def postcategories():
    posts = Post.objects.filter(status=1)
    categories = Category.objects.all()
    cat_dict = {}
    for name in categories:
        cat_dict[name] = posts.filter(category=name).count()
    return {'categories': cat_dict}
@register.simple_tag(name='comments_count')
def function(pid):
    return Comment.objects.filter(post=pid,approved=True).count()