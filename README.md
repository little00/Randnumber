1. Input range of random number

startrand = int(input("Input start point of Random number? "))
endrand = int(input("Input end point of Random number? "))

2. Find starting point to larger number

large = round((startrand + endrand)/2) + 1

3. Input how many random number you want to generate

quant = int(input("How many Random number do you want to generate? "))

4. Set up seed value to generate random number

timenow =  int(datetime.now(tz).strftime("%S"))


5. Generate 73 % larger number and 27 % smaller number

for i in range(1, quant):
  timenow = timenow + i
  
  if i <= 73:
    rand_num = largernum(startrand, endrand,large, timenow)
    print(rand_num)
  else:
    rand_num = smallernum(startrand, endrand,large, timenow)
    print(rand_num)






#====================================================
Genarate Larger Number
#===================================================

def largernum(startrand, endrand,large, timenow):

1. Genarate 100 % larger number i.e  large <= num <= endrand

2. For every num1 try 73 possibilities to generate random number in range (large, endrand+1)
    
for num1 in range(large, endrand+1):
    
    # Increase seed value by x bcoz (larger / num1) < (larger*x / num1) == more possibility for number to fall in range of largerer number pool

    for x in range(1, 74):
      seed = int(timenow)*x
      num = round(seed / num1)
      
      if large <= num <= endrand:
        return num
    
    # to stop getting same larger number most frequently i.e to increase randomness

    p = round(seed % num1)
    if large <= p <= endrand:
      return p

3. In worst case return fix larger number in range
    
return endrand



#====================================================
Genarate Smaller Number
#===================================================

def smallernum(startrand, endrand,large, timenow):

1. Genarate 100 % smaller number i.e  startrand <= num <= large

2. For every num1 try 27 possibilities to generate random number in range (startrand, large)
    
for num1 in range(startrand, large):
    
    # decrease seed value by x to produce smaller number in range
    for x in range(74, 101):
      seed = int(timenow)
      num = seed % x
      
      if startrand <= num < large:
        return num
        
   
3. In worst case return fix smaller number in range

return num1
