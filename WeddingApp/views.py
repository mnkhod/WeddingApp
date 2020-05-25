from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages as msg
from django.contrib.auth import logout
from .models import Hurimiin_Yslol_Uilchilgee
from .models import Tureesiin_Uilchilgee
from .models import Neriin_Buteegdehuun
from .models import Surgalt
from .models import Hamtragch_Baiguulgiin_Zuuchlah_Uilchilgee
from .models import Cart , Calender
from .forms import LoginForm,RegisterForm
import datetime

from django.contrib.auth import authenticate, login

def logoutview(req):
    logout(req)
    msg.success(req,'Системээс хэрэглэгч амжилттай гарж чадлаа!')
    return redirect('main')

def cartAdd(req):
    item_id = req.POST['itemID']
    item_name = req.POST['itemName']
    item_sub = None

    try :
        user_item = Cart.objects.get(userId_id=req.user.id)
    except Cart.DoesNotExist :
        user_item = Cart(userId=req.user)
        user_item.save()

    if(item_name == 'Hurimiin_Yslol_Uilchilgee'):
        item_sub = Hurimiin_Yslol_Uilchilgee.objects.get(pk=item_id)
        user_item.yslol.add(item_sub)

    if(item_name == 'Calender'):
        item_sub = Calender(title=req.POST['title'],start=req.POST['start'])
        item_sub.save()
        user_item.calenders.add(item_sub)

    if(item_name == 'Tureesiin_Uilchilgee'):
        item_sub = Tureesiin_Uilchilgee.objects.get(pk=item_id)
        user_item.turees.add(item_sub)

    if(item_name == 'Neriin_Buteegdehuun'):
        item_sub = Neriin_Buteegdehuun.objects.get(pk=item_id)
        user_item.neriin.add(item_sub)

    if(item_name == 'Surgalt'):
        item_sub = Surgalt.objects.get(pk=item_id)
        user_item.surgalt.add(item_sub)

    if(item_name == 'Hamtragch_Baiguulgiin_Zuuchlah_Uilchilgee'):
        item_sub = Hamtragch_Baiguulgiin_Zuuchlah_Uilchilgee.objects.get(pk=item_id)
        user_item.hamtragch.add(item_sub)


    user_item.save()

    msg.success(req,'Сагсанд Нэмж Чадлаа!')

    return redirect('/#'+ item_name + item_id)

def main(req):
    size = 0
    if req.user.is_authenticated:
        try :
            user_item = Cart.objects.get(userId_id=req.user.id)
            cart_size = 0;
            cart_size += user_item.yslol.all().count()
            cart_size += user_item.surgalt.count()
            cart_size += user_item.neriin.count()
            cart_size += user_item.turees.count()
            cart_size += user_item.hamtragch.count()
            if cart_size == 0:
                req.session["cartSize"] = 0
            else :
                req.session["cartSize"] = cart_size
                size = req.session["cartSize"] = cart_size
        except Cart.DoesNotExist :
            user_item = Cart(userId=req.user)
            user_item.save()

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
        'cartSize' : size
    })

def zahialga(req):
    user_item = Cart.objects.get(userId_id=req.user.id)
    user_item.yslol.through.objects.all().delete()
    user_item.surgalt.through.objects.all().delete()
    user_item.neriin.through.objects.all().delete()
    user_item.turees.through.objects.all().delete()
    user_item.hamtragch.through.objects.all().delete()

    user_item.save()

    msg.success(req,'Захиалга Хүлээж Авлаа! Та Илүү Мэдээллийг Эмайл Хаягнаасаа Аваарай!')
    return redirect('main')

def cart(req):
    if not req.user.is_authenticated:
        msg.success(req,'Та Нэвтэрч Орно Уу!')
        return redirect('login')

    size = 0
    if req.user.is_authenticated:
        try :
            user_item = Cart.objects.get(userId_id=req.user.id)
            cart_size = 0;
            cart_size += user_item.yslol.all().count()
            cart_size += user_item.surgalt.count()
            cart_size += user_item.neriin.count()
            cart_size += user_item.turees.count()
            cart_size += user_item.calenders.count()
            cart_size += user_item.hamtragch.count()
            if cart_size == 0:
                req.session["cartSize"] = 0
            else :
                req.session["cartSize"] = cart_size
                size = req.session["cartSize"] = cart_size
        except Cart.DoesNotExist :
            user_item = Cart(userId=req.user)
            user_item.save()

    yslol = user_item.yslol.all()
    surgalt = user_item.surgalt.all()
    neriin = user_item.neriin.all()
    calender = user_item.calenders.all()
    turees = user_item.turees.all()
    baiguulga = user_item.hamtragch.all()

    return render(req,'cart.html',{ 'user' : req.user,
        'yslol' : yslol,
        'surgalt' : surgalt,
        'neriin' : neriin,
        'turees' : turees,
        'baiguulga' : baiguulga,
        'calenders' : calender,
        'cartSize' : size
       })

def loginview(req):
    invalid = None

    size = 0
    if req.user.is_authenticated:
        try :
            user_item = Cart.objects.get(userId_id=req.user.id)
            cart_size = 0;
            cart_size += user_item.yslol.all().count()
            cart_size += user_item.surgalt.count()
            cart_size += user_item.neriin.count()
            cart_size += user_item.turees.count()
            cart_size += user_item.hamtragch.count()
            if cart_size == 0:
                req.session["cartSize"] = 0
            else :
                req.session["cartSize"] = cart_size
                size = req.session["cartSize"] = cart_size
        except Cart.DoesNotExist :
            user_item = Cart(userId=req.user)
            user_item.save()

    if req.method == 'POST':
        form = LoginForm(req.POST)

        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(req,username=cd['username'],password=cd['password'])

            if user is not None:
                if user.is_active:
                    login(req,user)
                    msg.success(req,'Амжилттай нэвтэрч чадлаа!')
                    return redirect('main')
                else:
                    msg.success(req,'Энэ хэрэглэгч орж болохгүй')
                    return redirect('loginview')
            else:
                form = LoginForm()
                invalid = 'Tийм хэрэглэгч байхгүй байна!'
                return render(req,'login.html',{'form': form , 'invalid' : invalid})
    else:
        form = LoginForm()

    return render(req,'login.html',{'form': form , 'invalid' : invalid,'cartSize' : size })

def register(req):
    done = None
    taken = None

    size = 0
    if req.user.is_authenticated:
        try :
            user_item = Cart.objects.get(userId_id=req.user.id)
            cart_size = 0;
            cart_size += user_item.yslol.all().count()
            cart_size += user_item.surgalt.count()
            cart_size += user_item.neriin.count()
            cart_size += user_item.turees.count()
            cart_size += user_item.hamtragch.count()
            if cart_size == 0:
                req.session["cartSize"] = 0
            else :
                req.session["cartSize"] = cart_size
                size = req.session["cartSize"] = cart_size
        except Cart.DoesNotExist :
            user_item = Cart(userId=req.user)
            user_item.save()

    if req.method == 'POST':
        user_form = RegisterForm(req.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            done = "Амжилттай шинэ хэрэглэгч нэмж чадлаа!"
            return render(req,'register.html',{'user': new_user , 'done' : done,'cartSize' : size })
        else:
            done = "Адилхан нэртэй хэрэглэгч системд байна!"
            return render(req,'register.html',{'done' : done ,'taken' : taken,'cartSize' : size })

    else:
        form = RegisterForm()

    return render(req,'register.html',{'form': form,'done':done,'cartSize' : size })

