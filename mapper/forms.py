from django import forms

section_choices=(
    ("1", "Admin"),
    ("2", "Computer Department"),
    ("3", "IT Department"),
    ("4", "E&TC Department"),
)

identity_choices=(
    ("1", "Student"),
    ("2", "Parent"),
    ("3", "Guardian"),
    ("4", "Others"),
)

class EntryForm(forms.Form):
    student_name=forms.CharField(max_length=100)
    email_id=forms.EmailField(max_length=100)
    phone_number=forms.IntegerField(max_value=99999999999)
    address=forms.CharField(max_length=1000)
    purpose=forms.CharField(max_length=1000)
    section=forms.ChoiceField(choices=section_choices)
    identity=forms.ChoiceField(choices=identity_choices)
    others=forms.CharField(max_length=100)
    ref_no_1=forms.CharField(max_length=100)
    ref_no_2=forms.CharField(max_length=100)

class ExitForm(forms.Form):
    ref_no_1 = forms.CharField(max_length=100)
    ref_no_2 = forms.CharField(max_length=100)