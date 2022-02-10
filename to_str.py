# Convert arbitary integer to string with base from 2 to 16 

def to_str(num, base):
	lookUpStr = "0123456789ABCDEF"
	if num < base:
		return lookUpStr[num]
	else:
		return to_str(num // base, base) + lookUpStr[num % base]


if __name__ == "__main__":
	num = int(input("Input number is: "))
	base = int(input("Base is: "))
	print("Converted to {} with a base of {}".format(to_str(num,base), base))

