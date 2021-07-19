from .models import products
from .models import orders
from .models import feedback
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

def plp_func(request):
    return products.objects.all()


def home_func(request):
    data = []
    for i in products.objects.raw("select * FROM hotel.products order by id desc limit 4"):
        data.append(i)
    return data


def product_func(id):
    return products.objects.get(id=id)


def order_func(request,id):
    try:
        ord = orders()
        ord.name = request.POST['name']
        ord.phone = request.POST['phone']
        ord.address = request.POST['address']
        data = products.objects.get(id = id)
        ord.food = data.name
        ord.price = data.price
        ord.save()
        print("perfect ok")

        return "your order has been recorded, it will reach you soon. thank you for the purchase"

    except:
        print('sorry')

def search_fun(request):
    try:
        word = request.POST['search']
        data = products.objects.get(name = word)
        return [data]
    except:
        print("i am a sorry aliya")


def reg_form(request):
    try:
        user = User()
        user.username = request.POST['name']
        user.first_name = " "
        user.last_name = " "
        user.email = request.POST['email']
        user.password = request.POST['passswrd']
        user.save()
        print("machane ..ath pore aliya")
        return True

    except:
        return False


def log_func(request):
    try:
        username = request.POST['name']
        password = request.POST['password']
        user = User.objects.all()
        for i in user:
            if i.username == username and i.password == password:
                print("mothalaleee...chanka jaga jaga..")
                return True
        raise Exception("")
    except:
        print("thalararuth ramankutti")
        return False

def feed_func(request):
    feed = feedback()
    try:
        feed.name = request.POST['name']
        feed.content = request.POST['text']
        feed.save()
        print("um..um..")
        return "Thank you for your valuable feedback"
        
    except:
        print("sed lyf")
        return "we are unable to store your feebback"