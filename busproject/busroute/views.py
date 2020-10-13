from django.shortcuts import render,redirect
from .models import register
from busroute.forms import routeForm
from busroute.models import route


def home1(request):
    return render(request,"home1.html")

def home(request):
    return render(request,"home.html")

def index(request):
    return render(request,"index.html")

def signup(request):
    return render(request, "signup.html")

def about(request):
    return render(request, "about.html")



def registersubmit(request):

    srname=request.POST["srname"]
    email = request.POST["email"]
    mno = request.POST["mno"]
    spass= request.POST["spass"]

    r=register(name=srname,email=email,mobileno=mno,password=spass)
    r.save()
    return render(request, "index.html")



def loginsubmit(request):
    z=0
    log =register.objects.all()
    if request.method == "POST":
        name1 = request.POST.get("uname",False)
        password= request.POST.get("psw",False)

        for i in log:
            if(name1==i.name and password== i.password):
                 z=1
                 break
            elif(name1== "admin" and password== "admin"):
                 return  render(request,"adminlogin2.html")
            else:
                z=0

        if (z==1):
            print("Login Successful")
            return redirect("/userlogin/")

        else:
            print("Incorrect Credentials")
            return render(request,"index.html")

    else:
        print("Credentials not entered")
    return render(request,"index.html")

def adminlogin(request):
    return render(request, "adminlogin.html")

def adminlogin2(request):
    return render(request, "adminlogin2.html")

def userlogin(request):
    return render(request,"userlogin.html")
def userlogin1(request):
    return render(request,"userlogin1.html")

def contact(request):
    return render(request,"contact.html")

def broute(request):
    print("Helooo")
    if request.method == "POST":
        form = routeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                print("Hi")
                return redirect("/adminlogin2")
            except:
                print("Unsave")
                pass

    else:
        form = routeForm()
    return render(request,"signup.html",{'form':form})

def show(request):
    routes = route.objects.all()
    return render(request, "show.html", {'routes': routes})

def registeruser(request):
    Register = register.objects.all()
    return render(request, "registeruser.html", {'Register': Register})

def show1(request):
    routes = route.objects.all()
    return render(request, "show1.html", {'routes': routes})

def edit(request, id):
    Route = route.objects.get(id=id)
    return render(request, "edit.html", {'Route': Route})



def update(request, id):
    Route = route.objects.get(id=id)
    form = routeForm(request.POST, instance=Route)
    if form.is_valid():
        form.save()
        return redirect('/show')
    return render(request,"edit.html",{'Route':Route})

def delete(request, id):
    Route = route.objects.get(id=id)
    Route.delete()
    return redirect("/show")

