from paypalrestsdk import Payment
import logging
import paypalrestsdk

paypalrestsdk.configure({
  "mode": "sandbox", # sandbox or live
  "client_id": "ASGlW9mUxIfeCfJT3vh7QOyXD911zbx7zO1WORPNKnQijKv4AbhlLAMQMM6WKX38LWTrbhpQmV8NJ8zz",
  "client_secret": "EC-3IsnJLsmrb8OHf1M6JXR30GqJ5fc5E3uz8W846x9jXjdx80GEBBCU7XH8KyYT_ZMGBAWMT4i__jUC" })

logging.basicConfig(level=logging.INFO)

'''
P-26699382Y8449805UPV3AV3A
155b017f-4363-4a8b-a892-7f5b0839f81a
'''

def activate(plan_id):
    try:
        billing_plan = paypalrestsdk.BillingPlan.find(str(plan_id))
        print("Got Billing Plan Details for Billing Plan[%s]" % (billing_plan.id))

        if billing_plan.activate():
            billing_plan = paypalrestsdk.BillingPlan.find(str(plan_id))
            print("Billing Plan [%s] state changed to [%s]" %
                  (billing_plan.id, billing_plan.state))
        else:
            print(billing_plan.error)

    except paypalrestsdk.ResourceNotFound as error:
        print("Billing Plan Not Found")


def create():
    billing_plan = paypalrestsdk.BillingPlan({
        "description": "Create Plan for Regular",
        "merchant_preferences": {
            "auto_bill_amount": "yes",
            "cancel_url": "http://www.cancel.com",
            "initial_fail_amount_action": "continue",
            "max_fail_attempts": "1",
            "return_url": "http://www.success.com",
            "setup_fee": {
                "currency": "USD",
                "value": "25"
            }
        },
        "name": "Testing1-Regular1",
        "payment_definitions": [
            {
                "amount": {
                    "currency": "USD",
                    "value": "100"
                },
                "charge_models": [
                    {
                        "amount": {
                            "currency": "USD",
                            "value": "10.60"
                        },
                        "type": "SHIPPING"
                    },
                    {
                        "amount": {
                            "currency": "USD",
                            "value": "20"
                        },
                        "type": "TAX"
                    }
                ],
                "cycles": "0",
                "frequency": "MONTH",
                "frequency_interval": "1",
                "name": "Regular 1",
                "type": "REGULAR"
            },
            {
                "amount": {
                    "currency": "USD",
                    "value": "20"
                },
                "charge_models": [
                    {
                        "amount": {
                            "currency": "USD",
                            "value": "10.60"
                        },
                        "type": "SHIPPING"
                    },
                    {
                        "amount": {
                            "currency": "USD",
                            "value": "20"
                        },
                        "type": "TAX"
                    }
                ],
                "cycles": "4",
                "frequency": "MONTH",
                "frequency_interval": "1",
                "name": "Trial 1",
                "type": "TRIAL"
            }
        ],
        "type": "INFINITE"
    })

    if billing_plan.create():
        print("Billing Plan [%s] created successfully" % (billing_plan.id))
    else:
        print(billing_plan.error)


def get(plan_id):
    try:
        billing_plan = paypalrestsdk.BillingPlan.find(plan_id)
        print("Got Billing Plan Details for Billing Plan[%s]" % (billing_plan.id))

    except paypalrestsdk.ResourceNotFound as error:
        print("Billing Plan Not Found")


def get_link(plan_id):
    try:
        billing_plan = paypalrestsdk.BillingPlan.find(plan_id)
        print("Got Billing Plan Details for Billing Plan[%s]" % (billing_plan))

    except paypalrestsdk.ResourceNotFound as error:
        print("Billing Plan Not Found")


def get_all():
    history = paypalrestsdk.BillingPlan.all(
        {"status": "CREATED", "page_size": 5, "page": 1, "total_required": "yes"})
    print(history)

    print("List BillingPlan:")
    for plan in history.plans:
        print("  -> BillingPlan[%s]" % (plan.id))

