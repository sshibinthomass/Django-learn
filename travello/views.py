from django.shortcuts import render
from .models import Destination
# Create your views here.
def home(request):
    dest1=Destination()
    dest1.name="Chennai"
    dest1.img='destination_1.jpg'
    dest1.price='300'
    dest1.desc="Namba ooru chennai"
    dest1.offer=False
    
    dest2=Destination()
    dest2.name="Mumbai"
    dest2.img='destination_2.jpg'
    dest2.price='400'
    dest2.desc="Stock capital"
    dest2.offer=True

    dest3=Destination()
    dest3.name="Delhi"
    dest3.img='destination_3.jpg'
    dest3.price='500'
    dest3.desc="National capital"
    dest3.offer=False

    dests=[dest1,dest2,dest3]
    return render(request,'index.html', {'dests':dests})