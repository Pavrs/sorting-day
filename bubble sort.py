# [program name]
# Pavel Stoimenov
# [date]
# AS Computer Science

# [for loop]
def one():
    try:
        items = [23, 41, 11, 17, 34, 56]
        n = len(items) -1
        
        for x in range(0,n):
            for index in range(0, n):
                if items[index]>items[index+1]:
                    temp = items[index]
                    items[index] = items[index+1]
                    items[index+1] = temp
        print(items)
        print(f'length of the list {n}')
        pass   
    except Exception as e:
        print("Error occurred:", e )

# [while loop]
def two():
    try:
        items = [23, 41, 11, 17, 34, 56]
        n = len(items)-1
        swapped=True

        while swapped and n >0:
            swapped = False
            for index in range(0,n):
                if items[index] > items[index+1]:
                    temp = items[index]
                    items[index] = items[index+1]
                    items[index+1] = temp
                    swapped = True
            n -= 1
        print(items)
            
        pass   
    except Exception as e:
        print("Error occurred:", e )

# [random while loop]
def three():
    try:
        import random
        y=50
        
        items = [random.randint(0,10000) for x in range(y)]
        n = len(items)-1
        swapped=True

        while swapped and n >0:
            swapped = False
            for index in range(0,n):
                if items[index] > items[index+1]:
                    temp = items[index]
                    items[index] = items[index+1]
                    items[index+1] = temp
                    swapped = True
            n -= 1
        print(items)
            
        pass   
    except Exception as e:
        print("Error occurred:", e )

# [random while loop]
def four():
    try:
        import random,time
        start = time.time()
        y=100000
        
        items = [random.randint(0,10000) for x in range(y)]
        n = len(items)-1
        swapped=True

        while swapped and n >0:
            swapped = False
            for index in range(0,n):
                if items[index] > items[index+1]:
                    temp = items[index]
                    items[index] = items[index+1]
                    items[index+1] = temp
                    swapped = True
            n -= 1
        print(items)

        end=time.time()
        speed= round(end-start,5)
        print(f'Time taken: {speed}')
            
        pass   
    except Exception as e:
        print("Error occurred:", e )
# bubble sort with time
def five():
    try:
        import random,time
        start = time.time()
        y=100000
        items = [random.randint(0,10000) for x in range(y)]
        n = len(items) -1
        

        
        for x in range(0,n):
            for index in range(0, n):
                if items[index]>items[index+1]:
                    temp = items[index]
                    items[index] = items[index+1]
                    items[index+1] = temp
        print(items)
        print(f'length of the list {n}')

        end=time.time()
        speed= round(end-start,5)
        print(f'Time taken: {speed}')
        pass   
    except Exception as e:
        print("Error occurred:", e )

# [while loop with time]
def six():
    try:
        
        import random,time
        start = time.time()
        y=100000
        items = [random.randint(0,10000) for x in range(y)]
        n = len(items) -1
        swapped=True

        while swapped and n >0:
            swapped = False
            for index in range(0,n):
                if items[index] > items[index+1]:
                    temp = items[index]
                    items[index] = items[index+1]
                    items[index+1] = temp
                    swapped = True
            n -= 1
        print(items)

        
        end=time.time()
        speed= round(end-start,5)
        print(f'Time taken: {speed}')
        
        pass   
    except Exception as e:
        print("Error occurred:", e )




# [comment]
def main():
    try:
        six()
        pass   
    except Exception as e:
        print("Error occurred:", e )    

if (__name__ == "__main__"):
    main()
