from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"index.html")

def sum_page(request):
    return render(request,"sum.html")

def sum_logic(request):
    x=request.POST.get('a')
    y=request.POST.get('b')
    z=int(x)+int(y)
    return render(request,"sum.html",{"result":"Sum of two number is "+str(z)})

def multiplication(request):
    if request.method=='GET':
        return render(request,"multiply.html")
    else:
        x=request.POST.get('a')
        y=request.POST.get('b')
        z=int(x)*int(y)
        return render(request,"multiply.html",{"ans":"multiplication is"+str(z)})
