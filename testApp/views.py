from django.shortcuts import render


def pagecount_view(request):
    count= int(request.COOKIES.get('count',0))
    count=count+1
    response=render(request, 'testApp/counter.html', {'count': count})
    response.set_cookie('count',count)
    return response

