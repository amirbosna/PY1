from django.shortcuts import render
from .models import ShoppingItem
from django.db.models import Q

# Create your views here.
def mylist(request):
    if request.method == 'POST':
        print('Received data:', request.POST['itemName'])
        ShoppingItem.objects.create(name = request.POST['itemName'])
    all_items = ShoppingItem.objects.all()

    if 'q' in request.GET:
        q = request.GET['q']
        # all_items = ShoppingItem.objects.filter(name__icontains=q)
        multiple_q = Q(Q(name__icontains=q) | Q(beschreibung__icontains=q) | Q(link__icontains=q))
        all_items = ShoppingItem.objects.filter(multiple_q)

    return render(request, 'index.html', {'all_items': all_items})