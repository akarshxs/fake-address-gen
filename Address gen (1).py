from faker import Faker

fake = Faker()

first_name = fake.first_name()
last_name = fake.last_name()
email = fake.email()
birth_date = fake.date_of_birth(minimum_age=19, maximum_age=21)
address1 = fake.address().split('\n')[0]
address2 = fake.address().split('\n')[0]
address3 = fake.address().split('\n')[0]
region = fake.city()
city = fake.city()
country = fake.country()
state = fake.state()
zipcode = fake.zipcode()
phone_number = fake.phone_number()
fax_number = fake.phone_number()
alternate_phone_number = fake.phone_number()
credit_card_number = fake.credit_card_number(card_type=None)
credit_card_expiry_month = fake.credit_card_expire(start="now", end="+10y", date_format="%m")
credit_card_expiry_year = fake.credit_card_expire(start="now", end="+10y", date_format="%Y")
credit_card_security_code = fake.credit_card_security_code(card_type=None)
ip_address = fake.ipv4()
latitude = fake.latitude()
longitude = fake.longitude()
bank_account_number = fake.iban()
company = fake.company()

message = f"""\
First Name: {first_name}
Last Name: {last_name}
Email: {email}
Birth Date: {birth_date}
Address 1: {address1}
Address 2: {address2}
Address 3: {address3}
Region: {region}
City: {city}
Country: {country}
State: {state}
Zipcode: {zipcode}
Phone Number: {phone_number}
Fax Number: {fax_number}
Alternate Phone Number: {alternate_phone_number}
Credit Card Number: {credit_card_number}
Credit Card Expiry Month: {credit_card_expiry_month}
Credit Card Expiry Year: {credit_card_expiry_year}
Credit Card Security Code: {credit_card_security_code}
IP Address: {ip_address}
Latitude: {latitude}
Longitude: {longitude}
Bank Account Number: {bank_account_number}
Company: {company}
"""
print(message)