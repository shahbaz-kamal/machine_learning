data={
    "user":{
        "name":"Alice",
        id:123 ,
           "contact":{
               "email":"alice@example.com",
               "phone":"555-12345"
           }   }
,
"items":[
    {"name":"Laptop","price":1200},
    {"name":"Mouse","price":25}
    ]        
}

print("User Name",data["user"]["name"])
print("First Item Price: ",data["items"][0]["price"])
print("User Email: ",data["user"]["contact"]["email"])