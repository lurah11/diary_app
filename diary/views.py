from django.shortcuts import render, redirect
from .models import Entry
from .forms import EntryForm

# Create your views here.
def index(request):
    entries = Entry.objects.order_by('-date')
    context = {
        'entries':entries
    }
    return render(request,'diary/index.html',context=context)

def add(request):
    print(request)
    if request.method == "POST":
        form = EntryForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            entry = Entry(text=text)
            entry.save()
            return redirect('diary:index')
    else : 
        form = EntryForm()
    context = {
        'form':form
    }
    return render(request,'diary/add.html',context=context)
