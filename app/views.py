from django.shortcuts import render, redirect
from django.views import View
from .models import Product, Cart, Customer, OrderPlaced
from .forms import customerRegisternationform, ProfileForm
from django.contrib import messages
from .models import Customer, Cart,Product
# def home(request):
#  return render(request, 'app/home.html')

class productview(View):
 def get (self, request):
  topwear = Product.objects.filter(category = 'TW')
  bottomwear = Product.objects.filter(category = 'BW')
  mobile = Product.objects.filter(category = 'M')
  return render (request, 'app/home.html', {'topwear':topwear, 'bottomwear':bottomwear, 'mobile':mobile})



class productdetailview(View):
 def get(self, request, pk):
  product = Product.objects.get(pk=pk)
  return render(request, 'app/productdetail.html', {'product':product})

def add_to_cart(request):
 user = request.user
 product_id = request.GET.get('prod_id')
 product = Product.objects.get(id=product_id)
 Cart(user=user, product=product).save()
 return redirect ('/')

def show_cart(request):
 if request.user.is_authenticated:
  user = request.user
  cart = Cart.objects.filter(user=user)
  amount = 0.0
  shipping_amount = 50.0
  total_amount = 0.0

  cart_product = [p for p in Cart.objects.all() if p.user == user]

  if cart_product:
   for p in cart_product:
    temamount = (p.quantity * p.product.discounted_price)
    amount += temamount
    total_amount = amount + shipping_amount
    if amount >= 500:
     shipping_amount = 0.0
     total_amount = amount + shipping_amount
    #  messages.success(request, 'WOWW!! Great Offer Shipping Free ')

  return render(request, 'app/addtocart.html',{'carts':cart, 'amount1':total_amount, 'ship':shipping_amount, 'amount': amount})
  

def buy_now(request):
 return render(request, 'app/buynow.html')


class AddressView(View):
 def get(self, request):
  data = Customer.objects.filter(user=request.user)
  return render (request, 'app/address.html', {'data':data, 'active':'btn-primary'})

def orders(request):
 return render(request, 'app/orders.html')


def mobile(request, data=None):
 if data == None:
  mobiles = Product.objects.filter(category ='M')
 elif data == 'apple' or data == 'samsung' or data =='realme':
  mobiles = Product.objects.filter(category ='M').filter(brand =data)
 elif data == 'below':
  mobiles = Product.objects.filter(category ='M').filter(discounted_price__lt=15000)
 elif data == 'above':
  mobiles = Product.objects.filter(category ='M').filter(discounted_price__gt=15000)
 return render(request, 'app/mobile.html', {'mobiles':mobiles})



def topwear(request, data=None):
 if data == None:
  topwear = Product.objects.filter(category ='TW')
 elif data == 'below':
  topwear = Product.objects.filter(category ='TW').filter(discounted_price__lt= 700)
 elif data == 'above':
  topwear = Product.objects.filter(category ='TW').filter(discounted_price__gt= 700)

 return render(request, 'app/topwear.html', {'topwear':topwear})

def bottomwear(request, data=None):
 if data == None:
  bottomwear = Product.objects.filter(category ='BW')
 elif data == 'below':
  bottomwear = Product.objects.filter(category ='BW').filter(discounted_price__lt= 700)
 elif data == 'above':
  bottomwear = Product.objects.filter(category ='BW').filter(discounted_price__gt= 700)
 return render(request, 'app/bottomwear.html',{'bottomwear':bottomwear})
 


# def customerregistration(request):
#  return render(request, 'app/customerregistration.html')

class Customerregisternation(View):
 def get (self, request):
  form = customerRegisternationform()
  return render (request, 'app/customerregistration.html',{'form':form})
 def post (self, request):
  form = customerRegisternationform(request.POST)
  if form.is_valid():
   messages.success(request, 'Congratulations ! your Registred succesfully')
   form.save()
  return render (request, 'app/customerregistration.html',{'form':form})


def checkout(request):
 return render(request, 'app/checkout.html')


class ProfileView(View):
 def get(self, request):
  form = ProfileForm()
  return render(request, 'app/profile.html', {'form':form, 'active': 'btn-primary'})
 
 def post(self, request):
  form = ProfileForm(request.POST)
  if form.is_valid():
    usr = request.user
    name = form.cleaned_data['name']
    locality = form.cleaned_data['locality']
    city = form.cleaned_data['city']
    zipcode = form.cleaned_data['zipcode']
    state = form.cleaned_data['state']

    data = Customer(user = usr, name = name, locality = locality, city = city, zipcode = zipcode, state = state)
    data.save()
    messages.success(request, 'Congratulations ! Your Address is Successfully Saved')

  return render(request, 'app/profile.html', {'form':form, 'active': 'btn-primary'})
