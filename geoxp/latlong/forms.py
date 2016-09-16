from django import forms

class UploadFileForm(forms.Form):
    attrs = {
	'class' : 'network-name',
        'onchange' : 'javascript:this.form.submit();',
    }

    file = forms.FileField(label='', widget=forms.FileInput(attrs=attrs))
