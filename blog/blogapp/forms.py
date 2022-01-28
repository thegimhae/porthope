from django import forms
from .models import Post, Category

#choices = [('announcement','announcement'),('letter','letter'),('prayer','prayer'),('picture','picture'),('bible study','bible study'), ('Devotion','Devotion'),]
choices = Category.objects.all().values_list('name','name')

choice_list = []

for item in choices:
    choice_list.append(item)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'author', 'category', 'body')

        widgets = {
            'title':forms.TextInput(attrs = {'class':'form-control','placeholder':'Please select the category'}),
            'author':forms.Select(attrs = {'class':'form-control'}),
            'category':forms.Select(choices=choice_list, attrs = {'class':'form-control'}),
            'body':forms.Textarea(attrs = {'class':'form-control'}),
        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body')

        widgets = {
            'title':forms.TextInput(attrs = {'class':'form-control','placeholder':'This is Title Placeholder'}),
            # 'author':forms.Select(attrs = {'class':'form-control'}),
            'body':forms.Textarea(attrs = {'class':'form-control'}),
        }
