from paypalrestsdk import Payment
import logging
import paypalrestsdk

paypalrestsdk.configure({
  "mode": "sandbox", # sandbox or live
  "client_id": "ASGlW9mUxIfeCfJT3vh7QOyXD911zbx7zO1WORPNKnQijKv4AbhlLAMQMM6WKX38LWTrbhpQmV8NJ8zz",
  "client_secret": "EC-3IsnJLsmrb8OHf1M6JXR30GqJ5fc5E3uz8W846x9jXjdx80GEBBCU7XH8KyYT_ZMGBAWMT4i__jUC" })


logging.basicConfig(level=logging.INFO)
"""
payment = Payment({
    "intent": "sale",

    # Payer
    # A resource representing a Payer that funds a payment
    # Payment Method as 'paypal'
    "payer": {
        "payment_method": "paypal"},

    # Redirect URLs
    "redirect_urls": {
        "return_url": "http://localhost:3000/payment/execute",
        "cancel_url": "http://localhost:3000/"},

    # Transaction
    # A transaction defines the contract of a
    # payment - what is the payment for and who
    # is fulfilling it.
    "transactions": [{

        # ItemList
        "item_list": {
            "items": [{
                "name": "item",
                "sku": "item",
                "price": "5.00",
                "currency": "USD",
                "quantity": 1}]},

        # Amount
        # Let's you specify a payment amount.
        "amount": {
            "total": "5.00",
            "currency": "USD"},
        "description": "This is the payment transaction description."}]})

# Create Payment and return status
if payment.create():
    print("Payment[%s] created successfully" % (payment.id))
    # Redirect the user to given approval url
    for link in payment.links:
        if link.rel == "approval_url":
            # Convert to str to avoid google appengine unicode issue
            # https://github.com/paypal/rest-api-sdk-python/pull/58
            approval_url = str(link.href)
            print("Redirect for approval: %s" % (approval_url))
else:
    print("Error while creating payment:")
    print(payment.error)
    """
from paypalrestsdk import Payment
import logging
logging.basicConfig(level=logging.INFO)

payment_history = Payment.all({"count": 1})

# List Payments
print("List Payment:")
for payment in payment_history.payments:
    print("  -> Payment[%s]" % (payment.id))