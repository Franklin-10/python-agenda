from django import forms
from django.core.exceptions import ValidationError
from contact.models import Contact


class ContactForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Seu nome',
            }
        ),
        label='Primeiro Nome',
        help_text='Texto de ajuda'
    ) 

    def __init__(self, *args, **kwargs ):
        super().__init__(*args, **kwargs)

        # self.fields['first_name'].widget.attrs.update({
        #     'placeholder':'Olha aqui',
        # })
    class Meta:
        model = Contact
        fields = ('first_name', 'last_name', 'phone','email','description','category')
        # widgets = {
        #     'first_name': forms.TextInput(
        #         attrs={
        #             'placeholder': 'Escreva aqui',
        #         }
        #     )
        # }
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

        # self.add_error(
        #     'first_name',
        #     ValidationError(
        #         'Mensagem de erro',
        #         code='invalid'
        #     )
        # )
        # self.add_error(
        #     'first_name',
        #     ValidationError(
        #         'Mensagem de erro2',
        #         code='invalid'
        #     )
        # )
    
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