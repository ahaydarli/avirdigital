from django import forms
from django.utils.translation import gettext as _

class ContactForm(forms.Form):
    full_name = forms.CharField(required=True, label=_('Full Name'), widget=forms.TextInput(attrs={'placeholder': _('Full Name')}))
    email = forms.EmailField(required=True, label=_('Email'), widget=forms.TextInput(attrs={'placeholder': _('Email')}))
    phone = forms.CharField(required=True, label=_('Phone'), widget=forms.TextInput(attrs={'placeholder': _('Phone')}))
    message = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={'placeholder': _('Your Message')}),
        label=_('Your Message')
    )
