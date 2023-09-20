for number in range(2, 100):
  for factor in range(2, int(number**0.5)):
    if number % factor == 0:
      break
  else: 
      print(f'{number} is prime!')
   