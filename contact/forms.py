from django import forms
from django.forms import formset_factory
from .models import Contact


# region type1

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone = forms.CharField(max_length=20)
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)

# endregion


# region type2

class ModelFormContact(forms.ModelForm):

    class Meta:
        model = Contact
        fields = "__all__"

# endregion


# region type3

ContactFormSet = formset_factory(ContactForm, extra=3)

# endregion