import qrcode

# taking the UPI ID as an input
upi_id=input("Enter your UPI_ID")

#upi://pay?pa=UPI_ID&apn=NAME&am=Amount&cu=Currency&tn=message

# pa -->upi_id
# pn --> recipient_name
# am --> amount
# cu --> currency
# tn --> transaction message after payment

# Defining the payment URL based on the UPI ID and the payment
# you can modify these URLs based on the payment apps you want to support

Paytm_url=f'upi://pay?pa={upi_id}&pn=Recipient%20name&mc=1234'
PhonePe_url=f'upi://pay?pa={upi_id}&pn=Recipient%20name&mc=1234'
GooglePay_url=f'upi://pay?pa={upi_id}&pn=Recipient%20name&mc=1234'

# Create QRcode  for each payment app
Paytm_qr=qrcode.make(Paytm_url)
PhonePe_qr=qrcode.make(PhonePe_url)
GooglePay_qr=qrcode.make(GooglePay_url)

# Save the QR Code to image file
Paytm_qr.save("Paytm_qr.png")
PhonePe_qr.save("PhonePe_qr.png")
GooglePay_qr.save("GooglePay_qr.png")

# Display the QrCode
Paytm_qr.show()
# PhonePe_qr.show()
# GooglePay_qr.show()