#You are given the year, and you have to write a function to check if the year is leap or not.

def is_leap(year):
    leap = False
    
    if year % 4 == 0 and year % 100 == 0:
        if year % 400 == 0:
            leap = True
    elif year % 4 == 0:
        leap = True
    
    return leap

if __name__ == "__main__":
	year = int(input())
	print(is_leap(year))