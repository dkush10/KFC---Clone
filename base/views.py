from django.shortcuts import render ,redirect
from .models import fooditems, Cart
from django.db.models import Q
from .forms import *
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def count_(request):
    totalquantity=0
    if request.user.is_authenticated:
        c=Cart.objects.filter(host=request.user)
        for i in c:
            totalquantity+=i.quantity
    return totalquantity

def home(request):
    return render(request,'home.html',{'count_':count_(request)})

def menu(request):
    c=fooditems.objects.all()
    categorylinks=[]
    for i in c:
        if i.category not in categorylinks:
            categorylinks+=[i.category]

    all=[]
    norec=''
    if request.method=='GET':
        if 'cat' in request.GET:
            cat=request.GET['cat']
            all=fooditems.objects.filter(category=cat)

        elif 'q' in request.GET:
            q=request.GET['q']
            all=fooditems.objects.filter(Q(name__icontains=q)|Q(desc__icontains=q)|Q(category__icontains=q))
            if len(all)==0:
                norec='No items found.'
        else:
            all=fooditems.objects.all()

    context={
        'category':categorylinks,
        'all':all,
        'norec':norec,
        'count_':count_(request),
    }
    return render(request,'menu.html',context)

def cart(request):
    if request.user.is_authenticated:
        c=Cart.objects.filter(host=request.user)

        totalamount=0
        for i in c:
            totalamount+=i.totalprice

        noitem=False
        if len(c)==0:
            noitem=True

        return render(request,'cart.html',{'c':c,
                                        'noitem':noitem,
                                        'totalamount':totalamount,
                                        'count_':count_(request),
                                        })
    else:
        return redirect('signin')

def remove(request, id):
    c=Cart.objects.get(id=id)
    c.delete()
    return redirect('cart')

def removeall(request):
    c=Cart.objects.filter(host=request.user)
    c.delete()
    return redirect('cart')


def addtocart(request, id):
    auth="Please sign in first!"
    if request.user.is_authenticated:
        f=fooditems.objects.get(id=id)

        try:
            c=Cart.objects.get(name=f.name,host=request.user)
            c.quantity+=1
            c.totalprice+=f.price
            c.save()
        except:
            Cart.objects.create(name=f.name,
                                image=f.image,
                                category=f.category,
                                desc=f.desc,
                                price=f.price,
                                quantity=1,
                                totalprice=f.price,
                                host=request.user,
                                )
        return redirect('menu')
    return render(request,'menu.html',{'auth':auth,'count_':count_(request)})

def quantityplus(request, id):
    c=Cart.objects.get(id=id)
    c.quantity+=1
    c.totalprice+=c.price
    c.save()
    return redirect('cart')

def quantityminus(request, id):
    c=Cart.objects.get(id=id)
    if c.quantity>1:
        c.quantity-=1
        c.totalprice-=c.price
        c.save()
        return redirect('cart')
    else:
        c.delete()
    return redirect('cart')


def checkout(request):
    if request.method =='POST':
        f=CheckoutForm(data=request.POST)
        if f.is_valid():
            ho=f.save(commit=False)
            ho.host=request.user
            ho.save()
            return redirect('orderplaced')
        else:
            print(f.errors)
    return render(request,'checkout.html',{'CheckoutForm':CheckoutForm,'count_':count_(request)})

def contactus(request):
    if request.method=='POST':
        f=ContactForm(data=request.POST)
        if f.is_valid():
            ho=f.save(commit=False)
            ho.host=request.user
            ho.save()
            return render(request,'contactthanks.html')
    return render(request,'contactus.html',{'ContactForm':ContactForm,'count_':count_(request)})

def contactthanks(request):
    return render(request,'contactthanks.html',{'count_':count_(request)})

def profile(request):
    return render(request,'profile.html',{'count_':count_(request)})

def updateprofile(request, id):
    u=User.objects.get(id=id)
    if request.method=='POST':
        first_name=request.POST['first_name']
        email=request.POST['email']
        username=request.POST['username']
        u.first_name=first_name
        u.email=email
        u.username=username
        u.save()
        return redirect('profile')
    return render(request,'updateprofile.html',{'u':u,'count_':count_(request)})

def changepassword(request, id):
    u=User.objects.get(id=id)
    invalid=''
    if request.method=='POST':
        current_password=request.POST['current_password']
        new_password=request.POST['new_password']
        if u.password==current_password:
            u.password=new_password
            u.save()
            logout(request)
            return redirect('signin')
        else:
            invalid='Invalid current password'
    return render(request,'changepassword.html',{'u':u,'invalid':invalid,'count_':count_(request)})

def deleteprofile(request, id):
    u=User.objects.get(id=id)
    u.delete()
    logout(request)
    return redirect('signin')

def logout_(request):
    logout(request)
    return redirect('signin')
    
def aboutus(request):
    return render(request,'aboutus.html',{'count_':count_(request)})

def orderplaced(request):
    c=Cart.objects.all()
    c.delete()
    return render(request,'orderplaced.html')


