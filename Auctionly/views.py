from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
import uuid
from .models import *
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth import authenticate,  login 
from django.http import HttpResponse
from django.contrib.auth import logout 
from django.utils.timezone import now
from django.contrib.auth.decorators import login_required


# Create your views here.

def home(request):
    return render(request, 'Auctionly.html')

def sign_in(request):

    if request.method == 'POST':

        # retrives username and pass from the form submitted by user
        
        username = request.POST.get('username')
        password = request.POST.get('password')


        # check if the username exist in database or not
        user_obj = User.objects.filter(username = username).first()
        if user_obj is None:
            messages.success(request, 'User not found')
            return redirect('/sign_in')
        
        profile_obj = Profile.objects.filter(user = user_obj).first() 

        if not profile_obj.is_verified:
            messages.success(request, "Profile isn't verified check your mail")
            return redirect('/sign_in')
        
        user = authenticate(username = username, password = password)
        if user is None:
            messages.success(request, "Wrong Password")
            return redirect('/sign_in')
        
        login(request, user)
        return redirect('/')
    return render(request, 'signin.html')

def sign_up(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            if User.objects.filter(username=username).first():
                messages.success(request, 'Username is already taken.')
                return redirect('/sign_up')
            if User.objects.filter(email=email).first():
                messages.success(request, 'Email already in use.')
                return redirect('/sign_up')

            user_obj = User.objects.create(username=username, email=email)
            user_obj.set_password(password)
            user_obj.save()
            auth_token = str(uuid.uuid4())
            profile_obj = Profile.objects.create(user=user_obj, auth_token=auth_token)
            profile_obj.save()
            send_mail_after_registration(email, auth_token)
            return redirect('/emailsent')
        except Exception as e:
            print(e)
    return render(request, 'signup.html')


    return render(request, 'signup.html')

def success(request):
    return render(request, 'Auctionly.html')

def aboutAuctionly(request):
    return render(request, 'aboutAuctionly.html')


def contactUs(request):
    if request.method == "POST":
        contact = Contact()
        name = request.POST.get('name')
        mail = request.POST.get('mail')
        mobile = request.POST.get('mobile')
        text = request.POST.get('text')
        contact.name = name
        contact.mail = mail
        contact.mobile = mobile
        contact.text = text
        contact.save()
        return HttpResponse("<h1>THANKS FOR CONTACTING AUCTIONLY</h1>")
    return render(request, 'contactUs.html')

def departmentAuctionly(request):
    return render(request, 'departmentAuctionly.html')

def liveauction(request):
    return render(request, 'liveauction.html')

def pastauction(request):
    return render(request, 'pastauction.html')

def upcomingauction(request):
    return render(request, 'upcomingauction.html')

def emailsent(request):
    return render(request, 'emailsent.html')

def modernart(request):
    products = Product.objects.all()
    return render(request, 'modernart.html', {'products': products})

def timepieces(request):
    return render(request, 'timepieces.html')

def furniture(request):
    return render(request, 'furniture.html')

def jewellery(request):
    return render(request, 'jewellery.html')
    




def openpage(request, id):
    product = Product.objects.filter(id=id).first()
    bids = product.bids.all().order_by('-amount')
    remaining_time = max((product.end_auction - now()).total_seconds(), 0)
    error_message = None
    auction_active = remaining_time > 0
    winner = None

    if not auction_active and bids.exists():
        winner = bids.order_by('-amount').first().user
        product.winner = winner
        product.save()

    if request.method == 'POST':
        if not auction_active:
            error_message = "Auction has ended. You cannot place a bid."
        else:
            amount = request.POST.get('amount')
            Bid.objects.create(
                user=request.user,
                product=product,
                amount=amount
            )



    context = {
        'product': product,
        'bids': bids,
        'remaining_time': remaining_time,
        'error_message': error_message,
        'auction_active': auction_active,
        'winner': winner,
    }
    return render(request, 'openpage.html', context)



# veryfying the authetication link shared

def verify(request, auth_token):
    try:
        profile_obj = Profile.objects.filter(auth_token = auth_token).first()
        if profile_obj:
            if profile_obj.is_verified:
                messages.success(request, 'Your account has already been verified.')
                return redirect('/sign_in')
            profile_obj.is_verified = True
            profile_obj.save()
            messages.success(request, 'Congrats your account has been verified.')
            return redirect('/sign_in')
        else:
            return redirect('/error')
    except Exception as e:
        print(e)





# fxn for sending email for authetication


def send_mail_after_registration(email, token):
    domain = settings.SITE_DOMAIN  # Set this in settings.py or via environment variable
    verify_url = f'http://{domain}/verify/{token}'
    
    subject = 'Verify Your Account'
    message = f'Hi, please click the link below to verify your account:\n{verify_url}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]

    send_mail(subject, message, email_from, recipient_list)




# fxn for sending winner and owner emails

def handle_ended_auctions():
    ended_auctions = Product.objects.filter(end_auction__lt=now(), notified=False)

    for product in ended_auctions:
        bids = product.bids.all().order_by('-amount')
        owner_email = product.owner.email  # Make sure Product model has owner with email

        if bids.exists():
            winner = bids.first().user
            winner_email = winner.email

            # Save winner to the product
            product.winner = winner

            # Email to the winner
            send_mail(
                subject='🎉 You Won the Auction!',
                message=f'Congratulations {winner.username},\n\nYou won the auction for "{product.title}" with a bid of ${bids.first().amount:.2f}.\n\nPlease follow up for delivery or payment.',
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[winner_email],
                fail_silently=False,
            )

            # Email to the owner
            send_mail(
                subject='🏁 Your Auction Has Ended',
                message=f'Your auction for "{product.title}" has ended. The winner is {winner.username} with a bid of ${bids.first().amount:.2f}.',
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[owner_email],
                fail_silently=False,
            )
        else:
            # No bids placed
            send_mail(
                subject='🔔 No Bids on Your Auction',
                message=f'Your auction for "{product.title}" has ended, but no one placed a bid.',
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[owner_email],
                fail_silently=False,
            )

        # Mark auction as handled
        product.notified = True
        product.is_auction_active = False
        product.save()



from django.http import HttpResponse

def trigger_auction_check(request):
    handle_ended_auctions()
    return HttpResponse("Auction check triggered!")


def logout_view(request):
    logout(request)
    return redirect('home')




