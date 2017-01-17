import paypalrestsdk
import logging

#Sandbox account:
	#watcha.ac-facilitator@gmail.com
#Client ID:
	#AePJT8vNBcC1Z51Q8OBjclOUM4iyll6GXD77Zdx8eXhlYWu9fu86aCXMrxI_kI15U2-02-x4aq_nkTDB
#Secret:
	#EHP2TSxiGxcdqmLsjA05cR18zamGE0ZPt-7Q1bnae6fNoaePAAizXx28ehniN9M5izzu5tjTeDeZLxaj

paypalrestsdk.configure({
  "mode": "sandbox", # sandbox or live
  "client_id": "AePJT8vNBcC1Z51Q8OBjclOUM4iyll6GXD77Zdx8eXhlYWu9fu86aCXMrxI_kI15U2-02-x4aq_nkTDB",
  "client_secret": "EHP2TSxiGxcdqmLsjA05cR18zamGE0ZPt-7Q1bnae6fNoaePAAizXx28ehniN9M5izzu5tjTeDeZLxaj",
 }) 

payment = paypalrestsdk.Payment({
  "intent": "sale",
  "payer": {
    "payment_method": "credit_card",
    "funding_instruments": [{
      "credit_card": {
        "type": "visa",
        "number": "4096363440954484",
        "expire_month": "11",
        "expire_year": "2021",
        "cvv2": "874",
        "first_name": "Watcharapon",
        "last_name": "Hongthong" }}]},
  "transactions": [{
    "item_list": {
      "items": [{
        "name": "item",
        "sku": "item",
        "price": "1.00",
        "currency": "USD",
        "quantity": 1 }]},
    "amount": {
      "total": "1.00",
      "currency": "USD" },
    "description": "This is the payment transaction description." }]})

if payment.create():
  print("Payment created successfully")
else:
  print(payment.error)
