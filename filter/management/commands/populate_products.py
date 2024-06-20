# products/management/commands/populate_products.py

import random

from django.core.management.base import BaseCommand
from faker import Faker
from products.models import Product


class Command(BaseCommand):
    help = 'Populates the database with sample products'

    def handle(self, *args, **kwargs):
        faker = Faker()

        for _ in range(20):  # Change the range to the desired number of products
            title = faker.text(max_nb_chars=50)
            price = round(random.uniform(10.0, 100.0), 2)
            featured = random.choice([True, False])
            Product.objects.create(title=title, price=price, featured=featured)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with sample products'))
