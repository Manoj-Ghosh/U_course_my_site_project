from datetime import date
from typing import Any 
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView, DetailView
from django.views import View

from .models import Post
from .forms import CommentForm







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


class SingePostView(View):
    template_name = "blog/post-detail.html"
    model = Post
    context_object_name = "post11"

    def get(self, request, slug):
        postt= Post.objects.get(slug = slug)
        context = {
            "post11": postt,
            "post_tags": postt.tags.all(),
            "comment": CommentForm()
        }
        return render(request, "blog/post-detail.html", context)


    def post(self, request, slug):
        comment_form = CommentForm(request.POST)
        postt= Post.objects.get(slug = slug)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post= postt
            comment.save()

            return HttpResponseRedirect(reverse("post-detail-page", args=[slug]))
        

        

        context = {
            "post11": postt,
            "post_tags": postt.tags.all(),
            "comment": CommentForm
        }

        return render(request, "blog/post-detail.html", context)




    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)

    #     context["post_tags"] = self.object.tags.all()
    #     context["comment"] = CommentForm()
    #     return context

# def post_detail(request, slug):
#     #identified_post = next(post11 for post11 in all_posts if post11['slug'] == slug)
#     #identified_post = Post.objects.get(slug=slug)
#     identified_post = get_object_or_404(Post, slug = slug)
#     return render(request, "blog/post-detail.html", {
#         "post11" : identified_post,
#         "post_tags": identified_post.tags.all()
#         })
    


