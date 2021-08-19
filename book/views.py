from django.shortcuts import render,redirect
from .forms import *
from .models import *
import random
from django.db.models import Sum
from datetime import date

# Create your views here.
def index(request):
    return render(request, 'book/index.html')

def std(request):
    if request.method == 'POST':
        form=student_form(request.POST)
        if form.is_valid():
            name= form.cleaned_data['name']
            
            f_name= form.cleaned_data['f_name']
            m_name= form.cleaned_data['m_name']
            mobile= form.cleaned_data['mobile']
            email= form.cleaned_data['email']
            age= form.cleaned_data['age']
            
            savedata=student(name=name,f_name=f_name,m_name=m_name,mobile=mobile,email=email,age=age)
            savedata.save()
            form=student_form()
    else:
        form=student_form()    
    formdata=student.objects.all()
    return render(request,'book/students.html',{'itemforms': form, 'showdata': formdata})

def delete_std(request,id):
    if request.method =='POST':
        dlt=student.objects.get(pk=id)
        dlt.delete()
        return redirect('/student/')

def book(request):
    if request.method == 'POST':
        form=books_form(request.POST)
        if form.is_valid():
            b_name= form.cleaned_data['b_name']
            
            publication= form.cleaned_data['publication']
            s_no= form.cleaned_data['s_no']
            edition= form.cleaned_data['edition']
           
            fees= form.cleaned_data['fees']
            
            savedata=books(b_name=b_name,publication=publication,s_no=s_no,edition=edition,fees=fees)
            savedata.save()
            form=books_form()
    else:
        form=books_form()    
    fromdata=books.objects.all()
    return render(request,'book/books.html',{'forms': form, 'show': fromdata})

def delete_book(request,id):
    if request.method =='POST':
        dlt=books.objects.get(pk=id)
        dlt.delete()
        return redirect('/books/')

# def bookmaster(request):
#     if request.method =='POST':
#         form=books_issue_form(request.POST)
#         if form.is_valid():
#             form.save()
#     else:
#         form=books_issue_form()
#     display=b_issue_mt.objects.all()
#     gtotal=display.aggregate(Sum('total'))
#     return render(request,'book/book_issue_m.html',{'bookForm': form, 'displaydata': display, 'gamount': gtotal})

# def delete_bookm(request, id):
#         if request.method == 'POST':
#             dt=b_issue_mt.objects.get(pk=id)
#             dt.delete()
#         return redirect('/books_issue_m/')

# def book_all(request):
#     if request.method == 'POST':
#         pdet=b_issue_mt.objects.all()       
#         for x in pdet:
#              pdet=book_issued_m()
#              #d=master()
#              pdet.s_name=x.s_name
#              pdet.totalm=request.POST.get('total')
#              pdet.date=x.date
#              #d.save()
#              pdet.save()
#         b_issue_mt.objects.all().delete()
#         return redirect('/books_issue_m/')    
#     else:
#         return render(request,'book/book_issue_m.html')



# def bookdetails(request):
#     if request.method =='POST':
#         form=books_issue_detailsform(request.POST)
#         if form.is_valid():
#             form.save()
#     else:
#         form=books_issue_detailsform()
#     display=bk_is_dt.objects.all()
#     return render(request,'book/book_issue_d.html',{'bookdetails': form, 'detailsdata': display})

# def delete_bookd(request, id):
#         if request.method == 'POST':
#             dt=bk_is_dt.objects.get(pk=id)
#             dt.delete()
#         return redirect('/books_issue_d/')

# def book_d_all(request):
#     if request.method == 'POST':
#         det=bk_is_dt.objects.all()       
#         for x in det:
#              det=bk_is_t()
#              #d=master()
#              det.b_is_id=x.b_is_id
#              det.b_m_id=x. b_m_id
#              det.is_upto=x.is_upto
#              det.b_is_id=x.b_is_id
#              det.re_date=x.re_date
#              det.fine=x.fine
#              #d.save()
#              det.save()
#         bk_is_dt.objects.all().delete()
#         res=bk_is_t.objects.all()
#         return redirect('/bookdetails/')    
#     else:
#         return render(request,'book/book_issue_d.html')

# def fine(request):
#      show=bk_is_t.objects.all()
#      return render(request,'book/finedetails.html',{'show':show})


def overalll(request):
    if request.method =='POST':
        form=all_form(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=all_form()
    display=overall.objects.all()
    gtotal=display.aggregate(Sum('total'))
    return render(request,'book/overall.html',{'all': form, 'showall': display, 'gamount': gtotal})



def ovral(request):
    if request.method == 'POST':
        pdet=overall.objects.all()       
        for x in pdet:
             pdet=book_issued_m()
             d=bk_is_t()
             pdet.s_name=x.s_name
             d.std_name=x.s_name
             d.bookname=x.bk_name
             pdet.totalm=request.POST.get('total')
             pdet.date=x.date
             d.iss_date=x.date
             d.save()
             pdet.save()
        overall.objects.all().delete()
        return redirect('/overall/')    
    else:
        return render(request,'book/overall.html')

def dlt_ovrall(request,id):
    if request.method =='POST':
        dlt=overall.objects.get(pk=id)
        dlt.delete()
        return redirect('/overall/')


def returnall(request):
   
        showreturn=bk_is_t.objects.all()
        return render(request, 'book/returnall.html',{'s':showreturn})

def returnupdate(request,id):
    if request.method== 'POST':
        a= bk_is_t1(id)
        a.re_date=request.POST.get('date')
        a.save()

        fine=bk_is_t2(id)
        book=bk_is_t.objects.filter(pk=id)
        for i in book:
            j=i.re_date-i.iss_date
            print(j)
            k=j.days
            print(k)
            l=books.objects.raw('select id ,b_name,fees from book_books where b_name="'+i.bookname+'"')
            for z in l:
                print(z.fees)
                y=k*z.fees
                print(y)
        fine.fine=y
        fine.save()
              
        return redirect('/return/')


def report(request):
    if request.method=="POST":
      fromdate=request.POST.get('formdate')
      todate=request.POST.get('todate')
      searchresult=bk_is_t.objects.raw('select * from book_bk_is_t where iss_date between "'+str(fromdate)+'" and "'+str(todate)+'"')
      return render(request,'book/report.html',{"data":searchresult})
    else:
      return render(request,'book/report.html')