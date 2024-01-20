start_loop = int(input("What is the start loop point? "))
end_loop = int(input("What is the end loop point? "))

loop_length = end_loop - start_loop

found = False

for i in range(start_loop):
    n1 = start_loop - i
    n2 = end_loop - i
    
    if n1 % 16 == 0 and n2 % 16 == 0:
        print("Start loop point:", n1, "\nEnd loop point:", n2)
        found = True
        
if not found:
    print("Nothing was found.")
