"""A view is a place where we put the "logic" of our application.
It will request information from the model you created before and pass
it to a template. We'll create a template in the next chapter. Views are
just Python functions that are a little bit more complicated than the ones
we wrote in the Introduction to Python chapter.
"""


from django.shortcuts import render
#the "." tells it to look in the current directory
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by(
                                                            'published_date')

    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk = pk)
    return render(request, 'blog/post_detail.html', {'post': post})
