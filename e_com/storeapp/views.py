from django.shortcuts import render,redirect
from .models import Products

from .serializers import ProductSerializer

#serializer_view
from rest_framework.response import Response
#permissions,viewsets 
from rest_framework import generics ,status  #using generics
from django.contrib.auth import authenticate,login,logout #built in log in log-out
from django.contrib import messages

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .forms import SignUpForm

from django.http import JsonResponse
from huggingface_hub import InferenceClient
from django.conf import settings

def text_generation_view(request):
    if request.method == "POST":
        prompt = request.POST.get("prompt")

        if prompt:
            # Initialize the InferenceClient with your API token
            client = InferenceClient(token=settings.HUGGINGFACE_API_TOKEN)
            
            # Specify the model you want to use
            model_id = "gpt2"
            
            try:
                # Make the API call to generate text
                generated_text = client.text_generation(prompt, model=model_id, max_new_tokens=50)
                return JsonResponse({"status": "success", "response": generated_text})
            except Exception as e:
                return JsonResponse({"status": "error", "message": str(e)})

    return render(request, "text_generation.html")


class Product_list(generics.ListCreateAPIView):
    queryset=Products.objects.all() #viewset ->api,database data
    serializer_class=ProductSerializer
     
    # Delete all in models
    def delete(self,request,*args,**kwargs):
        Products.object.all.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Update(put,patch), delete 
class ProductUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset=Products.objects.all()
    serializer_class=ProductSerializer
    lookup_field='pk'




# views request (logic)
def home(request):
    products=Products.objects.all()
    return render(request,'home.html',{'products':products})


def webpage(request):
    products=Products.objects.all()
    return render(request,'demo.html',{'products':products})

def product(request,pk):
    product=Products.objects.get(id=pk)
    return render(request,'product.html',{'product':product})


#Athentication
def login_user(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,(" successfull.. login"))
            return redirect('home')
        else:
            messages.success(request,("details Not matches"))
            return redirect('login')
    else:
        return render(request,'login.html',{})


def logout_user(request):
    logout(request)
    messages.success(request,("logout is successfull.."))
    return redirect('login_user')



def register_user(request):
    form=SignUpForm()
    if request.method =="POST":
        form =SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            user_name=form.cleaned_data['username']
            password1=form.cleaned_data['password1']

            user=authenticate(username=user_name,password=password1)
            login(request,user)
            messages.success(request,("you have registered"))
            return redirect('login_user')
        else:
             messages.error(request, "Error in registration. Please check the form for errors.")
             return render(request, 'register.html', {'form': form})


    return render(request,'register.html',{'form':form})
