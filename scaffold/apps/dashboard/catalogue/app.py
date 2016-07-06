from oscar.apps.dashboard.catalogue.app import CatalogueApplication as OscarCatalogueApplication

from oscar.core.loading import get_class


class CatalogueApplication(OscarCatalogueApplication):
    product_createupdate_view = get_class('scaffold.apps.dashboard.catalogue.views',
                                          'ProductCreateUpdateView')

application = CatalogueApplication()
