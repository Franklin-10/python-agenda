from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from contact.models import Contact
from django.http import Http404

# Create your views here.

def index(request):
    contacts = Contact.objects \
        .filter(show=True) \
        .order_by('-id')[0:10]
    
    print(contacts.query)
    context = {
        'contacts': contacts,
        'site_title': 'Contatos -'
    }
    return render(
        request,
        'contact/index.html',
        context
    )

def search(request):
    search_value = request.GET.get('q', '').strip()
    if search_value == '':
        return redirect('contact:index')
    contacts = Contact.objects \
        .filter(show=True) \
        .filter(Q(first_name__icontains=search_value) | Q(last_name__icontains=search_value) | Q(phone__icontains=search_value) | Q(email__icontains=search_value),) \
        .order_by('-id')
    
    print(contacts.query)
    context = {
        'contacts': contacts,
        'site_title': 'Search -'
    }
    return render(
        request,
        'contact/index.html',
        context
    )

def contact(request, contact_id):
    # single_contacts = Contact.objects.filter(pk=contact_id).first()
    single_contacts = get_object_or_404(Contact,pk=contact_id, show=True)
    site_title = f'{single_contacts.first_name} {single_contacts.last_name} -'
    context = {
        'contact': single_contacts,
        'site_title': site_title,
        

    }
    return render(
        request,
        'contact/contact.html',
        context
    )