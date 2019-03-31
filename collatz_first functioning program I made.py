def collatz():
        integer = input("enter integer")
        try:
                integer = int(integer)        
                while integer != 1:
                        if integer % 2 == 0:
                                integer = (integer // 2)
                                print(integer)
                        else:
                                integer = (integer * 3 + 1)
                                print(integer)
                return (integer) 
        except ValueError:
                print('integers only')
collatz()
