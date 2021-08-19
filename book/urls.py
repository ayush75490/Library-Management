from django.contrib import admin
from django.urls import path
from book import views

urlpatterns = [
    path('',views.index, name='book'),
    path('student/',views.std,name='student'),
    path('delete/<int:id>', views.delete_std, name="deletestd" ),
    path('books/',views.book,name='books'),
    path('delete_books/<int:id>', views.delete_book, name="deletebook" ),
    # path('books_issue_m/',views.bookmaster,name='booksmaster'),
    # path('delete_booksm/<int:id>', views.delete_bookm, name="deletebookm" ),
    # path('bookAll/', views.book_all, name="bookall"),
    # path('delete_booksd/<int:id>', views.delete_bookd, name="deletebookd" ),
    # path('bookdetails/', views.bookdetails, name="bookdetails"),
    # path('book_d_All/', views.book_d_all, name="booksalldetails"),
    path('overall/',views.overalll, name='overall'),
    path('saveoverall/',views.ovral, name='saveoverall'),
    path('delete_overall/<int:id>',views.dlt_ovrall, name='deleteovrall'),
    path('return/',views.returnall, name= 'returnall'),
    path('returnupdate/<int:id>', views.returnupdate),
    path("report/",views.report,name="report"),
]

