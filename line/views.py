from django.shortcuts import render, redirect, get_object_or_404
from line.models import Item, Comment
from line.forms import ItemForm, CategoryForm, CommentForm
from django.contrib.auth.decorators import login_required


def home(request):
    items = Item.objects.all()
    return render(request, 'home.html', {'items': items})

def medicine_list(request):
    items = Item.objects.filter(mtype='JH')
    return render(request, 'list.html', {'items': items})

def detail_view(request, item_pk):
    item = get_object_or_404(Item, id=item_pk)
    comments = Comment.objects.filter(item=item)
    form = CommentForm()
    return render(request, 'detail.html', 
        {'item': item, 'comments': comments, 'form': form})

@login_required(login_url='/login/')
def new_comment(request, item_id):
    form = CommentForm(data=request.POST)
    if form.is_valid():
        item = Item.objects.get(id=item_id)
        form.save(user=request.user, item=item)
    return redirect('detail_view', item.pk)

@login_required(login_url='/login/')
def edit_comment(request, comment_id):
    edit_comment = Comment.objects.get(id=comment_id)
    if request.method == 'POST':
        edit_comment.content = request.POST['content']
        edit_comment.save()
        return redirect('detail_view', edit_comment.item.pk)
    else:
        form = CommentForm({'content': edit_comment.content})
        return render(request, 'edit_comment.html', {'form':form, 'comment':edit_comment})


@login_required(login_url='/login/')
def new_category(request):
    if request.method == 'POST':
        form = CategoryForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = CategoryForm()
        return render(request, 'newcategory.html', {'form':form})

@login_required(login_url='/login/')
def new_line(request):
    if request.method == 'POST':
        form = ItemForm(data=request.POST)
        if form.is_valid():
            form.save(user=request.user)
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
