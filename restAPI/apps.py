from django.apps import AppConfig

from restAPI.cameras.zed2 import Zed2


class RestapiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'restAPI'

    def ready(self):
        zed2 = Zed2(15).start()
