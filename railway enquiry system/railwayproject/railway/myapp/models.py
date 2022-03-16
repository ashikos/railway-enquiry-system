from calendar import month_abbr
from django.db import models
from django.forms import CharField, IntegerField
from django.contrib.auth.models import AbstractUser 

class train_reg(models.Model):
    
    train_no=models.CharField(max_length=300)
    d_place=models.CharField(max_length=300)
    a_place=models.CharField(max_length=300)
    
    d_time=models.TimeField(max_length=300)
    a_time=models.TimeField(max_length=200)


    

class admin(AbstractUser):
    email=models.EmailField(max_length=300)
    fname=models.CharField(max_length=300)
    lname=models.CharField(max_length=300)
    is_admin = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)
    


class customer(models.Model):
    Choice_status = [('aluva','0'), ('Pulinchodu','1'),('Companypady','2'),
    ('Ambattukavu','3'),('Muttom','4'),('Kalamassery','5'),('Cochin University','6'),('Pathadipalam','7'),
    ('Edapally','8'),('Changampuzha park','9'),('Palarivattom','10'),('JLN Stadium','11'),('Kaloor','12'),
    ('Town hall','13'),('MG Road','14'),('Maharajas College','15'),('Ernakulam South','16'),('Kadavanthara','17'),('Elamkulam','18'),
    ('Vytilla','19'),('Thykoodam','20'),('Petta','21')]
    train_no=models.CharField(max_length=300)
    firstName=models.CharField(max_length=300) 
    lastName=models.CharField(max_length=300)
    email=models.EmailField(max_length=300)
    contact_no=models.IntegerField()
    c_from=models.CharField(max_length=300)
    c_to=models.CharField(max_length=300)
    date=models.DateField()
    passenger=models.IntegerField()
    uname=models.CharField(max_length=300,default='None')



class billing(models.Model):
    train_no=models.CharField(max_length=100)
    firstName=models.CharField(max_length=300) 
    lastName=models.CharField(max_length=300)
    email=models.EmailField(max_length=300)
    contact_no=models.IntegerField()
    c_from=models.CharField(max_length=300)
    c_to=models.CharField(max_length=300)
    date=models.CharField(max_length=500)
    passenger=models.IntegerField()
    payement=models.IntegerField()
    ac_no=models.IntegerField()
    ex_date=models.DateField()
    cvv=models.IntegerField()
    holder=models.CharField(max_length=300)
    uname=models.CharField(max_length=300,default='None')




















