from django.shortcuts import render
import random
# Create your views here.

def BlogPost(req):
    dummy_posts = [
    {
        "title": "Lorem Ipsum Post",
        "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
        "author": "John Doe",
        "image_url": f"https://picsum.photos/400/400?random={random.randint(1, 100)}"
    },
    {
        "title": "Python Programming Tips",
        "content": "Learn some useful tips for Python programming.",
        "author": "Jane Smith",
        "image_url": f"https://picsum.photos/400/400?random={random.randint(1, 100)}"
    },
    {
        "title": "Data Science Insights",
        "content": "Exploring the world of data science and analytics.",
        "author": "David Johnson",
        "image_url": f"https://picsum.photos/400/400?random={random.randint(1, 100)}"
    },
    {
        "title": "Web Development Trends",
        "content": "Discover the latest trends in web development.",
        "author": "Emily Davis",
        "image_url": f"https://picsum.photos/400/400?random={random.randint(1, 100)}"
    },
    {
        "title": "Tips for Effective Time Management",
        "content": "Maximize your productivity with these time management tips.",
        "author": "Chris Brown",
        "image_url": f"https://picsum.photos/400/400?random={random.randint(1, 100)}"
    },
    {
        "title": "Healthy Living Habits",
        "content": "Explore habits for a healthier and happier lifestyle.",
        "author": "Amy White",
        "image_url": f"https://picsum.photos/400/400?random={random.randint(1, 100)}"
    },
    {
        "title": "Introduction to Machine Learning",
        "content": "Understanding the basics of machine learning algorithms.",
        "author": "Michael Lee",
        "image_url": f"https://picsum.photos/400/400?random={random.randint(1, 100)}"
    },
    {
        "title": "Travel Adventures",
        "content": "Embark on a journey through exciting travel adventures.",
        "author": "Sophie Robinson",
        "image_url": f"https://picsum.photos/400/400?random={random.randint(1, 100)}"
    },
    {
        "title": "Cooking Delights",
        "content": "Delicious recipes and cooking tips for food enthusiasts.",
        "author": "Daniel Miller",
        "image_url": f"https://picsum.photos/400/400?random={random.randint(1, 100)}"
    },
    {
        "title": "Tips for Remote Work Success",
        "content": "Navigate the challenges of remote work with these tips.",
        "author": "Jessica Taylor",
        "image_url": f"https://picsum.photos/400/400?random={random.randint(1, 100)}"
    }
]   
    return render(req,'blog.html',context={'postList':dummy_posts})
