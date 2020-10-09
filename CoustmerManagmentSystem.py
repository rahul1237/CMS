# this is the coustmer managment system
# this is the basic version of dbms
# here we store all the data of the user! withour using any database!


idlist=[]
namelist=[]
contactlist=[]
emaillist=[]
genderlist=[]
statelist=[]
pincodelist=[]
productlist=[]
advancelist=[]

def addcoustmer(id,name,contact,email,gender,state,pincode,product,advance):
    idlist.append(id)
    namelist.append(name)
    contactlist.append(contact)
    emaillist.append(email)
    genderlist.append(gender)
    statelist.append(state)
    pincodelist.append(pincode)
    productlist.append(product)
    advancelist.append(advance)

def searchcoustmer(id):
    for e in range(len(idlist)):
        if(id==idlist[e]):
            print('ID=' ,idlist[e])
            print('NAME=', namelist[e])
            print('CONTACT=', contactlist[e])
            print('EMAIL=', emaillist[e])
            print('GENDER=', genderlist[e])
            print('STATE=', statelist[e])
            print('PINCODE=', pincodelist[e])
            print('PRODUCT=', productlist[e])
            print('ADVANCE=', advancelist[e])
        # else:
        #     print('INVALID ID \n   PLEASE TRY AGAIN')
        pass

def deletecoutmer(id):
    for i in range(len(idlist)):
        if(id==idlist[i]):
            idlist.pop(i)
            namelist.pop(i)
            contactlist.pop(i)
            emaillist.pop(i)
            genderlist.pop(i)
            statelist.pop(i)
            pincodelist.pop(i)
            productlist.pop(i)
            advancelist.pop(i)

        # else:
        #     print('INVALID ID \n   PLEASE TRY AGAIN')
        pass

def showall():
    for f in range(len(idlist)):
        print("ID=",idlist[f],"Name=",namelist[f],"Contact=",contactlist[f],"Email=",emaillist[f],"Gender=",genderlist[f],"State=",statelist[f],"Pincode=",pincodelist[f],"Product=",productlist[f],"Advance=",advancelist[f])



while(True):
    print("COUSTMER MANAGMENT SYSTEM")
    print()
    print()
    print("\tChoices we have:")
    #print()
    print("\t\t1. DATA ADDITION \n\t\t2. DATA SEARCHING \n\t\t3. DATA DELETION \n\t\t4.VIEW ALL DATA")
    print("\n\nEnter your choice:")
    a=int(input())
    if(a==1):
        id=int(input("Enter the id in the integer:"))
        name=input("Enter the name:")
        contact=int(input("Enter the contact number:"))
        email=input("Enter the email(Using @):")
        gender=input("M/F:")
        state=input("Enter your state:")
        pincode=int(input("Enter the pincode:"))
        product=input("Enter the product you want!:")
        advance=int(input("Enter the amount that you are paying as the advance payment!:"))
        addcoustmer(id,name,contact,email,gender,state,pincode,product,advance)
    elif(a==2):
        id=int(input("Enter the coustmers ID"))
        searchcoustmer(id)
    elif(a==3):
        id=int(input("Enter coustmers ID"))
        deletecoutmer(id)
    elif(a==4):
        showall()

    else:
        print("No other choice")


# CodeBy:Rahul Mahajan
# CC:anonymous0201
# CF:anonymous3107