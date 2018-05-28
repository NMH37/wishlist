
from __future__ import unicode_literals

from django.db import models
from django.contrib import messages
import bcrypt
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

# Create your models here.


class UserManager(models.Manager):
    def validate(self,request):
        if request.method == "POST":
            valid = True
            for key in request.POST:
                if request.POST[key] == "":
                    messages.error(request,"Please enter {}".format(key))
                    valid = False
            if len(request.POST['password'])< 8:
                valid = False
                messages.error(request,"password must have 8 characters")


            if request.POST['confirmpassword']!= request.POST['password']:
                valid = False
                messages.error(request,"password doesn't match")

            if valid == True:
                # encrypt password 
                password = request.POST['password']
                hashed_pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt())		
                User.objects.create(name=request.POST['name'],username=request.POST['username'],password=hashed_pw,hired=request.POST['hired_date'] )
                messages.success(request,"Successfully Registered, Proceed to login")
                return valid


   
	   



class User(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    hired =  models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()




class ProductManager(models.Manager):
    def validate_product(self,request):
        if request.method == "POST":
            valid = True
            for key in request.POST:
                if request.POST[key] == "":
                    messages.error(request,"Please fill the product field")
                    valid = False
                    return valid
                
                else:
                    valid = True
                    product = request.POST['product'] 
                    user= User.objects.get(id=request.session['id'])
                    wish = UserWishList.objects.create(product= product,user=user)
                    EveryoneWishList.objects.create(wish=wish,user=user)
                    return valid





class UserWishList(models.Model):
    product = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    user = models.ForeignKey(User,related_name="wishes")
    objects = ProductManager()




class EveryoneWishList(models.Model):
    wish = models.ForeignKey(UserWishList,related_name='wishes')
    user = models.ForeignKey(User,related_name='users')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)





    

