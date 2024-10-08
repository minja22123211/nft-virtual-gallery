from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'

filmovi=Filmovi.objects.all()
contex={'filmovi':filmovi}
return render(request,'app/filmovi.html',contex)