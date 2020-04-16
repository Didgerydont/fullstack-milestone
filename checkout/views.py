from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages, auth
from django.db.models import Q
from .forms import MakePaymentForm, OrderForm
from .models import OrderLineItem
from django.conf import settings
from django.utils import timezone
from auction.models import Auction
from antiques.models import Antiques
import stripe


# Create your views here.

stripe.api_key = settings.STRIPE_SECRET_KEY


@login_required()
def checkout_auction(request, pk):
    auction = get_object_or_404(Auction, pk=pk)
    total = auction.winning_bid
    if request.method == "POST":
        order_form = OrderForm(request.POST)
        payment_form = MakePaymentForm(request.POST)
        
        if order_form.is_valid() and payment_form.is_valid():
            order = order_form.save(commit=False)
            order.date = timezone.now()
            order.save()

            total = auction.winning_bid
            order_line_item = OrderLineItem(
                order=order,
                auction=auction,
            )
            order_line_item.save()

            try:
                customer = stripe.Charge.create(
                    amount=int(total * 100),
                    currency="EUR",
                    description=request.user.email,
                    card=payment_form.cleaned_data['stripe_id'],
                )
            except stripe.error.CardError:
                messages.error(request, "Your card was declined!")

            if customer.paid:
                messages.error(request, "You have successfully paid")
                auction.money_collected = True
                auction.antiques.bought = True
                auction.auction_expired = True
                auction.save()
                return redirect(reverse('auction:auction'))
            else:
                messages.success(request, "Unable to take payment")
        else:
            print(payment_form.errors)
            messages.error(request, "We were unable to take a payment with that card!")
    else:
        payment_form = MakePaymentForm()
        order_form = OrderForm()

    context = {
        'auction': auction,
        'total': total,
        'order_form': order_form,
        'payment_form': payment_form,
        'publishable': settings.STRIPE_PUBLISHABLE_KEY,
    }
    return render(request, "auction-checkout.html", context)


@login_required()
def buy_now_checkout(request, pk):
    auction = get_object_or_404(Auction, pk=pk)
    total = auction.antiques.buy_now_price
    if request.method == "POST":
        order_form = OrderForm(request.POST)
        payment_form = MakePaymentForm(request.POST)
        print('why arent you working')
        
        if order_form.is_valid() and payment_form.is_valid():
            order = order_form.save(commit=False)
            order.date = timezone.now()
            order.save()
            order_line_item = OrderLineItem(
                order=order,
                auction=auction,
            )
            order_line_item.save()
            order_line_item.save()

            try:
                customer = stripe.Charge.create(
                    amount=int(total * 100),
                    currency="EUR",
                    description=request.user.email,
                    card=payment_form.cleaned_data['stripe_id'],
                )
            except stripe.error.CardError:
                messages.error(request, "Your card was declined!")

            if customer.paid:
                messages.success(request, "You have successfully paid")
                auction.money_collected = True
                auction.antiques.bought = True
                auction.auction_expired = True
                auction.save()
                return redirect(reverse('products:antiques'))
            else:
                messages.error(request, "Unable to take payment")
        else:
            print(payment_form.errors)
            messages.error(request, "We were unable to take a payment with that card!")
    else:
        payment_form = MakePaymentForm()
        order_form = OrderForm()

    context = {
        'auction': auction,
        'total': total,
        'order_form': order_form,
        'payment_form': payment_form,
        'publishable': settings.STRIPE_PUBLISHABLE_KEY,
    }
    return render(request, "buy-now.html", context)
