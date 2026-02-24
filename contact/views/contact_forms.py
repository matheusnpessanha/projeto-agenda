from django.shortcuts import render
from contact.forms import Contactform


def create(request):
    if request.method == 'POST':
    
        context = {
            'form': Contactform(request.POST)

        }

        return render(
            request,
            'contact/create.html',
            context
        )
    
    context = {
        'form': Contactform()
    }

    return render(
        request,
        'contact/create.html',
        context
    )