from logging import exception
from django.shortcuts import render
from .models import blogpost
import json
# Create your views here.
from django.http import HttpResponse
def index (request):
    post_id = blogpost.objects.values('post_id')
    post_titles = blogpost.objects.values('post_title')
    total = len(post_id)
    post_dates = blogpost.objects.values('post_dateTime')
    author_names = blogpost.objects.values('author_name')
    post_headings1 =  blogpost.objects.values('post_heading1')
    post_headings2 = blogpost.objects.values('post_heading2')
    post_headings3 = blogpost.objects.values('post_heading3')
    post_contents1 = blogpost.objects.values('post_content1')
    post_contents2 = blogpost.objects.values('post_content2')
    post_contents3 = blogpost.objects.values('post_content3')
    post_thumbnails = blogpost.objects.values('post_thumbnail')
    print(post_titles)
    post_data = {'range':range(2,total),'post_id': post_id,'titles':post_titles,'auth_names':author_names,'post_dates':post_dates,'thumbnails':post_thumbnails,
                'post_headings1':post_headings1,'post_headings2':post_headings2,'post_headings3':post_headings3,'post_contents1':post_contents1,
                'post_contents2':post_contents2,'post_contents3':post_contents3}
    return render(request, 'blog/index.html', post_data)
def blogpost_page(request,postid):
    show_post = blogpost.objects.filter(post_id = postid)
    older = show_post[0].post_id-1
    next = show_post[0].post_id+1
    all_posts = blogpost.objects.values('post_id')
    post_count = len(all_posts)
   
    return render(request, 'blog/blogPost.html',{'post':show_post,'next_post':next,'older_post':older,'all_post':post_count})