from django import forms


class LocalSettingsForm(forms.Form):
    allowed_hosts = forms.CharField(
        label='ALLOWED_HOSTS',
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': "127.0.0.1,localhost"
        })
    )

    db_name = forms.CharField(label='DB Name', required=True)
    db_user = forms.CharField(label='DB User', required=True)
    db_password = forms.CharField(label='DB Password', required=True, widget=forms.PasswordInput(render_value=True))
    db_port = forms.CharField(label='DB Port', required=True)
    db_host = forms.CharField(label='DB Host', required=True)