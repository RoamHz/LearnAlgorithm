def quicksort(mylist, start, end):
	if start < end:
		key = partition(mylist, start, end)
		quicksort(mylist, start, key)
		quicksort(mylist, key+1, end)

def partition(mylist, start, end):
	i = start-1
	for j in range(len(num)):
		if mylist[j] <= mylist[end-1]:
			i = i + 1
			mylist[i], mylist[j] = mylist[j], mylist[i]
	mylist[i+1], mylist[end-1] = mylist[end-1], mylist[i+1]
	return i+1

num = [1, 7, 6, 5, 3, 10 ,6]
quicksort(num, 0, len(num)-1)
