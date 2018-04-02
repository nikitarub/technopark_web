from django import forms


class SignupForm(forms.Form):
	"""docstring for LoginForm"""
	username = forms.CharField(max_length=30, required=True)
	firstname = forms.CharField(max_length=30)
	lastname = forms.CharField(max_length=30)
	email = forms.EmailField(required=True)
	password = forms.CharField(min_length=8, max_length=30, required=True)
	confirm_password = forms.CharField(min_length=8, max_length=30, required=True)
	# avatar = forms.FileField()

class LoginForm(forms.Form):
	"""docstring for LoginForm"""
	username = forms.CharField(initial='class', required=True)
	email = forms.EmailField(required=True)
	password = forms.CharField(initial='class', min_length=8, max_length=30, required=True)
	