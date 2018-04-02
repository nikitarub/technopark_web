from django import forms


class CommentForm(forms.Form):
	"""docstring for CommentForm"""
	comment = forms.CharField(max_length=1000, required=True)
	

class AskForm(object):
	"""docstring for AskForm"""
	new_question = forms.CharField(max_length=1000, required=True)
	info = forms.CharField(max_length=1000, required=True)
	tags = forms.CharField(max_length=1000, required=True)
	
		