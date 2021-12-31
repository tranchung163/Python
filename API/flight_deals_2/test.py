import requests

SHEETY_ENDPOINT = "https://api.sheety.co/a5ef226282cad66b0d530bc4bfd36779/copyOfFlightDeals/users"

wrong_email = True
while wrong_email:
    first_name = input("Enter your first name: ")
    last_name = input("\nEnter your last name: ")
    email1 = input("\nEnter your email: ")
    email2 = input("\nType your email again: ")
    if email1 == email2:
        wrong_email = False
    else: 
        print("\n your email did not match!!! type again\n")
    
body = {
    "user": {
        "firstName": first_name,
        "lastName": last_name,
        "email": email2,
    }
}

response = requests.post(url=SHEETY_ENDPOINT, json=body)
get_response = requests.get(url=SHEETY_ENDPOINT).json()
print(get_response)
