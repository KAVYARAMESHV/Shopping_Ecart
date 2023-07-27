import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse
from myapp.models import *
from django.utils import timezone
from django.core.files.storage import FileSystemStorage


# Create your views here.

def laucning(request):
    return render(request,'launch.html')


def loginpage(request):
    return render(request,'login.html')

def login_post(request):
    uname = request.POST['Email']
    pwrd = request.POST['Password']
    if login.objects.filter(username=uname, password=pwrd).exists():
        lg = login.objects.get(username=uname, password=pwrd)
        if lg.type == 'shop':
            request.session['id'] = lg.id
            print(lg.type,"typeeeeeeeeee")
            print("LOgIN ID",request.session['id'])
            return redirect(homepage)
        elif lg.type == 'user':
            request.session['id'] = lg.id
            print("LOgIN ID",request.session['id'])
            return redirect(userhome)

        else:
            print(type)
            return HttpResponse("<script>alert('User Not Found');window.location='/myapp/login/'</script>")
    else:
        return HttpResponse("<script>alert('User Not Found');window.location='/myapp/login/'</script>")


def homepage(request):
   return render(request,'shop/index.html')

#------------------------------
#  product management

def add_product(request):
   return render(request, 'shop/add_prduct.html')

def product_post(request):
    name = request.POST['textfield']
    descr = request.POST['textarea']
    pricE = request.POST['textfield2']
    photo = request.FILES['fileField']
    fs = FileSystemStorage()
    s = datetime.datetime.now().strftime("%y%m%d%H%M%S") + ".jpg"
    fn = fs.save(s, photo)
    pobj = product()
    pobj.productname = name
    pobj.description = descr
    pobj.photo = fs.url(s)
    pobj.price =pricE
    pobj.save()
    return redirect('/myapp/product/')

def view_product(request):
   res = product.objects.all()
   return  render(request,'shop/view_product.html',{'data':res})

def delete_product(request,id):
    res = product.objects.get(id=id).delete()
    return redirect('/myapp/view_product/')


def edit_product(request,id):
    res = product.objects.get(id=id)
    return render(request,'shop/edit.html',{'data':res})

def edit_post(request):
    pid = request.POST['pid']
    productname = request.POST['textfield']
    description = request.POST['textarea']
    price = request.POST['textfield2']
    if 'fileField' in request.FILES:
        photo = request.FILES['fileField']
        if photo.name != '':
            fs = FileSystemStorage()
            s = datetime.datetime.now().strftime("%y%m%d%H%M%S") + ".jpg"
            fn = fs.save(s, photo)
            res = product.objects.filter(pk=pid).update(productname=productname, description=description,
                                                        price=price, photo=s)
        else:
            res = product.objects.filter(pk=pid).update(productname=productname, description=description,
                                                        price=price)
    else:
        res = product.objects.filter(pk=pid).update(productname=productname, description=description,
                                                    price=price)
    return HttpResponse('''<script>alert('Update Successfully');window.location="/myapp/view_product/"</script>''')


def view_users(request):
    res = user.objects.all()
    return render(request,'shop/view_user.html',{'data':res})


def view_orders(request):
    res = ordermain.objects.all()
    return render(request,'shop/view_orders.html',{'data':res})

def viewmore(request,id):
    res = ordersub.objects.filter(ORDER_id=ordermain.objects.get(id=id))
    return render(request,'shop/viewmore.html',{'data':res})

def update_status(request,id):
    res = ordermain.objects.filter(pk=id).update(Status='Delivered')
    return redirect(view_orders)



#  user begins    -------------------------
def signup(request):
    return render(request,'user/signup.html')

def signup_post(request):
    uname = request.POST['Name']
    email = request.POST['Email']
    phone = request.POST['phone']
    pswrd = request.POST['Password']
    cnfpswrd = request.POST['Password2']

    lobj = login()
    lobj.username = email
    lobj.password = cnfpswrd
    lobj.type = 'user'
    lobj.save()

    sobj = user()
    sobj.name = uname
    sobj.email = email
    sobj.phone = phone
    sobj.LOGIN = lobj
    sobj.save()

    return HttpResponse('''<script>alert('Signup Successfully');window.location="/myapp/login/"</script>''')

def userhome(request):
    return render(request,'user/index.html')

def saveadrs(request):
    return render(request,'user/save adrs.html')

def savedrs_post(request):
    name = request.POST['sname']
    phn = request.POST['sphone']
    house = request.POST['house']
    place = request.POST['place']
    rdname = request.POST['road']
    landmark = request.POST['lm']
    typeofadrs = request.POST['radioGroup']
    pin = request.POST['pin']

    lid = request.session['id']

    saveobj = useradrres()
    saveobj.USER = user.objects.get(LOGIN_id=lid)
    saveobj.name = name
    saveobj.phone = phn
    saveobj.house = house
    saveobj.place = place
    saveobj.roadname = rdname
    saveobj.landmark = landmark
    saveobj.adrstype = typeofadrs
    saveobj.pincode = pin

    saveobj.save()
    return redirect(saveadrs)


def viewmyadrs(request):
    lid = request.session['id']
    res = useradrres.objects.filter(USER_id=user.objects.get(LOGIN_id=lid))
    return render(request, 'user/vmyaddress.html',{'data':res})

def delete_adrs(request,id):
    res = useradrres.objects.get(id=id).delete()
    return redirect(viewmyadrs)

def editadrs(request,id):
    res = useradrres.objects.get(id=id)
    return render(request,'user/edit adrs.html',{'data':res})

def edit_adrsPost(request):
    id = request.POST['id']
    name = request.POST['sname']
    phn = request.POST['sphone']
    house = request.POST['house']
    place = request.POST['place']
    rdname = request.POST['road']
    landmark = request.POST['lm']
    typeofadrs = request.POST['radioGroup']
    pin = request.POST['pin']

    res = useradrres.objects.filter(pk=id).update(name=name, phone=phn, house=house, place=place, roadname=rdname,landmark=landmark,adrstype=typeofadrs,pincode=pin)
    return redirect(viewmyadrs)

def userviewproduct(request):
    res = product.objects.all()
    return render(request,'user/products.html',{'data':res})

def addtocart(request,id):
    res = product.objects.get(id=id)
    return render(request,'user/addto_Cart.html',{'data':res})

def cartpost(request):
    lid = request.session['id']
    pid = request.POST['h1']
    qty = request.POST['q1']
    cobj = cart()
    cobj.quantity = qty
    cobj.PRODCUT_id = pid
    cobj.USER = user.objects.get(LOGIN_id=lid)
    cobj.date = datetime.datetime.now()
    cobj.save()
    return redirect(userviewproduct)

def viewcart(request):
    lid =request.session['id']
    res = cart.objects.filter(USER_id=user.objects.get(LOGIN_id=lid))
    tot=0.0
    tam=0.0
    for i in res:
        tot=float(i.quantity) * float(i.PRODCUT.price)
        tam += tot
    return render(request,'user/mycart.html',{'data':res,'tot':tam})

def deletcart(request,id):
    res = cart.objects.get(id=id).delete()
    return redirect(viewcart)


def payment_page(request):
    lid = request.session['id']

    cart_items = cart.objects.filter(USER_id=user.objects.get(LOGIN_id=lid))
    total_amount = sum(int(item.PRODCUT.price) * int(item.quantity) for item in cart_items)
    adrs = useradrres.objects.filter(USER_id=user.objects.get(LOGIN_id=lid))
    print("Total: ",total_amount)
    return render(request, 'user/purchase.html', {'total_amount': total_amount,'address':adrs})


def process_payment(request):
    if request.method == 'POST':
        lid = request.session['id']
        # lid = user.objects.get(LOGIN_id=id)
        print(lid,"LOGIN ID-----------------------------------------")
        accnt_no = request.POST['acnt_no']
        ifsc = request.POST['ifsc_code']
        amount = request.POST['total_amount']
        addresss = request.POST['adrs']

        try:
            bank_account = Bank.objects.get(account_no=accnt_no, IFSC=ifsc)
        except Bank.DoesNotExist:
            return HttpResponse(" <script>alert('Bank Details Require!');window.location='/myapp/payment/'</script>")

        if float(bank_account.balance) >= float(amount):
            orderm = ordermain()
            orderm.USER = user.objects.get(LOGIN_id=lid)
            orderm.date = timezone.now()
            orderm.Status = 'Order Placed'
            orderm.amount = amount
            orderm.useradrs_id = addresss
            orderm.save()
            cart_items = cart.objects.filter(USER_id=user.objects.get(LOGIN_id=lid))

            for cart_item in cart_items:
                ordersub.objects.create(ORDER=orderm, PRODUCT_id=cart_item.PRODCUT_id, quantity=cart_item.quantity)

            cart_items.delete()

            return HttpResponse("<script>alert('Great! Continue your Shopping');window.location='/myapp/userhome/'</script>")
        else:
            return HttpResponse("<script>alert(' Not Found');window.location='/myapp/payment/'</script>")
    else:
        return HttpResponse("<script>alert('Not Found');window.location='/myapp/payment/'</script>")


def view_myorder(request):
    res = ordermain.objects.all()
    return render(request,'user/viewmyorder.html',{'data':res})


def my_ordermore(request,id):
    res = ordersub.objects.filter(ORDER_id=ordermain.objects.get(id=id))
    return render(request,'user/viewmore.html',{'data':res})

from django.contrib.auth import logout

def logout_view(request):
    request.session.clear()
    logout(request)
    return redirect(loginpage)


def rating_page(request,id):
    res =product.objects.get(id=id)
    return render(request,'user/rating.html',{'data':res})

def send_rating(request):
    txt = request.POST['desc']
    rat = request.POST['r1']

    lid = request.session['id']
    pid = request.POST['h1']
    obj = rating()
    obj.date = timezone.now()
    obj.message = txt
    obj.ratingg = rat
    obj.USER = user.objects.get(LOGIN_id=lid)
    obj.PRODUCT_id = pid
    obj.save()
    return HttpResponse("<script>alert('Success!');window.location='/myapp/userhome/'</script>")