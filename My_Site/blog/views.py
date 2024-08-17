from datetime import date
from typing import Any 
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

from .models import Post







# def get_date(post):
#     return post['date']

# Create your views here.


class StartingPageView(ListView):
    template_name = "blog/index.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "list_posts"


    def get_queryset(self):
        query_set = super().get_queryset()
        data = query_set[:3]
        return data
    


# def starting_page(request):
#     latest_posts = Post.objects.all().order_by("-date")[:3]
#     # sorted_posts = sorted(all_posts, key=get_date)
#     # latest_posts = all_posts[-3:]
#     return render(request, "blog/index.html", {"list_posts": latest_posts})


class AllPostView(ListView):
    template_name = "blog/all-posts.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "all_posts"

    

# def posts(request):
#     all_posts = Post.objects.all().order_by("-date")
#     return render(request, "blog/all-posts.html", {"all_posts": all_posts})



def post_detail(request, slug):
    #identified_post = next(post11 for post11 in all_posts if post11['slug'] == slug)
    #identified_post = Post.objects.get(slug=slug)
    identified_post = get_object_or_404(Post, slug = slug)
    return render(request, "blog/post-detail.html", {
        "post11" : identified_post,
        "post_tags": identified_post.tags.all()
        })
    


