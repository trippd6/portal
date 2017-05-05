from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Site, Account
from .tables import SiteTable
from .vacso_dns import get_current_dc, swap_dc
import logging

logger = logging.getLogger(__name__)

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/client/login/')

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
    
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/client/')
            else:
                return HttpResponse("Your account is disabled.")
        else:
            return HttpResponse("Invalid login details supplied.")

    else:
        return render(request, 'client/login.html', {})


@login_required
def index(request):
    site_list = Site.objects.filter(account__users__username=request.user.username).order_by('account')
    #table = SiteTable(site_list)
    #ite_list
    return render(request, 'client/index.html', { 'site_list': site_list } )

@login_required
def site(request, id):
    site = Site.objects.get(pk=id)
    
    if 'swap' in request.GET:
         logger.error('SWAPPING!')
         swap_dc(site.name)
    
    return render(request, 'client/site.html', { 
                                                'id': id , 
                                                'site': site,
                                                'hosted_dc': get_current_dc(site.name)[0],
                                                })
