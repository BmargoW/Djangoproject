from catalog.models import Product


def list_definition(category_id):
    l_p =  Product.objects.filter(category=category_id)
    if not l_p.exists():
        return None
    return l_p


