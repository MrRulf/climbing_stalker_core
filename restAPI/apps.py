from django.apps import AppConfig

# from restAPI.cameras.zed2 import Zed2


class RestapiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'restAPI'
    measurements_per_second = 15


    # Apps need to be loaded? Error -> phone. Make other tests bc for this one jetson is needed
    # def ready(self):
    #     zed2 = Zed2(self.measurements_per_second).start()
