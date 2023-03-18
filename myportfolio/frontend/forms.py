from django import forms
from .models import *
from django.utils.translation import gettext as _

class DocumentForm(forms.ModelForm):

    file = forms.FileField(label=_('Choose File'),
                            required=True, 
                            error_messages = {'required':'The file field is required.','invalid':_("Files only")}, 
                            widget=forms.FileInput(attrs={'multiple':True, 'class': 'form-control custom-file-input','id' : 'customFile'})
                        )

    class Meta:
        model = portfolio
        fields = ['img',]