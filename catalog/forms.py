from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_name', 'product_description', 'picture', 'category', 'purchase_price',]

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        self.fields['product_name'].widget.attrs.update({
            'class':'form-control',
            'placeholder':'введите наименование продукта'
        })
        self.fields['product_description'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'введите описание продукта'
        })
        self.fields['category'].widget.attrs.update({
            'class': 'form-control'
        })
        # self.fields['product_name'].widget.attrs.update({
        #     'class': 'form-control',
        #     'placeholder': 'введите наименование продукта'
        # })

    def clean(self):
        cleaned_data = super().clean()
        product_name = cleaned_data.get('product_name')
        product_description = cleaned_data.get('product_description')
        forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                           'радар']

        if product_description:
            for word in forbidden_words:
                if word.lower() in product_description.lower():
                    self.add_error('product_description', f'не может содержать слово "{word}"')

        if product_name:
            for word in forbidden_words:
                if word.lower() in product_name.lower():
                    self.add_error('product_name', f'не может содержать слово "{word}"')

        return cleaned_data
# крипта
# биржа,
# дешево,
# бесплатно,
# обман,
# полиция,
# радар.')
