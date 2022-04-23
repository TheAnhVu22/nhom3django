from cart.cart import Cart

from django.conf import settings
# for HTML Email
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from .models import Order, OrderItem

def checkout(request, first_name, last_name, email, phone, address, zipcode, place, amount, vendor):
    order = Order.objects.create(first_name=first_name, last_name=last_name, email=email, address=address, zipcode=zipcode, place=place, phone=phone, paid_amount=amount, vendors=vendor)
    for item in Cart(request):
        OrderItem.objects.create(order=order, product=item['product'], vendor=vendor, price=item['product'].price, quantity=item['quantity'])
        
    return order

def notify_vendor(order):
    from_email = settings.DEFAULT_EMAIL_FROM

    to_email = vendor.email
    subject = 'New order'
    text_content = 'You have a new order!'
    html_content = render_to_string('order/email_notify_vendor.html', {'order': order, 'vendor': vendor})

    msg = EmailMultiAlternatives(subject, text_content, from_email, [to_email])
    msg.attach_alternative(html_content, 'text/html')
    msg.send()

def notify_customer(order):
    from_email = settings.DEFAULT_EMAIL_FROM

    to_email = order.email
    subject = 'Order confirmation'
    text_content = 'Thank you for the order!'
    html_content = render_to_string('order/email_notify_customer.html', {'order': order})

    msg = EmailMultiAlternatives(subject, text_content, from_email, [to_email])
    msg.attach_alternative(html_content, 'text/html')
    msg.send()