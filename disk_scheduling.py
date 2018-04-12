from heapq import *
# hp is initial head position
# and requests is the list of requests
# no of cylinders is 200
def FCFS(hp,requests):
	time = 0
	n = len(requests)
	pos = hp
	for request in requests:
		time += abs(request-pos)
		pos = request
		print("        ",pos,"  seeked")

	# calculate average seek time
	avg_seek_time = time / n
	return avg_seek_time

# Shortest Seek Time First
def SSTF(hp,reqs):
	requests = reqs.copy()
	time = 0
	position = hp
	n = len(requests)
	heap=[]
	while len(requests)>0:
		for r in requests:
			heappush(heap,(abs(position-r),r))
		x=heappop(heap)[1]
		time+=abs(position-x)
		position=x
		print("        ",x,"  seeked")
		requests.remove(x)
		heap=[]

	# calculate average seek time
	avg_seek_time = time/n
	return avg_seek_time

def SCAN(hp,reqs):
	requests = reqs.copy()
	pos = hp
	time = 0
	end=200
	start=0
	#seek from curr_pos to end which is 200
	for i in range(pos,end+1):
		if i in requests:
			time+=abs(pos-i)
			pos=i
			print("        ",i,"  seeked")
			requests.remove(i)

	time+=abs(pos-end)
	pos=end
	#seek back to start
	for i in range(end,start-1,-1):
		if i in requests:
			time+=abs(pos-i)
			# print(time)
			pos=i
			print("        ",i,"  seeked")
			requests.remove(i)
	print(time)
	# calculate average seek time
	avg_seek_time = time/n
	return avg_seek_time

def C_SCAN(hp,reqs):
	requests = reqs.copy()
	pos = hp
	time = 0
	end=200
	start=0
	#seek from curr_pos to end which is 200
	for i in range(pos,end+1):
		if i in requests:
			time+=abs(pos-i)
			pos=i
			print("        ",i,"  seeked")
			requests.remove(i)
	time+=abs(pos-end)
	pos=end
	#seek to hp from start
	for i in range(start,hp+1):
		if i in requests:
			time+=abs(pos-i)
			pos=i
			print("        ",i,"  seeked")
			requests.remove(i)
	
	# calculate average seek time
	avg_seek_time = time/n
	return avg_seek_time

def LOOK(hp,reqs):
	requests = reqs.copy()
	pos = hp
	time = 0
	end=max(requests)
	start=min(requests)
	#seek from curr_pos to end which is 200
	for i in range(pos,end+1):
		if i in requests:
			time+=abs(pos-i)
			pos=i
			print("        ",i,"  seeked")
			requests.remove(i)

	#seek back to start
	for i in range(end,start-1,-1):
		if i in requests:
			time+=abs(pos-i)
			pos=i
			print("        ",i,"  seeked")
			requests.remove(i)
	print(time)
	# calculate average seek time
	avg_seek_time = time/n
	return avg_seek_time

def C_LOOK(hp,reqs):
	requests = reqs.copy()
	pos = hp
	time = 0
	end=max(requests)
	start=min(requests)
	#seek from curr_pos to max of list 
	for i in range(pos,end+1):
		if i in requests:
			time+=abs(pos-i)
			pos=i
			print("        ",i,"  seeked")
			requests.remove(i)

	time+=abs(pos-start)
	pos=start
	#seek to hp from start
	for i in range(start,hp+1):
		if i in requests:
			time+=abs(pos-i)
			pos=i
			print("        ",i,"  seeked")
			requests.remove(i)
	
	# calculate average seek time
	avg_seek_time = time/n
	return avg_seek_time

if __name__=='__main__':
	print("DISK SCHEDULING:")
	print("Provide number of I/O requests")
	#n is the number of I/O requests
	n = int(input())
	print("Provide initial position of disc arm (total cylinders=200)")
	hp = int(input())
	while hp>200:
		print("!!! INVALID !!! try again")
		hp = int(input())	
	print("Provide positions to visit : max is 200")
	requests = []
	for i in range(n):
		req = int(input())
		requests.append(req)

	print(requests)

	#calling the functions
	print("  **********     FCFS       *********")
	print("Avg seek time for  fcfs was ",
		FCFS(hp,requests))
	print("  **********     SSTF       *********")
	print("Avg seek time for  sstf was ",
		SSTF(hp,requests))
	print("  **********     SCAN       *********")
	print("Avg seek time for  scan was ",
		SCAN(hp,requests))
	print("  **********     C-SCAN     *********")
	print("Avg seek time for  C-scan was ",
		C_SCAN(hp,requests))
	print("  **********     LOOK       *********")
	print("Avg seek time for  look was ",
		LOOK(hp,requests))
	print("  **********     C-LOOK     *********")
	print("Avg seek time for  C-look was ",
		C_LOOK(hp,requests))
	print("  **********     Thanks       *********")
