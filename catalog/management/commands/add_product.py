from django.core.management import call_command, BaseCommand
from catalog.models import Category, Product


class Command(BaseCommand):
    help = "Add products to the database "

    def handle(self, *args, **kwargs):

        Product.objects.all().delete()

        new_category, _ = Category.objects.get_or_create(
            title_name="техника",
            description="это приборы и устройства, которые человек использует в повседневной жизни дома",
        )

        products = [
            {
                "product_name": "климатическая техника",
                "product_description": "устройства, которые помогают создать и поддерживать в помещении комфортный микроклимат",
                "picture": "",
                "category": new_category,
                "purchase_price": 11000,
            },
            {
                "product_name": "техника для кухни",
                "product_description": "устройства, которые помогают нам хранить продукты, готовить пищу, мыть посуду и поддерживать чистоту воздуха на кухне",
                "picture": "",
                "category": new_category,
                "purchase_price": 6000,
            },
            {
                "product_name": "садовая техника",
                "product_description": "устройства, которые помогают ухаживать за участком, садом, огородом и прилегающей территорией",
                "picture": "",
                "category": new_category,
                "purchase_price": 9000,
            },
        ]

        for element in products:
            product, created = Product.objects.get_or_create(**element)
            if created:
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Successfully added product: {product.product_name}"
                    )
                )
            else:
                self.stdout.write(
                    self.style.WARNING(
                        f"Product already exists: {product.product_name}"
                    )
                )
