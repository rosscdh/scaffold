from django import forms
from oscar.apps.dashboard.catalogue.forms import ProductForm as OscarProductForm


class ProductForm(OscarProductForm):
    data = forms.CharField(widget=forms.Textarea(attrs={'class': 'no-widget-init'}))

    class Meta(OscarProductForm.Meta):
        fields = [
            'title',
            'upc',
            'description',
            'is_discountable',
            'structure',
        ]

        widgets = {
            'structure': forms.HiddenInput(),
        }
