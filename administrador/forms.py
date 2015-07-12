from django import forms
from django.core.mail import send_mail


class ContactForm(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'textfield'
            }
        )
    )

    message = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'contact_textarea'
            }
        )
    )

    def send_email(self):
        name = self.cleaned_data['name']
        message = self.cleaned_data['message']

        message = "{0}\n\n{1}".format(
            name,
            message
        )

        send_mail(
            'Mensaje desde Pagina web ITA',
            message,
            'ITA Quejas y sujerencias <mailer@jualjiman.com>',
            ['jualjiman@gmail.com', ],
            fail_silently=False
        )
