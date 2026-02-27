import phonenumbers
from phonenumbers import geocoder, carrier, timezone

number = input("Enter phone number: ")

# Parse for India if no country code
if not number.startswith("+"):
    phoneNumber = phonenumbers.parse(number, "IN")
else:
    phoneNumber = phonenumbers.parse(number)

# Location (state / telecom circle)
location = geocoder.description_for_number(phoneNumber, "en")

# Carrier
sim = carrier.name_for_number(phoneNumber, "en")

# Timezone
time = timezone.time_zones_for_number(phoneNumber)

print("Location:", location)
print("Carrier:", sim)
print("Timezone:", time)