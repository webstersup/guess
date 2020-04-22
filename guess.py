#產生一個隨機整數1~100(不要印出來)
#讓使用者重複輸入數字去猜
#猜對的話 印出"終於猜對了"
#猜錯的話 要告訴他比答案大還是答案小


import random

r = random.randint(1,100)
while True :
	ans = input('請輸入數字:')
	ans = int(ans)
	if ans == r :
		print('終於猜對了')
		break
	elif ans < r :
		print('你猜的數字比答案小')
	elif ans > r :
		print('你猜的數字比答案大')

