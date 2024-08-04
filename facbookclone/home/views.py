from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from .models import Person, Loginto, Suggestion, FriendRequest, Friends, Profile
from django.contrib.auth import authenticate, login, logout
from .form import BlogPostForm

# Create your views here.
def login(request):
    return render(request, "home/index.html")


def createAccount(request):
    check = False
    if request.method == "POST":
        fname = request.POST.get("fname")
        phone = request.POST.get("phone_number")
        password = request.POST.get("password")
        email = request.POST.get("email")
        gender = request.POST.get("gender")
        lname = request.POST.get("lname")
        dob = request.POST.get("dob")
        user = Loginto(first_name = fname, last_name=lname, username=phone, password=password, dob=dob, email=email, gender=gender)
        check = True
        data = {"check":check, "phone":phone, "fname":fname, "lname":lname, "email":email, "dob":dob, "gender":gender}
        user.save()

    return render(request, "home/about.html", data)


def home(request, phone):
    if request.method=="POST":
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        email = request.POST.get("email")
        phone = request.POST.get("phone_number")
        gender = request.POST.get("gender")
        dob = request.POST.get("dob")
        school = request.POST.get("school")
        college = request.POST.get("college")
        company = request.POST.get("company")
        person = Person(first_name=fname, last_name=lname, email=email, phone=phone, gender=gender, dob=dob, school=school, college=college, company=company)
        person.save()
    datas = Profile.objects.all()
    arr = []
    for data in datas:
        dat = Person.objects.filter(phone=data.phone).first()
        arr.append([dat.first_name, dat.last_name, dat.phone, data.textField, data])
    return render(request, "home/home.html", {"check":True, "phone":phone, "data":arr})


def log_in(request):
    check = False
    if request.method == "POST":
        phone = request.POST.get("phone")
        password = request.POST.get("password")
        try:
            user_check = Loginto.objects.filter(username=phone, password=password)
            if user_check is None:
                return render(request, "home/index.html")
            else:
                check = True
                datas = Profile.objects.all()
                arr = []
                for data in datas:
                    dat = Person.objects.filter(phone=data.phone).first()
                    arr.append([dat.first_name, dat.last_name, dat.phone, data.textField, data])
                return render(request, "home/home.html", {"check":check, "phone":phone, "data":arr})
        except:
            return render(request, "home/index.html")


def contact(request, phone):
    if request.method=="POST":
        phones = request.POST.get("phone")
        email = request.POST.get("email")
        suggestion = request.POST.get("suggestion")
        suggest = Suggestion(phone=phones, email=email, suggestion=suggestion)
        suggest.save()
        return render(request, "home/contact.html", {"phone":phone, "email":email})
    else:
        try:
            user_check = Person.objects.filter(phone=phone).first()
            if user_check is None:
                return render(request, "hone/index.html")
            else:
                return render(request, "home/contact.html", {"phone":phone, "email":user_check.email})
        except:
            return render(request, "home/index.html")


def abouts(request, phone):
    person = Loginto.objects.filter(username=phone).first()
    persons = Person.objects.filter(phone=phone).first()
    check = True
    if persons:
        data = {"check": check, "phone": phone, "fname": persons.first_name, "lname": persons.last_name, "email": persons.email, "dob": persons.dob,
                "gender": persons.gender, "school":persons.school, "college":persons.college, "company":persons.company}
    else:
        data = {"check": check, "phone": phone, "fname": person.first_name, "lname": person.last_name, "email": person.email, "dob": person.dob,
                "gender": person.gender}
    return render(request, "home/about.html", data)


def find(request, phone):
    check = True
    data = Person.objects.exclude(phone=phone)
    check_data = FriendRequest.objects.all()
    data_arr = []
    for data in data:
        data_arr.append([data.first_name, data.last_name, data.phone])
    arr = []
    for data in check_data:
        if data.frm == phone:
            check_data_arr = Person.objects.filter(phone=data.to).first()
            arr.append([check_data_arr.first_name, check_data_arr.last_name, data.to])
    if arr:
        value_check = True
    else:
        value_check = False
    return render(request, "home/find.html", {'check':check, "phone":phone, "data":data_arr, "check_data":arr, "value_check":value_check})


def findus(request, phone, phons):
    check = True
    datas = Person.objects.filter(phone=phons).first()
    user = FriendRequest(to=phons, frm=phone, state=False)
    user.save()
    check_data = FriendRequest.objects.all()
    data = Person.objects.exclude(phone=phone)
    data_arr = []
    for data in data:
        data_arr.append([data.first_name, data.last_name, data.phone])
    arr = []
    for data in check_data:
        if data.frm == phone:
            check_data_arr = Person.objects.filter(phone=data.to).first()
            arr.append([check_data_arr.first_name, check_data_arr.last_name, data.to])
    if arr:
        value_check = True
    else:
        value_check = False
    return render(request, "home/find.html", {'check':check, "phone":phone, "data":data_arr, "check_data":arr, "value_check":value_check})


def request(request, phone):
    check = True
    user = FriendRequest.objects.all()
    data_arr = []
    for data in user:
        if data.to == phone:
            check_user = Person.objects.filter(phone=data.frm).first()
            data_arr.append([check_user.first_name, check_user.last_name, data.frm])
    return render(request, "home/request.html", {'check':check, "phone":phone, "data":data_arr})


def cancel(request, phone, phons):
    # item = get_object_or_404(FriendRequest, to=phons, frm=phone)
    item = FriendRequest.objects.filter(to=phons, frm=phone)
    deleted_count, _ = item.delete()
    check = True
    data = Person.objects.exclude(phone=phone)
    check_data = FriendRequest.objects.all()
    data_arr = []
    for data in data:
        data_arr.append([data.first_name, data.last_name, data.phone])
    arr = []
    for data in check_data:
        if data.frm == phone:
            check_data_arr = Person.objects.filter(phone=data.to).first()
            arr.append([check_data_arr.first_name, check_data_arr.last_name, data.to])
    if arr:
        value_check = True
    else:
        value_check = False
    return render(request, "home/find.html",
                  {'check': check, "phone": phone, "data": data_arr, "check_data": arr, "value_check": value_check})


def cancels(request, phone, phons):
    item = FriendRequest.objects.filter(to=phone, frm=phons)
    deleted_count, _ = item.delete()
    check = True
    user = FriendRequest.objects.all()
    data_arr = []
    for data in user:
        if data.to == phone:
            check_user = Person.objects.filter(phone=data.frm).first()
            data_arr.append([check_user.first_name, check_user.last_name, data.frm])
    return render(request, "home/request.html", {'check': check, "phone": phone, "data": data_arr})


def accept(request, phone, phons):
    item = FriendRequest.objects.filter(to=phone, frm=phons)
    deleted_count, _ = item.delete()
    data = Friends(friend=phons, of=phone)
    data.save()
    check = True
    user = FriendRequest.objects.all()
    data_arr = []
    for data in user:
        if data.to == phone:
            check_user = Person.objects.filter(phone=data.frm).first()
            data_arr.append([check_user.first_name, check_user.last_name, data.frm])
    return render(request, "home/request.html", {'check': check, "phone": phone, "data": data_arr})


def friends(request, phone):
    friend = Friends.objects.all()
    arr = []
    for frnd in friend:
        if frnd.friend == phone or frnd.of == phone:
            dat = frnd.friend if frnd.friend != phone else frnd.of
            data = Person.objects.filter(phone=dat).first()
            arr.append([data.first_name, data.last_name, dat])
    return render(request, "home/friends.html", {"check":True, "phone":phone, "data":arr})


def remove_friend(request, phone, phons):
    friend = Friends.objects.filter(friend=phone, of=phons)
    if friend:
        deleted_count, _ = friend.delete()
    else:
        friend = Friends.objects.filter(friend=phons, of=phone)
        deleted_count, _ = friend.delete()
    friend = Friends.objects.all()
    arr = []
    for frnd in friend:
        if frnd.friend == phone or frnd.of == phone:
            dat = frnd.friend if frnd.friend != phone else frnd.of
            data = Person.objects.filter(phone=dat).first()
            arr.append([data.first_name, data.last_name, dat])
    return render(request, "home/friends.html", {"check": True, "phone": phone, "data": arr})


def profile(request, phone):
    form = BlogPostForm()
    datas = Profile.objects.filter(phone=phone)
    dat = Person.objects.filter(phone=phone).first()
    arr = []
    for data in datas:
        arr.append([dat.first_name, dat.last_name, data.phone, data.textField, data])
    return render(request, "home/profile.html", {"check":True, "phone":phone, "form":form, "data":arr})


def upload(request, phone):
    if request.method == "POST":
        form = BlogPostForm(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            form.save()
    else:
        form = BlogPostForm()
    datas = Profile.objects.filter(phone=phone)
    dat = Person.objects.filter(phone=phone).first()
    arr = []
    for data in datas:
        arr.append([dat.first_name, dat.last_name, data.phone, data.textField, data])
    return render(request, "home/profile.html", {"check":True, "phone":phone, "form":form, "data":arr})


def lig(request):
    return render(request, "home/index.html")