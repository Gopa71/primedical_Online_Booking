from django.shortcuts import render
from .models import Service,Product
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator,InvalidPage,EmptyPage

# Create your views here.
def allProCat(req,c_slug=None):
    c_page=None
    if c_slug!=None:
       c_page=get_object_or_404(Service,slug=c_slug)
       product_list=Product.objects.filter(service=c_page,available=True)
    else:
       product_list=Product.objects.filter(available=True)

   #  Paginator
    
    paginator=Paginator(product_list,4)
    try:
       page=int(req.GET.get('page',))
    except:
       page=1
    try:
       products=paginator.page(page)
    except(EmptyPage,InvalidPage):
       products=paginator.page(paginator.num_pages)  
     
    return render(req,'category.html',{'product':products,'service':c_page})
