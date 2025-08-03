from django import forms
from django.core.exceptions import ValidationError
from contact.models import Contact


class ContactForm(forms.ModelForm):
    picture = forms.ImageField(
         widget=forms.FileInput(
              attrs={
                   'accept': 'image/*',
              }
         )
    )
    class Meta:
        model = Contact
        fields = ('first_name', 'last_name', 'phone','email','description','category', 'picture',)

    def clean(self):
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')

        if first_name == last_name:
                msg =  ValidationError(
                    'Primeiro nome não pode ser igual ao sobrenome',
                    code='invalid'
                )
                self.add_error('last_name', msg)
                self.add_error('first_name', msg)
        return super().clean()
    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if first_name == 'ABC':
            self.add_error(
                'first_name',
                ValidationError(
                    'Não digite ABC',
                    code='invalid'
                )
        )
        return first_name