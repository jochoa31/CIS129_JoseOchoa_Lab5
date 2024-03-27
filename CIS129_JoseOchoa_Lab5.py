#Jose Ochoa 
#3/26/2024
#This program counts bottle returns for the week
#and calculates total payment for returned bottles

#These are the variables
total_bottles = 0
today_bottles = 0
counter = 1
total_payout = 0

#Bottles returned and total for each day
while counter <= 7:
  today_bottles = int(input(f'Enter the number of bottles retured on day {counter} '))
  total_bottles += today_bottles
  total_payout = total_payout + total_bottles * .10
  counter += 1  
  print(f'Total bottles so far for this week: {total_bottles}')
  keep_going = input('Do you have more entries? y/n  ')
  if keep_going != 'y':
    break
  print(f'Total bottles so far for this week: {total_bottles}')

  
print(f'These are to total bottles for this week,{total_bottles}, and this is the payout: ${total_payout:<10.2f}')