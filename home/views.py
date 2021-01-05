from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response

from rest_framework.decorators import api_view

from home.forms import *



def index(request):
    return render(request, 'index.html')

def create_author(request):
    if request.method == "POST":
        form = Author_frm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = Author_frm()
    return render(request, 'create_author.html', {'form': form})

def create_publisher(request):
    if request.method == "POST":
        form = Publisher_frm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = Publisher_frm()
    return render(request, 'create_publisher.html', {'form': form})

def create_book(request):
    publishers = Publisher.objects.all()
    authors = Author.objects.all()
    if request.method == "POST":
        pbId = request.POST['publisher']
        pbObj = Publisher.objects.get(id=pbId)
        form = Book_frm(request.POST)
        if form.is_valid():
            f=form.save(commit=False)
            f.publisher=pbObj
            form.save()
        last_book = Book.objects.last()
        book_product = Book.objects.get(id=last_book.id)
        authorIdList = request.POST.getlist('author')
        for x in authorIdList:
            authorObj = Author.objects.get(id=x)
            book_product.authors.add(authorObj)
        # name = request.POST['name']
        # serial = request.POST['serial']
        # authorId = request.POST.getlist('services')
        # print(authorId)
        # authorObj = Author.objects.get(id=authorId)
        # pbId = request.POST['publisher']
        # pbObj = Publisher.objects.get(id=pbId)
        #
        # b = Author(name=name, serial=serial, publisher=pbObj)
        # b.save()
        # last_book = Book.objects.last()
        # book_product = Book.objects.get(id=last_book.id)
        # book_product.author.add(authorObj)

    return render(request, 'create_book.html', {'authors': authors, 'publishers': publishers})

