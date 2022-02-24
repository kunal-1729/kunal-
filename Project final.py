print(".......WELCOME TO SCHOOL MANAGEMENT PORTAL.......")
print("Enter number for following operations:-")
a=int(input("1.For Teacher Portal\n2.For Student Portal\nEnter:"))
add={}
if a==1:
    while True:
        print("\nMenu for Teacher's Portal:-")
        print("1.For adding new Teacher\n2.For display Teacher's information\n3.For deleting a record")
        b=int(input("4.For updating Teacher's record\n5.For searching Teacher's data\n6.Quit\nEnter:"))
        if b==1:
            n=int(input("Enter number of Teacher you want add:"))
            for i in range(n):
                name=input("Enter Teacher's name:")
                i_d=int(input("Enter Teacher's id:"))
                sub=input("Enter Subject:")
                add[name]=[i_d,sub]
            print("Data added successfully!!")
        if b==2:
            if len(add)==0:
                print("No record found!!\n")
            else:
                print("------------------------------------------------\nName               ID              Subject\n")
                for j in add:
                    print(j,"            ",add[j][0],"           ",add[j][1])   
                print("\n------------------------------------------------\n")
        if b ==3:
            if len(add)==0:
                print("No record is there!!\n")
            else:
                Name=input("Enter name of the Teacher for whom you want to remove the data:")
                add.pop(Name)
                print(Name+"'s data is removed!!\n")
        if b==4:
            while True:
                if len(add)==0:
                    print("No record is there to update!!\n")
                    break
                print("\nMenu,what do you want to update:-")
                u=int(input("1.ID\n2.Subject\n3.Back\nEnter:"))
                if u==1:
                    NAME=input("Enter name of the Teacher who's name is to be updated:")
                    ID=int(input("Input new id:"))
                    s=add[NAME][1]
                    add[NAME]=[ID,s]
                    print("Record Updated!!")
                if u==2:
                    N=input("Enter name of the Teacher who's subject is to be updated:")
                    SUB=input("Enter new subject:")
                    PID=add[N][0]
                    add[N]=[PID,SUB]
                    print("Record Updated!!")
                if u==3:
                    break
        if b==5:
            temp=input("Enter name of the Teacher to find record:")
            if temp in add:
                print("Name:",temp)
                print("ID:",add[temp][0])
                print("Subject:",add[temp][1])
            else:
                print("No record is there!!")
        if b==6:
            break
if a==2:
    while True:
        print("\nMenu for Student's Portal:-")
        print("1.For adding new Students\n2.For display Student information\n3.For deleting the data of the Student")
        b=int(input("4.For updating Student information\n5.For searching Student information\n6.Quit\nEnter:"))
        if b==1:
            n=int(input("\nEnter number of Student to be added:"))
            for i in range(n):
                name=input("Enter Student's name:")
                i_d=int(input("Enter Student's admission number:"))
                c=int(input("Enter Class:"))
                add[name]=[i_d,c]
            print("Data added successfully!!")
        if b==2:
            if len(add)==0:
                print("No record found!!")
            else:
                print("------------------------------------------------\nName           Admission number         Class\n")
                for j in add:
                    print(j,"               ",add[j][0],"              ",add[j][1])
                print("\n------------------------------------------------")
        if b==3:
            if len(add)==0:
                print("No record is there!!")
            else:
                Name=input("Enter name of the Student whose data is to be removed:")
                add.pop(Name)
                print(Name+"'s data is removed!!")
        if b==4:
            while True:
                if len(add)==0:
                    print("No record is there to update!!")
                    break
                print("\nMenu,what do you want to update:-")
                u=int(input("1.Admission number\n2.Class\n3.Back\nEnter:"))
                if u==1:
                    NAME=input("Enter name of the Student who's Admission number is to be updated:")
                    ID=int(input("Input new Admission number:"))
                    s=add[NAME][1]
                    add[NAME]=[ID,s]
                    print("Record Updated!!")
                if u==2:
                    N=input("Enter name of the Student who's class is to be updated:")
                    C=input("Enter new class:")
                    PID=add[N][0]
                    add[N]=[PID,C]
                    print("Record Updated!!")
                if u==3:
                    break
        if b==5:
            temp=input("Enter name of the Student to find record:")
            if temp in add:
                print("Name:",temp)
                print("Admission number:",add[temp][0])
                print("Class:",add[temp][1])
            else:
                print("No record is there!!")
        if b==6:
            break
print("-------------------------------------------------------------------------------------")
print("\t\t\tThank You For Using")
print("-------------------------------------------------------------------------------------")
