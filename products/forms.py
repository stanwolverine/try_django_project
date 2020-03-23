from django import forms
from .models import Product


class ProductCreateForm(forms.ModelForm):
    email = forms.EmailField()
    title = forms.CharField(
        label='',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Type title here',
                'style': 'border-radius: 20px; border-color: violet; outline: none; padding: 8px'
            }
        )
    )
    description = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={'placeholder': 'Your description',
                   'class': 'new-class-name two', 'rows': 10, 'cols': 20}
        )
    )

    class Meta:
        model = Product
        # note that email field is not here, meaning we can render extra fields.
        fields = ['title', 'description', 'price', 'mrp', 'featured']

    # overriding title validation
    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get('title')
        if 'CFE' not in title:
            raise forms.ValidationError('This is not a valid title: "CFE"')
        if not 'news' in title:
            raise forms.ValidationError('This is not a valid title: "news"')
        return title

    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        if not email.endswith(".com"):
            raise forms.ValidationError('Please enter a valid email address')
        return email


class RawProductForm(forms.Form):
    title = forms.CharField(
        label='',
        widget=forms.TextInput(
            attrs={'placeholder': 'Type title here'}
        )
    )
    description = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={'placeholder': 'Your description',
                   'class': 'new-class-name two', 'rows': 10, 'cols': 20}
        )
    )
    mrp = forms.DecimalField()
    price = forms.DecimalField()
    featured = forms.BooleanField(initial=True)
