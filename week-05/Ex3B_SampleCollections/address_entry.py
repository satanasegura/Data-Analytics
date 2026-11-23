name = "Jalen Brunson"
address = "158 Rutherford Place"
city = "North Arlington"
state = "NJ"
zip = "07031"   

contact_info = {
    "name": name,
    "address": address,
    "city": city,
    "state": state,
    "zip": zip
}

mailing_address = (f"{contact_info['name']}\n"
                   f"{contact_info['address']}\n"
                   f"{contact_info['city']}, {contact_info['state']} {contact_info['zip']}")

print(mailing_address)

del contact_info["name"]

first_name = "Jalen"
last_name = "Brunson"
full_name = {"first name": first_name, "last name": last_name,}

honorific = "Mr."
full_name.update({"honorific": honorific})

contact_info.update({"full_name": full_name})

name_line = (
    f"{contact_info['full_name']['honorific']} {contact_info['full_name']['first name']} {contact_info['full_name']['last name']}"
)
street_line = contact_info["address"]  
city_state_zip_line = f"{contact_info['city']}, {contact_info['state']} {contact_info['zip']}"  

mailing_address = f"{name_line}\n{street_line}\n{city_state_zip_line}"

print(mailing_address)