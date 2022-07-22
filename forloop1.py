for i in range(5):
	print('Hello',i)

print('----Loop in List----')
friend = ['Korkai','Khorkai','Khorkwai','Somchai','Somsak']

for f in friend:
	print(f)
	if f == 'Korkai':
		print('สวัสดีคุณก.ไก่')
	else:
		print('สวัสดีคุณลูกค้า')
print('----Loop in Dictionary----')

friend2 = {'Korkai':'คุณก.ไก่',
		   'Khorkai':'คุณข.ไข่',
		   'Somchai':'คุณสมชาย'}

for f in friend2:
	print(f)

for k,v in friend2.items():
	print('Key:',k)
	print('Value:',v)


for f in friend2.keys():
	print(f)


for f in friend2.values():
	print(f)


for i,f in enumerate(friend,start=1000):
	print(i,f)


for i,f in enumerate(friend2.items()):
	print(i,f)

for i,(k,v) in enumerate(friend2.items()):
	print(i,k,v)