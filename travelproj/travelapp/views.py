from django.shortcuts import render

from travelapp.models import Place, Team


# Create your views here.
def demo2(request):
    obj=Place.objects.all()
    obj2=Team.objects.all()
    return render(request,'index.html',{'result':obj,'result2':obj2})