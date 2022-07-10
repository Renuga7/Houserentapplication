class houserent:
    def houses():
        area=input("which area you want: \n1:anna nagar \n2:kodambakkam \n3.goripalayam \n")
        if area=="1":
            userdata=["locality:anna nagar","area:chennai","square_feet:1200","type:3BHK","rent:rs.15000/month","owner_id=2"]
            for i in userdata:
                print(i)
        elif area=="2":
            userdata=["locality:kodambakkam","area:chennai","square_feet:798","type:2BHK","rent:rs.6000/month","owner_id=1"]
            for i in userdata:
                print(i)
        elif area=="3":
            userdata=["locality:goripalayam","area:madurai","square_feet:560","type:1BHK","rent:rs.5500/month","owner_id=2"]
            for i in userdata:
              print(i)
class tenant:
    def userreq():
        options = input("1:view houses  \n2:request  \n3:log out \n")
        if options == "1":
            userdata = houserent
            content = userdata.houses()
        elif options == "2":
            print("which area do you want: ")
            userdata = houserent
            content = userdata.houses()
            print("Request has sent successfully....")
        elif options == "3":
            print("THANK YOU! for choosing xyz, you are logged out successfully")

class owner:
    def ownerreq():
        options=input("1:To create a request to post  \n2:Remove their house for rental \n")
        if options == "1":
            userdata = houserent
            content = userdata.houses()
        elif options == "2":
            print("Request has been removed.....")

class user_details:
    def details():
        userdata = input("chose users details: \n1:1st user \n2:2nd user \n3:3rd user  \n")
        if userdata == "1":
            datas = ["User Id:1", "Name:Lucifer", "Email:lucifer@gmail.com", "Mobile:9876543210", "Aadhaar:123412341234"]
            for i in datas:
                print(i)
        elif userdata == "2":
            datas = ["User Id:2", "Name:Peter Parker", "Email:perterparker@gmail.com", "Mobile:1234567890", "Aadhaar:567856785678"]
            for i in datas:
                print(i)
        elif userdata == "3":
            datas = ["User Id:3", "Name:Tony Stark", "Email:tonystark@gmail.com", "Mobile:1234509876", "Aadhaar:345634563456"]
            for i in datas:
                print(i)

class approver:
    def approver_req():
        options=input("Enter your options: \n1:To view all the User details \n2:Decline the request \n")
        if options =="1":
            data = user_details
            content = data.details()
        elif options == "2":
            print("your request has declined")
print("-------------------------------------WELCOME TO HOUSE RENTAL PORTAL OF XYZ--------------------------------------------------")
user = input("1:Tenant \n2:Owner \n3:Approver \n")
if user == "1":
    opt = tenant
    obj = opt.userreq()
elif user == "2":
    opt = owner
    obj = opt.ownerreq()
elif user == "3":
    opt = approver
    obj = opt.approver_req()
