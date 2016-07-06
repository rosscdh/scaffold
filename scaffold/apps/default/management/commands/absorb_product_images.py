from __future__ import unicode_literals
from unidecode import unidecode
from django.core.management.base import BaseCommand
from django.utils.translation import ugettext_lazy as _
from django.db.utils import IntegrityError
from django.template.defaultfilters import slugify
from django.core.files.images import ImageFile
from django.core.files import File

from oscar.apps.catalogue.models import Product, ProductImage

import os
import re
import requests
import json

PRODUCTS = json.load(open('/Users/rosscdh/p/wilms.de/extract/products.json'))


class Command(BaseCommand):
    """
    Check stock records of products for availability and send out alerts
    to customers that have registered for an alert.
    """
    help = _("Check for products that are back in "
             "stock and send out alerts")

    def download(self, product, r, path):
        tail, head = os.path.split(path)
        with open(path, 'wb') as handle:
            if r.ok:
                for block in r.iter_content(1024):
                    handle.write(block)
        image = ProductImage(product=product)
        image.product = product
        image.cation = product.title

        with open(path, 'r') as image_file:
            image.original.save(head, File(image_file), save=False)

        try:
            image.save()
        except:
            pass
        return image

    def handle(self, **options):
        """
        Check all products with active product alerts for
        availability and send out email alerts when a product is
        available to buy.
        """
        ProductImage.objects.all().delete()

        for page in PRODUCTS:
            page = page.get('page')
            product = page.get('product')[0]
            image = '/web/%s' % product.get('image')

            tail, head = os.path.split(image)

            pre_title = product.get('title').strip()
            match = re.match(r'^Art-Nr\: (\d+) \- (.*)$', pre_title)

            if match:
                sku, title = match.groups()
            else:
                sku, title = None, pre_title

            title = unidecode(title)
            slug = slugify(title)
            product = Product.objects.filter(slug=slug).first()
            # for product in products:
            if product:
                image = self.download(product=product, r=requests.get('http://www.wilms.de%s' % image), path='./images/%s' % head)
