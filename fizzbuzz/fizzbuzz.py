#Print a sequence of numbers
#Multiples of 3 are replaced with "fizz"
#Multiples of 5 are replaced with "buzz"
#Multiples of 3 & 5 are replaced with "fizzbuzz"
#Do this for n numbers

n = 100

for i in range(1,n+1): #range is lower inclusive and upper exclusive
	output=""
	if not i%3:
		output+="fizz"
	if not i%5:
		output+="buzz"
	if output == "":
		output+=str(i)
	print(output)
