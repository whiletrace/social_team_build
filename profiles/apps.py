from django.apps import AppConfig



class UserProfilesConfig(AppConfig):
    default_auto_field = 'django.db.models.AutoField'
    name = 'profiles'

    def ready(self):
        import profiles.models

