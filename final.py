def prog():
    print("\n ************WELCOME TO  Program ************")
    print(  "\n 1.parseing  a log file and extracting all information from it like ip,url,...")
    print(  " \n 2.monitoring file ")
    print(  " \n 3.scanning ports ")
    print(  "\n 4.detecting attack \n")
  
  
   

while loop:
    prog()
    choice=input("Please enter your choice:" )

    if choice == 1:
        exec(open("extracting info from log file.py").read())

    elif choice == 2:
        exec(open("monitor sys.py").read())

    elif choice == 3:
        exec(open("scanning.py").read())

    elif choice == 4:
      
       
        exec(open(socket__client.py) 
        exec(open("attack detection.py").read())
        
    else:
        print("\n Please try again ")
        prog()