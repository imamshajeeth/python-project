
class cash:
    l=[[100,"KINGERFISHER",1500,"Bangalore","Chennai"],[101,"INDIGO",2000,"Trichy","kerala"],[102,"VISTARA",2500,"Pondicherry","Goa"],
       [103,"AIR INDIA",3000,"Hyderabad","Madurai"],[104,"SPICEJET",4500,"Trichy","Hyderabad"],[105,"AIR ASIA",5000,"Chennai","Kerala"]]
    
    dis={}
    iid=1000
    
    
def passenger():
    while True:
        b=int(input("\t1.Signup:\n\t2.Login:\n\t3.Exit:\n\nPress The Number:"))
        if b==1:
            passname=input("\tEnter Your Name : ")
            Gender=input("\tEnter your Gender : ")
            Email=input("\tEnter your Mail : ")
            verif=input("\tGive any ID proof : ")
            passwd=int(input("\tEnter Your Password : "))
            cash.dis[cash.iid]=[cash.iid,passname,passwd,0,"nil",0,0,"nil","nil","yet to book"]
            print("\tYour Id is : ",cash.iid)
            print("\n")
            print("\t\t\t\t\t***************************************************\n")
            
            print("\t\t\t*****check your details*****")
            print("\n")
            print("\tyour Name : ",passname)
            print("\tyour Gender : ",Gender)
            print("\tyour Mail : ",Email)
            print("\tyour ID proof is : ",verif)
            print("\tyour passwd : ",passwd)
            print("\n\t\t\t\tIF ANY DETAILS ARE WRONG GO CORRECT THEM")
            print("\n")
            print("\t\t\t*****Your Id is created successfully*****")
            print("\n")
            print("\t\t\t\t\t***************************************************\n")
            cash.iid+=1
        elif b==2:
            print("\n\t\t Your Id is created in Signup section please cheak it up......")
            try:
                entpsid=int(input("\n\tEnter Your Id : "))
            except:
                print("\tYour Passenger Id Incorrect,please try again")
                try:
                    entpsid=int(input("\tEnter Your Id : "))
                except:
                    print("\ttwo many attems try again later!!!...")
                    break
            if entpsid<1000 or entpsid>=cash.iid:
                print("\tInvalid ID!!...")
                break
            else:
                entpswd=int(input("\tEnter your password : "))
                if entpswd==cash.dis[entpsid][2]:
                    while True:
                        c=int(input("1.Check Avability and Far:\n2.Book Tricket:\n3.View:\n4.Exit\n\nPress the number:"))
                        print("\t\t\t\t\t***************************************************\n")
                        print("\n")
                        if c==1:
                            for i in cash.l:
                                print(i)
                                print("\n\t")
                            try:
                                frm=input("\n\tEnter the From Location : ")
                                to=input("\tEnter the To Location : ")
                                print("\n")
                            except:
                                print("\tInvaild Location")
                                try:
                                    frm=input("\n\tEnter the From Location : ")
                                    to=input("\tEnter the To Location : ")
                                    print("\n")
                                except:
                                    print("\tTO MANY ATTEMS!!.....PLEASE TRY AGAIN---")
                                    break
                            for i in range(len(cash.l)):
                                if frm==cash.l[i][3] and to==cash.l[i][4]:
                                    print(*cash.l[i],sep='\t')
                                    break
                            else:
                                    print("Not Avaible")
                        elif c==2:
                            try:
                                flid=int(input("\tEnter the flight Id : "))
                            except:
                                print("\tFlight Id is Missing\n")
                                break
                            for i in range(len(cash.l)):
                                if flid==cash.l[i][0]:
                                    tric=int(input("\tEnter the number of Tickets : "))
                                    cash.dis[entpsid][3]=flid
                                    cash.dis[entpsid][4]=cash.l[i][1]
                                    cash.dis[entpsid][5]=tric
                                    cash.dis[entpsid][6]=tric*int(cash.l[i][2])
                                    cash.dis[entpsid][7]=frm
                                    cash.dis[entpsid][8]=to
                                    cash.dis[entpsid][9]="Pending"
                                    print("\tyour flight fare is : Rs.",cash.dis[entpsid][6])
                                    Payment=input("\tkindly mention your Payment mode example online or offline : ")
                                    print(f"\n\tyou have selected mode as {Payment}\n")
                                    print(f"\tThe online payement mode is successfully submitted Rs.{cash.dis[entpsid][6]}\n")
                                    print("\tyour Request are summitted Successfully\n")
                                    print(f"\tyour Tickets has been send to your register Mail : {Email}")
                                    print("\n\n\t\t\t\t\t\tAny Further Details please........Contact Through our Mail")
                                    print("\n\n\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tOur Email Id is : airworld@gmail.com")
                                    break
                            else:
                                print("\tInvalid flight Id")
                        elif c==3:
                            print("Passenger id\tpassenger name\tpassenger pass\tflight id\tflight name\tno.of tickets\ttotal fare\t takeoff\tlanding\tstatus\n")
                            for i in cash.dis:
                                print(*cash.dis[i],sep="\t")
                        else:
                            break
        else:
            break
            
print("\t\t\t\t*********Welcome To AIRWORLD**********")
while True:
    a=int(input('1.passenger:\n2.Cashier:\n3.Exit:\n\nPress The Number:'))
    if a==1:
       passenger()
    elif a==2:
        while True:
            acceid=4343
            acceid2=6363
            acceid3=8767
            eacceid=int(input("Enter your Access Id : "))
            if eacceid==acceid:
                print("\t\t\t\t Welcome IMAM")                
            elif eacceid==acceid2:
                print("\t\t\t\t Welcome GOPI")
            elif eacceid==acceid3:
                print("\t\t\t\t Welcome CATHRIN")    
            else:
                print("\t\t\tInvaild Access ID!!.......")
                break
            print("\t")
            print("\t\t\t\t\t***************************************************\n")
            chs=int(input("1.view:\n2.Approve:\n3.cancel:\n4.report:\n5.Exit:\n\npress the Key:"))
            if chs==1:
                print("Passenger id\tpassenger name\tpassenger pass\tflight id\tflight name\tno.of tickets\ttotal fare\t takeoff\tlanding\tstatus\n")
                for i in cash.dis:
                    print(*cash.dis[i],sep="\t")
            elif chs==2:
                apr=int(input("1.approve using id\n2.approve all\n3.exit\nenter the key:"))
                if apr==1:
                    try:
                       chsid=int(input("Enter passenger Id : "))
                    except:
                        print("\tPassenger Id is Missing")
                        break
                    if chsid<1000 or chsid>=cash.iid:
                        print("\tInvalid ID!!...")
                        break
                    else:
                        for i in cash.dis:
                            if chsid==i and cash.dis[i][9]=="Pending":
                                cash.dis[i][9]="approved"
                                print("ticket approve for :",chsid)
                                break
                        else:
                            print("No pending ticket are avaible Against :",chsid,"\n")
                            break
                elif apr==2:
                    for i in cash.dis:
                        if cash.dis[i][9]=="Pending":
                            cash.dis[i][9]="approved"
                            print("all the pending ticket are approved")
                        break
                    else:
                        print("No pending ticket are avaible ")
                        break
                else:
                    break
            elif chs==3:
                for i in cash.dis:
                    if cash.dis[i][9]=="Pending":
                        cash.dis[i][9]="cancel"
                        print("all the pending tickets are cancelled")
                        break
                else:
                    print("No pending ticket are avaible")
                    break
            elif chs==4:
                
                m=open("pass.txt","w")
                m.write(str(cash.dis))
                m.close()
                print("\n")
                print("\tReport Save Successfully")

           
            else:
                break
    else:
        print("\t\t\t\t*****Thanking for Visiting Our AIRWORLD*****")
        break

