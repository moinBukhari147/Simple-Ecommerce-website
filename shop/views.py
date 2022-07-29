from logging import exception
from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
from math import ceil
import json
from .models import product, contact_us, newOrders, newTrackingUpdate
def index(request):
    product_categories = product.objects.values('product_category', 'id')
    categorised_product = []
    cats = {item['product_category'] for item in product_categories}
    for cat in cats:
        products = product.objects.filter(product_category= cat)
        num_of_prod = len(products)
        num_of_slides = num_of_prod // 4 + ceil(num_of_prod / 4 - num_of_prod // 4)
        categorised_product.append([products,num_of_slides,range(1,num_of_slides)])
    no_product = False
    para = {"categorised_product": categorised_product,'no_product': no_product}
    return render(request, 'shop/index.html', para)
# Search funtion logic will implement here
def searchMatch(query, item):
    if query in item.product_desc.lower() or query in item.product_name.lower() or query in item.product_category.lower() or query in item.product_subcatrgory.lower():
        return True
    else:
        return False
# Search function for views dot py
def search (request):
    if request.method == "GET":
        search_query = request.GET.get('search','none').lower()
        product_categories = product.objects.values('product_category', 'id')
        categorised_product = []
        cats = {item['product_category'] for item in product_categories}
        for cat in cats:
            all_products = product.objects.filter(product_category= cat)
            products = [item for item in all_products if searchMatch(search_query,item)]
            num_of_prod = len(products)
            num_of_slides = num_of_prod // 4 + ceil(num_of_prod / 4 - num_of_prod // 4)
            if num_of_prod!= 0:
                categorised_product.append([products,num_of_slides,range(1,num_of_slides)])
        no_product = False
        if len(categorised_product) == 0:
            no_product = True
        para = {"categorised_product": categorised_product,'no_product': no_product}
        return render(request, 'shop/index.html', para)

def about(request):
    return render(request, 'shop/about.html')
def contactUs(request):
    if request.method == 'POST':
        person_name= request.POST.get('full_name','none')
        person_contact = request.POST.get('contact', '0')
        person_email = request.POST.get('email','none')
        person_query = request.POST.get('query', 'none')
        saving_contact_database = contact_us(contactor_name=person_name,contactor_email=person_email,contactor_phone=person_contact,contactor_query=person_query)
        saving_contact_database.save()
        message = True
        return render(request, 'shop/contact.html',{'message':message})
    return render(request, 'shop/contact.html')
def productView(request,myid):
    viewproduct = product.objects.filter(id=myid)

    # fetching the product using id
    return  render(request, 'shop/productView.html', {'viewProduct': viewproduct[0]})
def tracking(request):
    if request.method == "POST":
        tracking_Id = request.POST.get('trackerId')
        track_email = request.POST.get('email')
        try:
            checkTracker = newOrders.objects.filter(trackId= tracking_Id, chekout_email = track_email)
            if len(checkTracker)>0:
                update = newTrackingUpdate.objects.filter(orderId = tracking_Id)
                updatess =[]
                for item in update:
                    updatess.append({'text':item.orderUpdate, 'time': item.timeUpdate})
                response = json.dumps([updatess, checkTracker[0].item_jason], default=str)
                return HttpResponse(response)
            else:
                return HttpResponse(json.dumps(False))
        except Exception as e:
            return HttpResponse(f'exception is {e} ')
    return render(request, 'shop/tracking.html')
i=234
def checkout(request):
    
    if request.method == "POST":
        checkout_fname = request.POST.get('fname','none')
        checkout_lname = request.POST.get('lname','none')
        checkout_address = request.POST.get('address','none')
        checkout_phone = request.POST.get('phone','none')
        checkout_city = request.POST.get('city','none')
        checkout_state = request.POST.get('state','none')
        checkout_zip = request.POST.get('zip','none')
        checkout_email= request.POST.get('email','none')
        item_json = request.POST.get('itemJson','none')
        i=i+4
        checkout_track_id = i
        save_order_database = newOrders(trackId =checkout_track_id, chekout_fname = checkout_fname, chekout_lname =checkout_lname, chekout_address= checkout_address, chekout_phone= checkout_phone, chekout_city=checkout_city,chekout_state=checkout_state,chekout_zip=checkout_zip,chekout_email=checkout_email,item_jason=item_json)
        save_order_database.save()
        
        thanks_message = True
        trackUpdate = newTrackingUpdate(orderId = checkout_track_id, orderUpdate = "Order has been Dispached")
        trackUpdate.save()
        return render(request, 'shop/checkout.html',{'thanks':thanks_message, 'checkout_track_id':checkout_track_id})
    thanks_message = False
    return render(request, 'shop/checkout.html',{'thanks':thanks_message})

