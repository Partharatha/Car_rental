from django.shortcuts import render,redirect
from carsapp.models import Company,Products,Bookdrive
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from carsapp.forms import ProductEmiForm,BookDriveForm,EnquiryForm
import math
# Create your views here.
@login_required(login_url='login')
def Companylist(request):
    companies= Company.objects.all()
    return render(request,'cars/companylist.html',{'companies':companies})

@login_required(login_url='login')
def Company_details(request,id=0):
    companies= Company.objects.get(id=id)
    print(Company)
    return render(request,'cars/companydetails.html',{'companies':companies})

@login_required(login_url='login')
def calcemi(request, id=0):
    product = Products.objects.get(id=id)
    emi = None

    if request.method == 'POST':
        form = ProductEmiForm(request.POST, instance=product)
        if form.is_valid():
            price = form.cleaned_data.get('price') or 0
            print(price)
            loan_amount = form.cleaned_data.get('loan_amount') or 0
            print(loan_amount)
            tenure = form.cleaned_data.get('tensure') or 0  # in years
            print(tenure)

            # Auto-set interest rates based on tenure
            if 1 <= tenure <= 2:
                interest_rate = 8.5
            elif 3 <= tenure <= 4:
                interest_rate = 9.5
            elif 5 <= tenure <= 6:
                interest_rate = 10.5
            elif 7 <= tenure <= 8:
                interest_rate = 12
            elif tenure >= 9:
                interest_rate = 13.5
            else:
                interest_rate = 10.0

            try:
                loan_amount = float(loan_amount)
                tenure = int(tenure)
                interest_rate = float(interest_rate)

                monthly_rate = interest_rate / 12 / 100
                total_months = tenure * 12

                if loan_amount > 0 and monthly_rate > 0:
                    emi = (loan_amount * monthly_rate * math.pow(1 + monthly_rate, total_months)) / \
                          (math.pow(1 + monthly_rate, total_months) - 1)
                    emi = round(emi, 2)
            except (TypeError, ValueError, ZeroDivisionError):
                emi = None
    else:
        form = ProductEmiForm(instance=product)

    return render(request, 'cars/calemi.html', {'form': form, 'emi': emi})

@login_required(login_url='login')
def product(request,id=0):
    prod=Products.objects.get(id=id)
    print(prod)
    prod1=Products.objects.get(id=id+1)
    print(prod1)
    return render(request,'cars/product.html',{'prod':prod,'prod1':prod1})


@login_required(login_url='login')
def finalprice(request,id=0):
    prod=Products.objects.get(id=id)
    print(prod)
    prod1=Products.objects.get(id=id)
    print(prod1)

    price = float(prod.price)
    road_tax = price * 0.08
    rto_charges = price * 0.05
    gst = price * 0.18
    insurance = price * 0.035
    miscellaneous = price * 0.25


    final_price = price + road_tax + rto_charges + gst + insurance + miscellaneous

    context = {
        'prod': prod,
        'ex_showroom': price,
        'road_tax': road_tax,
        'rto_charges': rto_charges,
        'gst': gst,
        'insurance': insurance,
        'miscellaneous': miscellaneous,
        'final_price': round(final_price, 2),
        'prod1':prod1
    }
    return render(request,'cars/finalprice.html',context)

@login_required(login_url='login')
def Bookdrive(request, id=0):
    prod = Products.objects.get(id=id)

    if request.method == "POST":
        form = BookDriveForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)

            # Auto-fill fields
            booking.product_name = prod.product_name
            booking.user_name = request.user.username
            # booking.phone = request.user.profile.Phone 
            booking.email = request.user.email

            # booking.save()
            messages.success(
                request,
                f"✅ Thank you {request.user.username}! Your booking for {prod.product_name} "
                f"on {booking.date} at {booking.timings} is successful, you need to availble on that time of when ever u have bokked for the testdrive  ."
            )

            # return redirect("book_drive", id=prod.id)  
            # return redirect("bookings_list")
    else:
        form = BookDriveForm()

    return render(request, "cars/Bookdrive.html", {'prod': prod,'form': form})

@login_required(login_url='login')
def enquiry_view(request, id):
    prod = Products.objects.get(id=id)

    if request.method == "POST":
        form = EnquiryForm(request.POST)
        if form.is_valid():
            enquiry = form.save(commit=False)
            enquiry.user = request.user
            # enquiry.save()

            
            messages.success(
                request,
                "👍 \n Your request is received! Please wait for a callback."
            )

            return redirect("enquiry", id=prod.id) 

    else:
        form = EnquiryForm()

    return render(request, "cars/enquiry.html", {"prod": prod, "form": form})
# @login_required(login_url='login')
# def calcemi(request,id=0):
#     Product=Products.objects.get(id=id)
#     emi=None
#     if request.method == 'POST':
#         form = ProductEmiForm(request.POST,instance=Product)
#         if form.is_valid():
#             price=int(form.cleaned_data.get('price'))
#             print(price)
#             loan_amount=form.cleaned_data.get('loan_amount')
#             print(loan_amount)
#             tensure=form.cleaned_data.get('tensure')
#             print(tensure)
#     else:
#         form = ProductEmiForm(instance=Product)
#     return render(request,'cars/calcemi.html',{'form':form})