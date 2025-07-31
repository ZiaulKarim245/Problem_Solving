n , t = map(int,input().split())
time = list(map(int,input().split()))
cnt = 0
total_time = 0
for i in time:
    total_time += i
    if total_time > t:
       total_time -= time[cnt]
       cnt += 1
print(n - cnt)
   			 	 	 		 			 		 	 	 		   	