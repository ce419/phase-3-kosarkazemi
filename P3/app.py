from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

class P3Config(AppConfig):
    name = 'P3'
    verbose_name = _('P3')

    def ready(self):
        import P3.signals