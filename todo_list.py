works = []
def add():
    work = input("Kare khod ra vared konid:")
    if work in works:
        print("in mored vojod dare!")
        return add()
    elif work == 'menu':
        return menu()
    works.append(work)
    while True:
        answer = input("mikahi add koni?(y,n):")
        if answer.lower() == 'y':
            return add()
        elif answer.lower() == 'n':
            break
        else:
            print("lotfan bein (y/n) entekhab kon.")
    menu()
def show():
    print("========works========")
    for i in range(len(works)):
        print(f"{i+1}.{works[i]}")
    print("=====================")

def show_info():
    print("========works========")
    for i in range(len(works)):
        print(f"{i+1}.{works[i]}")
    print("=====================")
    answer = input("for menu 'menu'/for exit 'e'.")
    if answer == 'menu':
        return menu()
    elif answer == 'e':
        print('exit...')
    else:
        print("error...")
        return show_info()

def delete():
    while True:
        if not works:
            print("no works here! add somthing.")
            return add()
        show()
        num = input("az bein in mavared kdom shomare ro mikhai hazf koni:")
        if num == 'menu':
            break
        try:
            works.remove(works[int(num)-1])
        except ValueError:
            print("lotfan adad vared konid/adad bayad dar list bashad.")
            continue
        answer = input('mikhai adame bedi (y/n):')
        if answer.lower() == 'y':
            continue
        elif answer.lower() == 'n':
            break
        else:
            print("lotfan bein (y/n) entekhab kon.")
    menu()

def menu():
    print("""
    all works you can do:
          1.add
          2.show
          3.delete
          if ur want to back to menu just type 'menu'.
          if you want to exit just type 'e'.      
""")
    answer = input("choose between this 3 number:")
    if answer == "1":
        return add()
    elif answer == "2":
        return show_info()
    elif answer == "3":
        return delete()
    elif answer == "e":
        print("you exit...")
    else:
        print("please choose between 1 to 3.")
        return menu()

menu()