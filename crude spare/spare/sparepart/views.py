from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages



def index(request):
 
    item_list= Item.objects.all()
    context={
    'item_list' :item_list
        }
    return render(request,'index.html',context)


def add_item(request):
    if request.method=="POST":
        name=request.POST['name']
        description = request.POST.get('description')
        item=Item(name=name,description=description)
        item.save()
        messages.info(request,"ITEM ADDEDD SUCCESSFULL")
    else:
        pass 
    item_list= Item.objects.all()
    context={
        'item_list' :item_list
    }
    return render(request,'index.html',context)



def delete_item(request,myid):
    item = Item.objects.get(id = myid)
    item.delete()
    messages.info(request,"item deleted successfully")
    return render(request,'index.html')

def edit_item(request,myid):
    sel_item = Item.objects.get(id = myid)
    item_list=Item.objects.all()
    context ={
        'sel_item':item_list,
        'item_list': item_list
    }
   
    return render(request,'index.html',context)


def update_item(request,myid):
    item = Item.objects.get(id = myid)
    item.name = request.POST['description']
    item.save()
    messages.info(request," YOUR ITEM UPDATE SUCCESSFULL")
    return redirect('index')

