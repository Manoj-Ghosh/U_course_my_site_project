from datetime import date

from django.shortcuts import render


posts = [
    {
        "slug":"hike-in-the-mountain",
        "image": "mountains.jpeg",
        "author": "Manoj",
        "date": date(2024, 7, 17),
        "title":"Mountain Hiking",
        "excerpt": "There's is nothing like views you get when hiking in the mountains!I wasn't even prepared for what happend whilst I was enjoying the view!",
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
        "slug":"hike-in-the-mountain",
        "image": "mountains.jpeg",
        "author": "Manoj",
        "date": date(2023, 8, 17),
        "title":"Mountain Hiking",
        "excerpt": "There's is nothing like views you get when hiking in the mountains!I wasn't even prepared for what happend whilst I was enjoying the view!",
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
        "slug":"hike-in-the-mountain",
        "image": "mountains.jpeg",
        "author": "Manoj",
        "date": date(2022, 7, 7),
        "title":"Mountain Hiking",
        "excerpt": "There's is nothing like views you get when hiking in the mountains!I wasn't even prepared for what happend whilst I was enjoying the view!",
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

# Create your views here.

def starting_page(request):
    return render(request, "blog/index.html")

def posts(request):
    return render(request, "blog/all-posts.html")

def post_detail(request, slug):
    return render(request, "blog/post-detail.html")
    


