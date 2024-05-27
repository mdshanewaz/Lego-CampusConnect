from django.apps import AppConfig


class MyDocumentationsConfig(AppConfig):
    name = 'mydocumentations'

    def ready(self):
        import mydocumentations.signals

