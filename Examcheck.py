a=int(input('enter your attendence'))
medicalcause =(input ('do you have a medical cause'))
if medicalcause == 'yes':
 print('your are allowed')
else:
 if a>=75:
  print('allowed')
 else:
  print('not allowed')