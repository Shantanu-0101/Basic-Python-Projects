import qrcode 

upi_id = input("enter your upi id: ")

phone_pay_url = f"upi://pay?pa={upi_id}&pn=Recipient%20Name&Mc=1234"

phonepay_qr = qrcode.make(phone_pay_url)

phonepay_qr.show()