
def func(message_json):
    for items in message_json:
        print(f"{items} -> {message_json[items]}")



message = {
  "property_id": "PROP-101",
  "monthly_rent": 15000,
  "security_deposit": 30000,
  "bedrooms": 2
}

func(message)




