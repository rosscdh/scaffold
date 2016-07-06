from __future__ import unicode_literals
from unidecode import unidecode
from django.core.management.base import BaseCommand
from django.utils.translation import ugettext_lazy as _

from django.template.defaultfilters import slugify

from oscar.apps.catalogue.models import Category, Product, ProductClass, ProductAttribute, ProductAttributeValue, ProductCategory

import re
import json

PRODUCTS = json.load(open('/Users/rosscdh/p/wilms.de/extract/products.json'))


class Command(BaseCommand):
    """
    Check stock records of products for availability and send out alerts
    to customers that have registered for an alert.
    """
    help = _("Check for products that are back in "
             "stock and send out alerts")

    def handle(self, **options):
        """
        Check all products with active product alerts for
        availability and send out email alerts when a product is
        available to buy.
        """
        Product.objects.all().delete()
        Category.objects.all().delete()

        for page in PRODUCTS:
            page = page.get('page')

            category = unidecode(page.get('category')).strip()
            category_slug = slugify(category)
            try:
                cat = Category.objects.get(slug=category_slug, depth=1)
            except Category.DoesNotExist:
                cat = Category(name=category, depth=1)
                cat.path = category_slug
                cat.save()
            except Exception as e:
                import pdb;pdb.set_trace()

            product_type = unidecode(page.get('sub_category')).strip()
            product_type_slug = slugify(product_type)
            pt, pt_is_new = ProductClass.objects.get_or_create(name=product_type)

            product = page.get('product')[0]
            pre_title = product.get('title').strip()
            match = re.match(r'^Art-Nr\: (\d+) \- (.*)$', pre_title)

            if match:
                sku, title = match.groups()
            else:
                sku, title = None, pre_title

            title = unidecode(title)
            slug = slugify(title)
            description = '\n'.join([unidecode(i.get('text').strip()) for i in product.get('description', [])]).strip()

            print product_type, sku, slug, title, description
            p = Product(slug=slug,
                        title=title,
                        product_class=pt,
                        # upc=sku,
                        description=description)
            p.save()

            p.productcategory_set.add(ProductCategory(category=cat, product=p))

            p_attributes = [re.sub(r'[\:\.]', '', unidecode(i.get('text'))) for i in product.get('attr_headers', [])]
            p_codes = [slugify(re.sub(r'[\:\.]', '', unidecode(i.get('text')))) for i in product.get('attr_headers', [])]
            p_values = [unidecode(i.get('text')) for i in product.get('attr_values', [])]
            for name, code, value in zip(p_attributes, p_codes, p_values):
                pa, is_new = ProductAttribute.objects.get_or_create(name=name, code=code)
                pav, pav_is_new = ProductAttributeValue.objects.get_or_create(value_text=value, attribute=pa, product=p)
                pa.productattributevalue_set.add(pav)