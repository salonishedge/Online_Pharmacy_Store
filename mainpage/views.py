from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required
from .models import Product
from django.http import  HttpResponseRedirect
from .models import Person
from .forms import SubscribeForm,UserUpdateForm,HotelForm
from .models import Post
from .models import Profile

def createpost(request):
        if request.method == 'POST':
            if request.POST.get('title') and request.POST.get('content'):
                post=Post()
                post.title= request.POST.get('title')
                post.content= request.POST.get('content')
                post.save()
                
                return render(request, 'mainpage/createpost.html',{})  

        else:
                return render(request,'mainpage/createpost.html',{})


# Create your views here. 
def hotel_image_view(request): 
    # Create your views here. 
 
  
    if request.method == 'POST': 
        form = HotelForm(request.POST, request.FILES) 
  
        if form.is_valid(): 
            form.save() 
            return redirect('success') 
    else: 
        form = HotelForm() 
    return render(request, 'mainpage/tp.html', {'form' : form}) 
  
  
def success(request): 
    return HttpResponse('successfuly uploaded')   
    

def profile(request):
	if request.method == 'POST':

		p_form=UserUpdateForm(request.POST, request.FILES)
		if p_form.is_valid():
				p_form.save() 
				messages.success(request,f'Uploaded!')
		return redirect('login')
	else:
		p_form=UserUpdateForm()
	context = {
		'p_form':p_form
	}
	return render(request,'mainpage/hello.html',context)


def success(request): 
    return HttpResponse('successfuly uploaded') 




def home(request):
 
    
    form = SubscribeForm(request.POST)
    
    if form.is_valid():
        # process the data in form.cleaned_data as required
        p = form.save()
        '''
        name = form.cleaned_data['name']
        number = form.cleaned_date['phone_number']
        p = Person(name=name, phone_number=number, date_subscribed=datetime.now(), messages_recieved=0)
        p.save()
        '''
        # redirect to a new URL:
        return HttpResponseRedirect('/success/')
  # if a GET (or any other method) we'll create a blank form    
#	else: 
 #   	form = SubscribeForm()

 #		return render(request, 'texting/index.html', {'form': form})



def tp(request):
	t=Product.objects.all()
	return render(request, 'mainpage/tp.html', {'form': t})
def aboutus(request):
    if request.method == 'POST' :
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your Account Has been created')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})



def db(request):
	print("working")
	return render(request)

	
def hello(request):
   return render(request, 'mainpage/hello.html',{})





def about(request):
	
	return render(request,'mainpage/about.html',{})



def viewproducts(request):
	return render(request,'mainpage/viewproducts.html',{})

def aboutus(request):
	return render(request,'mainpage/aboutus.html',{})
	
def login(request):
	return render(request,'mainpage/login.html',{})
	
def register(request):
	return render(request,'mainpage/register.html',{})
	
def cart(request):
	return render(request,'mainpage/cart.html',{})


