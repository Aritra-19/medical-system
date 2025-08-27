from django import forms
from api.models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        if not cleaned_data.get("first_name"):
            raise forms.ValidationError("First name is required.")
        if not cleaned_data.get("last_name"):
            raise forms.ValidationError("Last name is required.")
        if not cleaned_data.get("date_of_birth"):
            raise forms.ValidationError("Date of birth is required.")
        if not cleaned_data.get("phone_number"):
            raise forms.ValidationError("Phone number is required.")
        return cleaned_data