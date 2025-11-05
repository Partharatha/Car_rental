from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from rentalcars.models import cars
from rentalcars.forms import SeatFilterForm

# Create your views here.

def rental_cars_list(request):
    form = SeatFilterForm(request.GET)
    qs = cars.objects.all()

    # if form.is_valid():
    #     seat = form.cleaned_data.get('seat')
    #     company = form.cleaned_data.get('company')
    #     if seat:
    #         qs = qs.filter(seat_capacity=int(seat))
    #     if company:
    #         qs = qs.filter(company__icontains=company)

    context = {'cars': qs, 'form': form}
    return render(request, 'Rentalcar/rentalcars_list.html', context)

def car_detail(request,pk):
    car = get_object_or_404(cars, pk=pk)
    return render(request, 'Rentalcar/rentalcars_details.html', {'car': car})

# def details(request):
#     return render(request, "Rentalcar/details_rent.html")

# def car_detail(request,pk):
#     car = get_object_or_404(cars, pk=pk)
#     return render(request, 'Rentalcar/rentalcars_detail.html', {'car': car})

# def details(request, pk):    
#     car = get_object_or_404(cars, pk=pk) 
#     print(car)
#     if car.seat_capacity=='5':
#         k=15
#     elif car.seat_capacity=='7':
#         k=25
        
#     if request.method=='POST':
#         print("1")
#         expected_km = int(request.POST['expected_km'])
#         Days=int(request.POST.get('Expected_Km',0))
#         print("2")
#         if expected_km==0:
#             print("3")
#             total_rent=Days*300*k
#             print(total_rent)
#             cal=True
#             return render(request, "Rentalcar/details_rent.html",{"car": car,'k':k,'days':Days,'total_rent':total_rent,'cal':cal})
#         else:
#             print("4")
#             print(expected_km)
#             print(k)
#             total_rent=expected_km*k
#             print(total_rent)
#             cal=True
#             return render(request,"Rentalcar/details_rent.html",{"car": car,'k':k,'excepted_km':expected_km,'days':Days,'total_rent':total_rent,'cal':cal})
#     return render(request, "Rentalcar/details_rent.html", {"car": car,'k':k})




def details(request, pk):    
    car = get_object_or_404(cars, pk=pk) 
    
    # Set rate based on seat capacity
    if car.seat_capacity == '5':
        k = 15
    elif car.seat_capacity == '7':
        k = 25
    else:
        k = 20  # default rate if something else
    
    total_cost = None
    warning = None

    if request.method == 'POST':
        days = int(request.POST.get('days', 0))
        expected_km = int(request.POST.get('expected_km', 0))

        # Case 1: If expected_km == 0 → calculate based on days (300km/day)
        if expected_km == 0:
            total_cost = days * 300 * k
            warning = f"Assumed {days * 300} km (300 km/day)"
        else:
            total_cost = expected_km * k

    return render(request, "Rentalcar/details_rent.html", {
        "car": car,
        "rate": k,
        "days": request.POST.get('days', ''),
        "expected_km": request.POST.get('expected_km', ''),
        "total_cost": total_cost,
        "warning": warning
    })

def final(request, pk):    
    car = get_object_or_404(cars, pk=pk) 
    ca = False
    km = 0
    fp=0
    if car.seat_capacity == '5':
        k = 50
    elif car.seat_capacity == '7':
        k = 100

    if request.method == 'POST':
        days = int(request.POST.get('days', 1))
        excepted_km = int(request.POST.get('excepted_km', 0))
        tk=excepted_km-car.total_km_driven
        petrol=(tk/car.milage)*102
        if tk>days*300:
            tp=tk*km
            fp=(tp-petrol)+(tp*0.02)
            ca=True
            return render(request, 'Rentalcar/finalprice.html', {'ca': ca, 'km': km, 'car': car,'fp':fp})
        elif tk==days*300:
            tp=tk*km
            fp=(tp-petrol)
            ca=True
            return render(request, 'Rentalcar/finalprice.html', {'ca': ca, 'km': km, 'car': car,'fp':fp})
        else:
            tp=days*300*km
            fp=(tp-petrol)
            ca =True
            return render(request, 'Rentalcar/finalprice.html', {'ca': ca, 'km': km, 'car': car,'fp':fp})
            


      

    return render(request, "Rentalcar/finalprice.html", {"car": car})