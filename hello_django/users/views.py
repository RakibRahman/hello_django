from django.shortcuts import render
from .forms import UserRegistration
# Create your views here.
def UserList(req):
    userListArray = [
        {
    "id": 1,
    "name": "Leanne Graham",
    "username": "Bret",
    "email": "Sincere@april.biz",
    'img':'https://randomuser.me/api/portraits/men/41.jpg',
    "address": {
      "street": "Kulas Light",
      "suite": "Apt. 556",
      "city": "Gwenborough",
      "zipcode": "92998-3874",
      "geo": {
        "lat": "-37.3159",
        "lng": "81.1496"
      }}
    },
     {
    "id": 2,
    "name": "Ervin Howell",
    "username": "Antonette",
    "email": "Shanna@melissa.tv",
    'img':'https://randomuser.me/api/portraits/men/74.jpg',
    "address": {
      "street": "Victor Plains",
      "suite": "Suite 879",
      "city": "Wisokyburgh",
      "zipcode": "90566-7771",
      "geo": {
        "lat": "-43.9509",
        "lng": "-34.4618"
      }
    },
    "phone": "010-692-6593 x09125",
    "website": "anastasia.net",
    "company": {
      "name": "Deckow-Crist",
      "catchPhrase": "Proactive didactic contingency",
      "bs": "synergize scalable supply-chains"
    }
  },
    ]
    frm = UserRegistration(auto_id='user_%s',initial={'nid':653})
    frm.order_fields(field_order=['nid'])
    return render(req,'userList.html',{'list':userListArray,'form':frm})