from django.shortcuts import render
from .models import Item
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView



# Create your views here.






def mylist(request):
    if request.method == 'POST':
        Item.objects.create(
        name = request.POST['itemName'],
        beschreibung = request.POST['itemBeschreibung'],
        link = request.POST['itemTag'],
        public = request.POST['itemPublic'],
        useridnummer = request.POST['itemUserid'],
        author = request.user
    )

    all_items = Item.objects.all()

    if 'q' in request.GET:
        q = request.GET['q']
        # all_items = Item.objects.filter(name__icontains=q)
        multiple_q = Q(Q(name__icontains=q) | Q(beschreibung__icontains=q) | Q(link__icontains=q))
        all_item = Item.objects.filter(multiple_q)


    return render(request, 'index.html', {'all_items': all_items})






@login_required(login_url='user-login')
def private(request):
        if 'p' in request.GET:
            p = request.GET['p']
            # all_items = Item.objects.filter(name__icontains=q)
            multiple_p = Q(Q(author=request.user) & Q(public__icontains='private')) & Q(Q(name__icontains=p) | Q(beschreibung__icontains=p) | Q(link__icontains=p))
            all_items = Item.objects.filter(multiple_p)

        else:
            private = Q(Q(author=request.user) & Q(public__icontains='private'))
            all_items = Item.objects.filter(private)

        return render(request, 'private.html', {'all_items': all_items})



