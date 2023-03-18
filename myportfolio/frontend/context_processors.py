from .models import profile as p
def profile(request):
    profil = p.objects.all()
    return {"profile": profil}