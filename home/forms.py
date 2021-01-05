from django import forms


from home.models import *


class Publisher_frm(forms.ModelForm):
    class Meta():
        model=Publisher
        fields='__all__'

class Author_frm(forms.ModelForm):
    class Meta():
        model=Author
        fields='__all__'

class Book_frm(forms.ModelForm):
    class Meta():
        model=Book
        fields=['title','publication_date']