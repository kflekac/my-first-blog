"""A view is a place where we put the "logic" of our application.
It will request information from the model you created before and pass
it to a template. We'll create a template in the next chapter. Views are
just Python functions that are a little bit more complicated than the ones
we wrote in the Introduction to Python chapter.
"""


from django.shortcuts import render

def post_list(request):
    return render(request, 'blog/post_list.html', {})
