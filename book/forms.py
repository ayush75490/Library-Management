from django import forms
from django.forms import widgets 
from .models import *


#student
class student_form(forms.ModelForm):
    class Meta:
        model=student
        fields=['name','f_name','m_name','mobile','email','age',]
        
        widgets={

            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'f_name':forms.TextInput(attrs={'class': 'form-control'}),
            'm_name':forms.TextInput(attrs={'class': 'form-control'}),
            'mobile':forms.NumberInput(attrs={'class': 'form-control'}),
            'email':forms.TextInput(attrs={'class': 'form-control'}),
            'age':forms.NumberInput(attrs={'class': 'form-control'}),
        }
class books_form(forms.ModelForm):
    class Meta:
        model=books
        fields=['b_name','publication','s_no','edition','fees']
        labels={'b_name':'Book Name'}
        widgets={

            'b_name': forms.TextInput(attrs={'class': 'form-control'}),
            'publication':forms.TextInput(attrs={'class': 'form-control'}),
            's_no':forms.NumberInput(attrs={'class': 'form-control'}),
            'edition':forms.TextInput(attrs={'class': 'form-control'}),
            'fees':forms.NumberInput(attrs={'class': 'form-control'}),
            
        }


# class books_issue_form(forms.ModelForm):
#     class Meta:
#         model= b_issue_mt


#         fields=['s_name','bk_name','date']
#         labels={'s_name':'Select Student Name','bk_name':'Book Name'}
#         widgets={

#             's_name': forms.Select(attrs={'class': 'form-control'}),
#             'bk_name': forms.Select(attrs={'class': 'form-control'}),
#             'date':forms.DateInput(format='%Y-%m-%d',attrs={'class':'form-control', 'id': 'date','type':'date'}),
            
#         }


# class books_issue_detailsform(forms.ModelForm):
#     class Meta:
#         model= bk_is_dt

#         fields=['b_is_id','b_m_id','is_upto','re_date','fine']
#         labels={'b_is_id':'Book Issued Details','b_m_id':'Book Master Details','is_upto':'Date Upto' ,'re_date':'Return Date'}
#         widgets={

#             'b_is_id': forms.Select(attrs={'class': 'form-control'}),
#             'b_m_id':forms.Select(attrs={'class': 'form-control'}),
#             'is_upto':forms.NumberInput(attrs={'class': 'form-control'}),
#             're_date':forms.DateInput(format='%Y-%m-%d',attrs={'class':'form-control', 'id': 'date','type':'date'}),
#             'fine':forms.NumberInput(attrs={'class': 'form-control'}),
#         }
        
class all_form(forms.ModelForm):
    class Meta:
        model=overall
        fields=['s_name','bk_name','date']
        labels={'s_name':'Student Name','b_name':'Book Name'}
        widgets={
                's_name':forms.Select(attrs={'class':'form-control'}),
                'bk_name':forms.Select(attrs={'class':'form-control'}),
                'date':forms.DateInput(format='%Y-%m-%d',attrs={'class':'form-control', 'id': 'date','type':'date'}),


        }      