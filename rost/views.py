from django.shortcuts import render
def post_list(request):
    return render(request, 'rost/post_list.html', {})
