
def partition(arr, lo, hi):
	pivot = arr[lo]

	l = lo
	r = hi-1
	while True:
		while l < r and arr[l] < pivot:
			l += 1
		while r > l and arr[r] > pivot:
			r -= 1
		if l == r:
			return l
		temp=arr[l]
		arr[l]=arr[r]
		arr[r]=temp


def qsh(arr, lo, hi):
	if lo >= hi-1: #length 1 since hi is not inclusive
		return
	#partition
	split = partition(arr, lo, hi)

	qsh(arr, lo, split)
	qsh(arr, split+1, hi)


def quicksort(arr):
	qsh(arr, 0, len(arr))

arrays=[
	[1, 5, -4, 15, 6, 3, 9],
	[1],
	[5, 1],
	[4, 3, 2, 1],
	[1, 2, 3, 4]
]
for arr in arrays:
	quicksort(arr)
	print(arr)