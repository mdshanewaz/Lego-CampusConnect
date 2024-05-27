from django.apps import AppConfig


class ResumewebConfig(AppConfig):
    name = 'resumeweb'

    def ready(self):
        import resumeweb.signals

