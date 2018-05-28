from django.shortcuts import render,redirect,HttpResponse
from models import User,UserWishList,EveryoneWishList
import bcrypt
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib import messages


def index(request):
    return render(request,'wishlist/index.html')



def register(request):
    User.objects.validate(request)
    return redirect('/')


def dashboard(request):
    user= User.objects.get(id=request.session['id'])
   
    context = { 
           'user' : User.objects.get(id = request.session['id']),
           'all_users':EveryoneWishList.objects.exclude(user=user)
    }
    return render(request,'wishlist/dashboard.html',context)

def add_wish(request):
    return render(request,'wishlist/add_wish.html')

def addwish(request): # change name
    if request.method == "POST":
        valid = UserWishList.objects.validate_product(request)
        if valid: 
            print 'item added'
            return redirect('/dashboard') # redirect to dash board
        else:
            return redirect('/add_wish')



def login(request):
    if request.method == "POST":
       username = request.POST['username']
       password = request.POST['password']
        
    for key in request.POST:
            if request.POST[key] == "":
                messages.error(request,"Please enter all inputs")
                return redirect('/')

    user = User.objects.filter(username=username)
    if len(user) > 0:
		        # if user exists, check password
        isPassword = bcrypt.checkpw(password.encode(), user[0].password.encode())
        if isPassword:
            request.session['id'] = user[0].id
            return redirect('/dashboard')
        else:
            messages.error(request, "Incorrect username/password combination.")
            return redirect('/')
    else:
        messages.error(request, "User does not exist. Please Register first!")
        return redirect('/')

	               

def logout(request):
    request.session.clear()
    return redirect('/')

def joinwish(request,wish_id):# fix the function name
    new_wish =UserWishList.objects.get(id=wish_id)
    user = User.objects.get(id = request.session['id'])
    user.wishes.add(new_wish)
    EveryoneWishList.objects.create(wish=new_wish,user=user)
    return redirect('/dashboard')

def deletewish(request,wish_id):# remove from only current user
    user= User.objects.get(id = request.session['id'])
    del_wish =EveryoneWishList.objects.get(id=wish_id,user=user)
    del_wish.delete()
    return redirect('/dashboard')

def removewish(request,wish_id):# remove from only current user
    user= User.objects.get(id = request.session['id'])
    rem_wish =UserWishList.objects.get(id=wish_id,user=user)
    rem_wish.delete()
    return redirect('/dashboard')

def desire(request,item_id):
    item_details = UserWishList.objects.get(id=item_id)
    whose_wish = EveryoneWishList.objects.filter(wish=item_id) 
    context={
        'item_details':item_details,
        'whose_wish':whose_wish
    }
    print " in item details"
    return render(request,'wishlist/item_details.html',context)




    

