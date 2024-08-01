from datetime import date

from django.shortcuts import render

from .models import Post


all_posts = []




def get_date(post):
    return post['date']

# Create your views here.

def starting_page(request):
    latest_posts = Post.objects.all().order_by("-date")[:3]
    # sorted_posts = sorted(all_posts, key=get_date)
    # latest_posts = all_posts[-3:]
    return render(request, "blog/index.html", {"list_posts": latest_posts})

def posts(request):
    all_posts = Post.objects.all().order_by("-date")
    return render(request, "blog/all-posts.html", {"all_posts": all_posts})



def post_detail(request, slug):
    identified_post = next(post11 for post11 in all_posts if post11['slug'] == slug)
    return render(request, "blog/post-detail.html", {"post11" : identified_post})
    


