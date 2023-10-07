import phonenumbers
from phonenumbers import geocoder

phone_number1 = phonenumbers.parse("+33797845980")
phone_number2 = phonenumbers.parse("+256718747189")

print("\nPhone Number Location")

print(geocoder.description_for_number(phone_number1,"en"))
print(geocoder.description_for_number(phone_number2,"en"))
