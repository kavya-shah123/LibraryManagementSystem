#menu for library management
import dt
def insert():
        print()
        print("\nEnter Book Details in the Following Order (ONLY):")
        print()
        name=input('Enter Book Name : ')
        bid=input('Enter Book ID : ')
        author=input('Enter Author Name : ')
        price=float(input('Enter Price : '))
        q=int(input('Enter Quantity : '))

        fp=open('books.txt','a+')
        fp.write(name + '     '+bid + '     ' +author+ '        '+str(price)+'        '+str(q)+'\n')
        fp.close()
        print()
        print("Record Inserted Successfully !!! " )
        print()
        



def search():
        print()
        ch=-1
        f=0
        c=0
        print('Select Option to Search From the List Provided Below.')
        print("Enter Search Criteria \n\ 1. Book Name\n 2. Book ID \n 3. Author Name\
                   \nPlease enter (from 1-3):")
        
        ch=int(input('Enter your choice : '))

        if ch==1:
                print()
                query=input('Enter the Name of the Book You Wish to search : ')
                fp=open("books.txt","r")
                m=fp.readlines()
                for i in m:
                    w=i.split(',')
                    #print()
                    for j in w:
                        if w[1]==query:
                                if f==0:
                                        print()
                                        print('-'*100)
                                        print('Book Name'.ljust(9)+'Book ID'.ljust(20)+'Author'.ljust(20)+'Price'.ljust(20)+'Quantity'.ljust(20))
                                        print('-'*100)
                                f=1
                                
                                if j==w[0]:
                                    print(j.ljust(9),end=" ")
                                else:
                                    print(j.ljust(20),end=" ")
                        else:
                                continue
                      
                if f==0:
                        print('No Records !!!')
                        print()
                fp.close()
                print()
        elif ch==2:
                print()
                query=input('Enter Book ID : ')
                fp=open("books.txt","r")
                m=fp.readlines()
                for i in m:
                    w=i.split(',')
                    #print()
                    for j in w:
                        if w[2]==query:
                                if f==0:
                                        print()
                                        print('-'*100)
                                        print('Book Name'.ljust(9)+'Book ID'.ljust(20)+'Author'.ljust(20)+'Price'.ljust(20)+'Quantity'.ljust(20))
                                        print('-'*100)
                                f=1
                                
                                if j==w[0]:
                                    print(j.ljust(9),end=" ")
                                else:
                                    print(j.ljust(20),end=" ")
                        else:
                                continue
                      
                if f==0:
                        print('No Records !!!')
                        print()
                fp.close()
                print()
        elif ch==3:
                print()
                query=input('Enter Name of the Author : ')
                fp=open("books.txt","r")
                m=fp.readlines()
                for i in m:
                    w=i.split(',')
                    print()
                    for j in w:
                        if w[3]==query:
                                if f==0:
                                        print()
                                        print('-'*100)
                                        print('Book Name'.ljust(9)+'Book ID'.ljust(20)+'Author'.ljust(20)+'Price'.ljust(20)+'Quantity'.ljust(20))
                                        print('-'*100)
                                f=1
                                
                                if j==w[0]:
                                    print(j.ljust(9),end=" ")
                                else:
                                    print(j.ljust(20),end=" ")
                        else:
                                continue
                      
                if f==0:
                        print('No Records !!!')
                        print()
                fp.close()
                print()
        else:
                print('Invalid !!!')
                print()
                

                
def display():
        fp=open("books.txt","r")
        #a=fp.read()
        print()
        print('-'*100)
        print('Book Name '.ljust(9)+' Book ID'.ljust(15)+'Author'.ljust(15)+'Price'.ljust(10)+'Quantity'.ljust(10))
        print('-'*100)
        print()
        #m=a.split('\n')
        m=fp.readlines()
        for i in m:
            w=i.split(',')
            print()
            for j in w:
                if j==w[0]:
                    print(j.ljust(9),end=" ")
                else:
                    print(j.ljust(15),end=" ")

        fp.close()
        print()
        print('-'*100)
        print()
 






