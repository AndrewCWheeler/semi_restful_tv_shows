from datetime import date
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Show

def shows(request):
    
    context = {
        'all_shows' : Show.objects.all(),
        
    }
    return render(request, 'all_shows.html', context)

def new_show_form(request):
    return render(request, 'new_show.html')

def create_show(request):
    errors = Show.objects.show_validator(request.POST)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/shows/new')
    else:
        title = request.POST['title']
        network = request.POST['network']
        date = request.POST['date']
        desc = request.POST['desc']
        new_show = Show.objects.create(
            title=title,
            network=network,
            date=date,
            desc=desc,
        )
        show_id = new_show.id
    return redirect(f'/shows/{show_id}')

def view_show(request, show_id):
    this_show = Show.objects.get(id=show_id)
    context = {
        'id' : this_show.id,
        'title' : this_show.title,
        'network' : this_show.network,
        'date' : this_show.date,
        'desc' : this_show.desc,
        'updated_at' : this_show.updated_at
    }
    return render(request, 'view_show.html', context)

def edit_show_form(request, show_id):
    this_show = Show.objects.get(id=show_id)
    context = {
        'id' : this_show.id,
        'title' : this_show.title,
        'network' : this_show.network,
        'date' : this_show.date,
        'desc' : this_show.desc,
    }
    return render(request, 'edit_show.html', context)

def edit_show(request):
    show_id = request.POST['show_id']
    errors = Show.objects.show_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f'/shows/{show_id}/edit')
    else:
        title = request.POST['title']
        network = request.POST['network']
        date = request.POST['date']
        desc = request.POST['desc']
        e = Show.objects.get(id=show_id)
        e.title = title
        e.network = network
        e.date = date
        e.desc = desc
        e.save()
        return redirect(f'/shows/{show_id}')

def delete_show(request, show_id):
    d = Show.objects.get(id=show_id)
    d.delete()
    return redirect('/shows')

