# -*- coding: utf-8 -*-
import os
import json
import requests
import tempfile

from django.core import files
from slugify import slugify, Slugify, GERMAN

slugify_de = Slugify(pretranslate=GERMAN)

from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth import get_user_model

from oscar.apps.catalogue.models import Category, ProductClass, ProductCategory, ProductImage
from oscar.apps.catalogue.categories import create_from_breadcrumbs

from scaffold.apps.catalogue.models import Product

User = get_user_model()



class Command(BaseCommand):
    help = 'import cats'

    def handle(self, *args, **options):
        data = json.load(open('reuter-cats.json'))
        product_class = ProductClass.objects.get(slug='reuter-products')
        for page in data.get('page').get('sections'):

            cat = unicode(page.get('cat', None))
            slug = slugify_de(cat, to_lower=True)
            cat, is_new = Category.objects.get_or_create(name=cat)
            #import pdb;pdb.set_trace()
            #print slug
            for sub in page.get('sub_cats'):
                sub_cat = unicode(sub.get('sub_cat'))
                #create_from_breadcrumbs(u' > '.join([cat, sub_cat]))
                sub_cat = slugify_de(sub_cat, to_lower=True)

                #print 'gdom reuter.gdom "https://www.reuter.de/%s/%s.html" > gdom_results/%s.json' % (slug, sub_cat, sub_cat)

                try:
                    print 'gdom_results/%s.json' % sub_cat
                    data2 = json.load(open('./gdom_results/%s.json' % sub_cat))
                except ValueError:
                    data2 = {}

                for page2 in data2.get('page', {}).get('summaries', []):

                    link = page2.get('link')
                    image = page2.get('image')
                    image_url = 'http:%s' % image
                    name = unicode(page2.get('name'))
                    current_price = page2.get('current_price')
                    full_price = page2.get('full_price')
                    product_slug = slugify_de(name, to_lower=True)
                    filename, file_extension = os.path.splitext(image_url)
                    product, is_new = Product.objects.get_or_create(title=name, product_class=product_class)

                    # prod_cat, prod_cat_is_new = ProductCategory.objects.get_or_create(product=product, category=cat)
                    # product.productcategory_set.add(prod_cat)
                    image_resp = requests.get(image_url, stream=True)
                    display_order = product.images.count()
                    image = ProductImage(product=product, display_order=display_order+1)
                    
                    image.original.save('%s-%s%s' % (sub_cat, product_slug, file_extension), files.base.ContentFile(image_resp.content), save=True)

                    # if is_new is True:
                    #     product.save()
                    



    