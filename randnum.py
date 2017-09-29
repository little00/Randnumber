from datetime import datetime
import pytz

tz = pytz.timezone('Asia/Kolkata')
timenow =  int(datetime.now(tz).strftime("%S"))


def largernum(startrand, endrand,large, timenow):
  
  # 1st find number from 73% bias
  
  for num1 in range(large, endrand+1):
    
    for x in range(1, 74):
      seed = int(timenow)*x
      num = round(seed / num1)
      
      if large <= num <= endrand:
        return num
    
    # to stop getting same number i.e to increase randomness
    p = round(seed % num1)
    if large <= p <= endrand:
      return p
        
    
  return endrand
  
# ====================================================
# smaller number
# ====================================================

def smallernum(startrand, endrand,large, timenow):
  
  # 2nd find number from 27% bias
  
  for num1 in range(startrand, large):
    
    for x in range(74, 101):
      seed = int(timenow)
      num = seed % x
      
      if startrand <= num < large:
        return num
        
   
  return num1

startrand = int(input("Input start point of Random number? "))
endrand =  int(input("Input end point of Random number? "))

# Biasing calculation
large = round((endrand)/2) + 1

quant = int(input("How many Random number do you want to generate? "))

for i in range(1, quant):
  timenow = timenow + i
  
  if i <= 73:
    rand_num = largernum(startrand, endrand,large, timenow)
    print(rand_num)
  else:
    rand_num = smallernum(startrand, endrand,large, timenow)
    print(rand_num)
  
  
  
  