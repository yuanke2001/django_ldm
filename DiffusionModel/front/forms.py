from django.contrib.auth import get_user_model
from django import forms  # 注意导入的是django下的forms


class LoginForm(forms.ModelForm):
    telephone = forms.CharField(max_length=11)
    remeber = forms.IntegerField(required=False)

    class Meta:
        model = get_user_model()
        fields = ['password']

