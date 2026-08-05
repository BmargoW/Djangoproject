from itertools import product

from django import forms
from django.core.exceptions import ValidationError

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

    def clean_price(self):
        purchase_price = self.cleaned_data.get('purchase_price')
        if purchase_price <= 0:
            raise ValidationError("Стоимость не должна быть отрицательной")
        return purchase_price



    def clean_picture(self):
        picture = self.cleaned_data.get('picture')
        if picture.size > 50 * 5000 * 4000:
            raise ValidationError("Файл должен быть не больше 50 МБ")

        valid_extensions = ['jpg', 'png']
        if picture.name.lower().split('.')[-1] not in valid_extensions:
            raise ValidationError(f"Неподдерживаемый формат файла. Поддерживаемые форматы: {valid_extensions}")
        return picture


