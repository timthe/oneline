from django.shortcuts import render, redirect
from line.models import Item
from line.forms import ItemForm
from django.contrib.auth.decorators import login_required


def home(request):
    items = Item.objects.all()
    return render(request, 'home.html', {'items' : items})

@login_required(login_url='/login/')
def new_line(request):
    if request.method == 'POST':
        form = ItemForm({'text': request.POST['text'], 'user': request.user})
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = ItemForm()
        return render(request, 'newline.html', {'form':form})

@login_required(login_url='/login/')
def edit_line(request, line_id):
    edit_item = Item.objects.get(id=line_id)   
    if request.method == 'POST':
        edit_item.text = request.POST['text']
        edit_item.save()
        return redirect('/')
    else:
        form = ItemForm({'text':edit_item.text})
        return render(request, 'edit.html', {'form':form, 'item':edit_item})


@login_required(login_url='/login/')
def delete_line(request, line_id):
    deleting_item = Item.objects.filter(id=line_id)
    deleting_item.delete()
    return redirect('/')
