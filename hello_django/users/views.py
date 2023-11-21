from django.shortcuts import render

# Create your views here.
def UserList(req):
    return render(req,'userList.html')