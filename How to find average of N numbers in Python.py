num = int (input("How many numbers that you need to avrage for?"))
total_sum = 0

for n in range (num):
    numbers = float(input("Enther he number:"))
    total_sum += numbers

avg = total_sum/num

print ("Avrage is:" , avg)