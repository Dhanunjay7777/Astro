from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import registerForm, FeedbackForm, ContactForm
from .models import register
from django.db.models import Q


def home(request):
    return render(request, "base.html")


def feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('feedback')
    else:
        form = FeedbackForm()
    response = render(request, 'feedback.html', {'form': form})
    return HttpResponse(response)


def zodiacsign(request):
    return render(request, "zodiacsign.html")


def horoscope(request):
    return render(request, "horoscope.html")


# def contact(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             form.save()
#     form = ContactForm()
#     return render(request, 'contact.html', {'form': form})


def home(request):
    return render(request, "home.html")


def registration(request):
    form1 = registerForm()
    msg = ""
    if request.method == "POST":
        form = registerForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            if register.objects.filter(email=email).exists():
                msg = "Email already registered!"
            else:
                form.save()
                msg = "Successfully registered!"
        else:
            msg = "Failed Registration"
    return render(request, "register.html", {"msg": msg, "form": form1})


def checklogin(request):
    uname = request.POST["uname"]
    pwd = request.POST["pwd"]

    flag = register.objects.filter(Q(username=uname) & Q(password=pwd))
    print(flag)

    if flag:
        print("Login Successs")
        return render(request, "userhome.html", {"uname": uname})
    else:
        msg = "Incorrect username or Password"
        return render(request, "userlogin.html", {"message": msg})
        return HttpResponse("Login Failed")


def login(request):
    return render(request, "userlogin.html")

from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import Contact

def contact_view(request):
    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            # Handle form submission and database insertion here
            contact = Contact(
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                email=form.cleaned_data['email'],
                need=form.cleaned_data['need'],
                message=form.cleaned_data['message']
            )
            contact.save()  # Save the contact submission to the database

            return redirect('contact')  # Redirect to a success page

    return render(request, 'contact.html', {'form': form})
