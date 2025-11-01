from django.shortcuts import render, redirect, get_object_or_404
from .models import CRUD
from django.contrib import messages

# Create your views here.
def any_view(request):
    return render(request, 'accounts/any.html')

def create_view(request):

    cruds = CRUD.objects.all().order_by('-created_at')
    if request.method == 'POST':
        name = request.POST.get('name')
        message = request.POST.get('message')

        if not name or not message:
            messages.error(request, "Enter both fields")
        else:
            CRUD.objects.create(name=name, message=message)
            messages.success(request, "Successfully added ")
            return redirect('create')
    return render(request, 'accounts/create.html', {'cruds':cruds})


def read_view(request):
    cruds = CRUD.objects.all()

    return render(request, 'accounts/read.html',{'cruds':cruds})

def update_view(request, id):
    crud = get_object_or_404(CRUD, id=id)

    if request.method == 'POST':
        name = request.POST.get('name')
        message = request.POST.get('message')

        if not name or not message:
            messages.error(request, "Enter both fields")
        else:
            crud.name = name
            crud.message =message
            crud.save()
            messages.success(request, "Successfully updated ")
            return redirect('create')
    return render(request, 'accounts/update.html', {'crud':crud})