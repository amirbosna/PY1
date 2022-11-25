from django.shortcuts import render, render
from .models import Post, Comment
from django.db.models import Q
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.core import serializers
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.shortcuts import redirect
from .forms import EditForm, CommentForm
from django.urls import reverse_lazy



# Create your views here.

class HomeView(ListView):
    model = Post
    template_name = 'index.html'



class Detailed(DetailView):
    context_object_name = 'id'
    model = Post
    template_name = 'details.html'
    form = CommentForm
    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        if form.is_valid():
            post = self.get_object()
            form.instance.user = request.user
            form.instance.post = post
            form.save()

            return redirect("article-detail", pk = post.id)

    def get_context_data(self, **kwargs):
        post_comments =  Comment.objects.all().filter(post=self.object.id)
        context = super().get_context_data(**kwargs)
        context.update({
            'form': self.form,
            'post_comments': post_comments,
        })
        return context



class UpdatePost(UpdateView):
    context_object_name = 'id'
    model = Post
    form_class = EditForm
    template_name = 'edit.html'
    #fields = ['name', 'beschreibung', 'public', 'link']



class AddPost(CreateView):
    model = Post
    template_name = 'add_post.html'
    fields = ['name', 'beschreibung', 'link', 'public']







def mylist(request):

    if 'q' in request.GET:
        q = request.GET['q']
        return redirect(("/search/" + "?q=" + q))

    elif request.method == 'POST':
        posts = Post.objects.all
        Post.objects.create(
        name = request.POST['itemName'],
        beschreibung = request.POST['itemBeschreibung'],
        link = request.POST['itemTag'],
        public = request.POST['itemPublic'],
        useridnummer = request.POST['itemUserid'],
        author = request.user
    )
        return render(request,('index.html', 'add_post.html'),{'posts':posts})
        

    elif request.user.is_active:
        filter = Q(Q(public__icontains='public') | Q(author=request.user) & Q(public__icontains='private'))
        posts=Post.objects.filter(filter)[::-1]
        # Pagintion
        paginator=Paginator(posts,5)
        page_number=request.GET.get('page')
        posts_obj=paginator.get_page(page_number)
        return render(request,('index.html', 'add_post.html'),{'posts':posts_obj})


    else:
        filter = Q(Q(public__icontains='private'))
        posts=Post.objects.filter(filter)[::-1]
        # Pagintion
        paginator=Paginator(posts,5)
        page_number=request.GET.get('page')
        posts_obj=paginator.get_page(page_number)
        return render(request,('index.html', 'add_post.html'),{'posts':posts_obj})










def privatelist(request):

    if 'p' in request.GET:
        p = request.GET['p']
        return redirect(("/privatesearch/" + "?p=" + p))

    elif request.method == 'POST':
        posts = Post.objects.all
        Post.objects.create(
        name = request.POST['itemName'],
        beschreibung = request.POST['itemBeschreibung'],
        link = request.POST['itemTag'],
        public = request.POST['itemPublic'],
        useridnummer = request.POST['itemUserid'],
        author = request.user
    )
        return render(request,('private.html', 'add_post.html'),{'posts':posts})

    elif request.user.is_active:
        filter = Q(Q(author=request.user) & Q(public__icontains='private'))
        posts=Post.objects.filter(filter)[::-1]
        # Pagintion
        paginator=Paginator(posts,5)
        page_number=request.GET.get('page')
        posts_obj=paginator.get_page(page_number)
        return render(request,('private.html', 'add_post.html'),{'posts':posts_obj})


    else:
        filter = Q(Q(public__icontains='private') & Q(author=request.user))
        posts=Post.objects.filter(filter)[::-1]
        # Pagintion
        paginator=Paginator(posts,5)
        page_number=request.GET.get('page')
        posts_obj=paginator.get_page(page_number)
        return render(request,('private.html', 'add_post.html'),{'posts':posts_obj})

















def search(request):
    if 'q' in request.GET:
        q = request.GET['q']
        # all_items = Item.objects.filter(name__icontains=q)
        multiple_q = Q(Q(name__icontains=q) & Q(author=request.user) & Q(public__icontains='private') | Q(beschreibung__icontains=q) & Q(author=request.user) & Q(public__icontains='private') | Q(link__icontains=q) & Q(author=request.user) & Q(public__icontains='private') | Q(Q(name__icontains=q) & Q(public__icontains='public') | Q(beschreibung__icontains=q) & Q(public__icontains='public') | Q(link__icontains=q) & Q(public__icontains='public')))
        postsearch = Post.objects.filter(multiple_q)[::-1]
        return render(request, 'search.html', {'posts': postsearch})
    




def privatesearch(request):
    if 'p' in request.GET:
        p = request.GET['p']
        # all_items = Item.objects.filter(name__icontains=q)
        multiple_p = Q(Q(name__icontains=p) & Q(author=request.user) & Q(public__icontains='private') | Q(beschreibung__icontains=p) & Q(author=request.user) & Q(public__icontains='private') | Q(link__icontains=p) & Q(author=request.user) & Q(public__icontains='private'))
        postsearch = Post.objects.filter(multiple_p)[::-1]
        return render(request, 'privatesearch.html', {'posts': postsearch})







def load_more(request):
    offset=int(request.POST['offset'])
    limit=2
    posts=Post.objects.all()[offset:limit+offset]
    totalData=Post.objects.count()
    data={}
    posts_json=serializers.serialize('json',posts)
    return JsonResponse(data={
        'posts':posts_json,
        'totalResult':totalData
    })



class DeletePost(DeleteView):
    context_object_name = 'id'
    model = Post
    template_name = 'delete.html'
    success_url = reverse_lazy('mylist')