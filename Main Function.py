#main
def main1():
    import menu    
    print('-'*80)
    s='WELCOME TO LIBRARY MANAGEMENT SYSTEM '
    print(s.center(80))
    print('-'*80)
    print()
    ch=-1
    while ch!=0:
        print("\t Welcome to LMS \n")
        print("1. Insert Record of New Book ")
        print("2. Search For a Particular Book Record ")
        print("3. Display All Book Records")
        print("4. Exit ")
        ch=int(input('Enter your choice : '))

        if ch==1:
            menu.insert()
        elif ch==2:
            menu.search()
        elif ch==3:
            menu.display()
        elif ch!=4:
            print('Invalid Option')
            print()

    
