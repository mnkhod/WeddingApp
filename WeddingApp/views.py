from django.shortcuts import render
from .models import Hurimiin_Yslol_Uilchilgee
from .models import Tureesiin_Uilchilgee
from .models import Neriin_Buteegdehuun
from .models import Surgalt
from .models import Hamtragch_Baiguulgiin_Zuuchlah_Uilchilgee

def main(req):
    yslol = Hurimiin_Yslol_Uilchilgee.objects.all()
    surgalt = Surgalt.objects.all()
    neriin = Neriin_Buteegdehuun.objects.all()
    turees = Tureesiin_Uilchilgee.objects.all()
    baiguulga = Hamtragch_Baiguulgiin_Zuuchlah_Uilchilgee.objects.all()

    return render(req,'index.html',{
        'yslol' : yslol,
        'surgalt' : surgalt,
        'neriin' : neriin,
        'turees' : turees,
        'baiguulga' : baiguulga,
    })
