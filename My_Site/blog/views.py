from datetime import date

from django.shortcuts import render


all_posts = [
    {
        "slug":"hike-in-the-mountain",
        "image": "mountains.jpg",
        "author": "Manoj",
        "date": date(2021, 7, 17),
        "title":"Mountain Hiking",
        "excerpt": "There's is nothing like Mountain Hiking views you get when hiking in the mountains!I wasn't even prepared for what happend whilst I was enjoying the view!",
        "content": """
            As of June 2020, the Bengali Wikipedia is the only online free 
            encyclopedia written in the Bengali language. It is also one of 
            the largest Bengali content related sites on the internet. 
            The mobile version of the Bengali Wikipedia was launched in 2010
             As of June 2020, the Bengali Wikipedia is the only online free 
            encyclopedia written in the Bengali language. It is also one of 
            the largest Bengali content related sites on the internet. 
            The mobile version of the Bengali Wikipedia was launched in 2010
             
              As of June 2020, the Bengali Wikipedia is the only online free 
            encyclopedia written in the Bengali language. It is also one of 
            the largest Bengali content related sites on the internet. 
            The mobile version of the Bengali Wikipedia was launched in 2010
             As of June 2020, the Bengali Wikipedia is the only online free 
            encyclopedia written in the Bengali language. It is also one of 
            the largest Bengali content related sites on the internet. 
            The mobile version of the Bengali Wikipedia was launched in 2010
             
              As of June 2020, the Bengali Wikipedia is the only online free 
            encyclopedia written in the Bengali language. It is also one of 
            the largest Bengali content related sites on the internet. 
            The mobile version of the Bengali Wikipedia was launched in 2010 """
    },
        
    

    {
        "slug":"Nature",
        "image": "woods.jpg",
        "author": "Manoj",
        "date": date(2022, 7, 7),
        "title":"Nature at its best",
        "excerpt": "There's is nothing like Nature at its best views you get when hiking in the mountains!I wasn't even prepared for what happend whilst I was enjoying the view!",
        "content": """
            As of June 2020, the Bengali Wikipedia is the only online free 
            encyclopedia written in the Bengali language. It is also one of 
            the largest Bengali content related sites on the internet. 
            The mobile version of the Bengali Wikipedia was launched in 2010
             As of June 2020, the Bengali Wikipedia is the only online free 
            encyclopedia written in the Bengali language. It is also one of 
            the largest Bengali content related sites on the internet. 
            The mobile version of the Bengali Wikipedia was launched in 2010
             
              As of June 2020, the Bengali Wikipedia is the only online free 
            encyclopedia written in the Bengali language. It is also one of 
            the largest Bengali content related sites on the internet. 
            The mobile version of the Bengali Wikipedia was launched in 2010
             As of June 2020, the Bengali Wikipedia is the only online free 
            encyclopedia written in the Bengali language. It is also one of 
            the largest Bengali content related sites on the internet. 
            The mobile version of the Bengali Wikipedia was launched in 2010
             
              As of June 2020, the Bengali Wikipedia is the only online free 
            encyclopedia written in the Bengali language. It is also one of 
            the largest Bengali content related sites on the internet. 
            The mobile version of the Bengali Wikipedia was launched in 2010 """
    },

    {
        "slug":"Programming",
        "image": "coding.jpg",
        "author": "Manoj",
        "date": date(2023, 8, 17) ,
        "title":"Programming is Great",
        "excerpt": "There's is nothing like Programming is Great views you get when hiking in the mountains!I wasn't even prepared for what happend whilst I was enjoying the view!",
        "content": """
            As of June 2020, the Bengali Wikipedia is the only online free 
            encyclopedia written in the Bengali language. It is also one of 
            the largest Bengali content related sites on the internet. 
            The mobile version of the Bengali Wikipedia was launched in 2010
             As of June 2020, the Bengali Wikipedia is the only online free 
            encyclopedia written in the Bengali language. It is also one of 
            the largest Bengali content related sites on the internet. 
            The mobile version of the Bengali Wikipedia was launched in 2010
             
              As of June 2020, the Bengali Wikipedia is the only online free 
            encyclopedia written in the Bengali language. It is also one of 
            the largest Bengali content related sites on the internet. 
            The mobile version of the Bengali Wikipedia was launched in 2010
             As of June 2020, the Bengali Wikipedia is the only online free 
            encyclopedia written in the Bengali language. It is also one of 
            the largest Bengali content related sites on the internet. 
            The mobile version of the Bengali Wikipedia was launched in 2010
             
              As of June 2020, the Bengali Wikipedia is the only online free 
            encyclopedia written in the Bengali language. It is also one of 
            the largest Bengali content related sites on the internet. 
            The mobile version of the Bengali Wikipedia was launched in 2010 """
    }



]

def get_date(post):
    return post['date']

# Create your views here.

def starting_page(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = all_posts[-3:]
    return render(request, "blog/index.html", {"list_posts": latest_posts})

def posts(request):
    return render(request, "blog/all-posts.html", {"all_posts": all_posts})


def post_detail(request, slug):
    return render(request, "blog/post-detail.html")
    


