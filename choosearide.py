print('select your ride')
print('1.bike')
print('2.car')
choice=int(input('enter your choice'))
if choice==1:
 print('what type of bike')
 print('1.scooty')
 print('2.hardtail')
 choice2=int(input('enter your choice'))
 if choice2==1:
  print('you have selected scooty')
 else:
  print('you have selected hardtail')
elif choice==2:
 print('what type of car')
 print('1.sadan')
 print('2.suv')
 choice3=int(input('enter your choice'))
 if choice3==1:
  print('you have selected sadan')
 else:
  print('you have selected suv')
else:
 print('wrong choice')