from django.db import models
from datetime import datetime,date
import random
  
from django.db.models.fields import AutoField

# Create your models here.

random = random.randint(0, 1234)
class student(models.Model):
    id = models.AutoField(auto_created = True,serialize = True,primary_key=True)
    name=models.CharField(max_length=50,blank=False)
    roll=models.IntegerField(default = random)
    f_name=models.CharField(max_length=50,blank=False)
    m_name=models.CharField(max_length=50,blank=False)
    mobile=models.BigIntegerField(blank=False)
    email=models.CharField(max_length=70,blank=False)
    age=models.IntegerField()
    status=models.IntegerField(default=1)

    def __str__(self):
        return self.name

#books
class books(models.Model):
    id = models.AutoField(auto_created = True,serialize = True,primary_key=True)
    b_name=models.CharField(max_length=50,blank=False)
    publication=models.CharField(max_length=50,blank=False)
    s_no=models.BigIntegerField(blank=False)
    edition=models.CharField(max_length=70,blank=False)
    fees=models.IntegerField()
    status=models.IntegerField(default=1)

    def __str__(self):
        return self.b_name

#book issue master
# class b_issue_mt(models.Model):
#     id = models.AutoField(auto_created = True,serialize = True,primary_key=True)
#     s_name=models.ForeignKey(student ,on_delete=models.CASCADE)
#     bk_name=models.ForeignKey(books ,on_delete=models.CASCADE)
#     total=models.BigIntegerField(default=1)
#     date=models.DateField(default=date.today())
#     status=models.IntegerField(default=1)

class book_issued_m(models.Model):
     id = models.AutoField(auto_created = True,serialize = True,primary_key=True)
     s_name=models.CharField(max_length=50,blank=False)
     totalm=models.BigIntegerField()
     date=models.DateField(default=date.today())
     status=models.IntegerField(default=1)

     def __str__(self):
        return self.s_name

# class bk_is_dt(models.Model):
#    id = models.AutoField(auto_created = True,serialize = True,primary_key=True)
#    b_is_id=models.ForeignKey(book_issued_m ,on_delete=models.CASCADE)
#    b_m_id=models.ForeignKey(books ,on_delete=models.CASCADE)
#    is_upto=models.BigIntegerField()
#    re_date=models.DateField(default=date.today())
#    fine=models.BigIntegerField(null=True)
#    status=models.IntegerField(default=1)

class bk_is_t(models.Model):
  id = models.AutoField(auto_created = True,serialize = True,primary_key=True)
  std_name=models.CharField(max_length=50,blank=False)
  bookname=models.CharField(max_length=50,blank=False)
  iss_date=models.DateField(default=date.today())
  re_date=models.DateField(default=date.today())
  fine=models.BigIntegerField(default=0)
  status=models.IntegerField(default=1)
class bk_is_t1(models.Model):
     re_date=models.DateField()
     class Meta:
         db_table="book_bk_is_t"
         managed=False
  
class bk_is_t2(models.Model):
      fine=models.BigIntegerField()
      class Meta:
         db_table="book_bk_is_t"
         managed=False


class overall(models.Model):
    id = models.AutoField(auto_created = True,serialize = True,primary_key=True)
    s_name=models.ForeignKey(student ,on_delete=models.CASCADE)
    bk_name=models.ForeignKey(books ,on_delete=models.CASCADE)
    total=models.BigIntegerField(default=1)
    date=models.DateField(default=date.today())
    status=models.IntegerField(default=1)
