from django import forms


class CVForm(forms.Form):
    cv = forms.FileField(
        widget=forms.ClearableFileInput(
            attrs={
                "class": "custom-file-input",
                "id": "validatedCustomFile",
                "required": True,
            }
        )
    )
