from django.shortcuts import render, get_object_or_404, resolve_url
from .models import House

def houses_list(request):
	houses = House.objects.all()
	return render(request, "houses/houses_list.html", {"houses": houses})
#добавление еще представления
def house_detail(request, house_id):
	house = get_object_or_404(House, id=house_id)
	return render(request, "houses/house_detail.html", {"house": house})
