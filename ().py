# coding: utf-8
from blog.models import Post
a = Post.objects.all()
a
b = Post.objects.filter(id = 'test - 2026-04-18 07:50:53.899255+00:00')
b = Post.objects.filter(id = 1)
b
b = Post.objects.filter(id = 5)
b
b.title = 'koni'
b
b.save()
