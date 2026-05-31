from django import forms
from django.core.validators import MinLengthValidator

from .models import User


# user form
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            "email",
            "password",
            "first_name",
            "last_name",
            "gender",
            "weight",
            "height",
            "age",
            "activity_status",
            "target",
        ]

    password = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Пароль от 8-ми символов"}),
        validators=[MinLengthValidator(8)],
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # add CSS class for every widget and placeholders if necessary
        self.fields["gender"].widget.attrs["class"] = "form-select"
        self.fields["activity_status"].widget.attrs["class"] = "form-select"
        self.fields["target"].widget.attrs["class"] = "form-select"

        self.fields["email"].widget.attrs["class"] = "form-control"
        self.fields["email"].widget.attrs["placeholder"] = "example@email.ru"
        self.fields["first_name"].widget.attrs["class"] = "form-control"
        self.fields["first_name"].widget.attrs["placeholder"] = "Иван"
        self.fields["last_name"].widget.attrs["class"] = "form-control"
        self.fields["last_name"].widget.attrs["placeholder"] = "Иванов"
        self.fields["weight"].widget.attrs["class"] = "form-control"
        self.fields["height"].widget.attrs["class"] = "form-control"
        self.fields["age"].widget.attrs["class"] = "form-control"
