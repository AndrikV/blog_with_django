from django import forms


class CommentForm(forms.Form):
    author = forms.CharField(
        max_length=100,
        label='Your nickname',
        widget=forms.TextInput(attrs={
            "placeholder": "nickname"
        }),
        required=False
    )
    text = forms.CharField(
        widget=forms.Textarea(
            attrs={"placeholder": "I want to write..."}
        )
    )
