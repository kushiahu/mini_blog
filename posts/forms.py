from django import forms

from posts.models import Post


class PostFormModel(forms.ModelForm):
	class Meta:
		model = Post
		fields = ['title', 'image', 'body']


# class PostForm(forms.Form):
# 	title = forms.CharField(max_length=250, required=True)
# 	image = forms.ImageField(required=True)
# 	body = forms.CharField(widget=forms.Textarea, required=True)


# class PostUpdateForm(PostForm):
# 	image = forms.ImageField(required=False)