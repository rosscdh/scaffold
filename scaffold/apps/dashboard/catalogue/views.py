from oscar.apps.dashboard.catalogue.views import ProductCreateUpdateView as OscarProductCreateUpdateView

from .forms import ProductForm
from scaffold.apps.room.forms import ProductRoomFormSet


class ProductCreateUpdateView(OscarProductCreateUpdateView):
    form_class = ProductForm
    rooms_formset = ProductRoomFormSet

    def __init__(self, *args, **kwargs):
        super(ProductCreateUpdateView, self).__init__(*args, **kwargs)
        self.formsets.update({'rooms_formset': self.rooms_formset})
