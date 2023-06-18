from django import forms
from .models import Post, BlogUser


class PostForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            print(field)
            field.field.widget.attrs["class"] = "form-control"

    class Meta:
        model = Post
        exclude = ("user",)


class BlogUserForm(forms.ModelForm):

    class Meta:
        model = BlogUser
        exclude = ("user", "name", "last_name", "profession", "profile_image", "interests", "skills")