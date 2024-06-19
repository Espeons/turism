from django import forms

from django.forms import TextInput, EmailInput, Textarea, Select, NumberInput, DateInput

from alex.models import Contact, Rev


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'


        widgets = {
            'name': TextInput(attrs={'placeholder': 'Introduce-ti numele', 'class': 'form-control'}),
            'email': EmailInput(attrs={'placeholder': 'Introduce-ti email-ul', 'class': 'form-control'}),
            'phone_number': NumberInput(
                attrs={'placeholder': 'Introduce-ti numarul de telefon', 'class': 'form-control'}),
            'message': Textarea(
                attrs={'placeholder': 'Introduce-ti mesajul ', 'class': 'form-control', 'rows': 3}),
        }

        def clean(self):
            cleaned_data = super().clean()  # se obtine access la informatiile din formular intr-un dictionar
            print(cleaned_data)

            return cleaned_data


class RevForm(forms.ModelForm):
    class Meta:
        model = Rev
        # exclude = ['first_name']  -> il folosim pt a exclude anumite fielduri din formular / TREBUIE CA IN MODELS.PY SA AVETI BLANK= TRUE SI NULL=TRUE
        fields = '__all__'  # specificam fieldurile dorite in formular
        # fields = ['first_name', 'last_name']

        widgets = {
            'prenumele': TextInput(attrs={'placeholder': 'Please enter your first name', 'class': 'form-control'}),
            'nume': TextInput(attrs={'placeholder': 'Please enter your last name', 'class': 'form-control'}),
            'email': EmailInput(attrs={'placeholder': 'Please enter your email', 'class': 'form-control'}),
            'descriere': Textarea(
                attrs={'placeholder': 'Please enter a description', 'class': 'form-control', 'rows': 3}),
            'start_date': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'excursia': Select(attrs={'class': 'form-select'}),
            'nota': Select(attrs={'class': 'form-select'}),
        }

    # Atunci cand creati sau personalizati un formular in Django puteti sa implementati validari personalizate
    # care se va aplica pe intregul formular

    # Aceasta metoda este folosita pentru a verifica corectitudinea datelor introduse de utilizator
    # inainte de fi procesate sau salve in baza de date

    def clean(self):
        cleaned_data = super().clean()  # se obtine access la informatiile din formular intr-un dictionar
        print(cleaned_data)