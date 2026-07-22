#recursion
def factorial(n): 
    if n <= 1:                  # base case 
        return 1 
    return n * factorial(n - 1) # recursive case 
  
factorial(4)   # 4 * 3 * 2 * 1 = 24

#call stack
total([100, 250, 400]) 
  = 100 + total([250, 400]) 
  = 100 + 250 + total([400]) 
  = 100 + 250 + 400 + total([])   # base: returns 0 
  = 750

  # linear searching
  def linear_search(items, target): 
    for i, x in enumerate(items): 
        if x == target: 
            return i      # found 
    return -1             # not found 

    #binary searching
   def binary_search(items, target): 
    lo, hi = 0, len(items) - 1 
    while lo <= hi: 
        mid = (lo + hi) // 2 
        if items[mid] == target: 
            return mid 
        elif items[mid] < target: 
            lo = mid + 1      # go right 
        else: 
            hi = mid - 1      # go left 
    return -

     #merge sort
     def merge_sort(items): 

if len(items) <= 1:       # base case 
 
 return items 
 
 mid = len(items) // 2 
 
 left = merge_sort(items[:mid])   # recurse 
 
 right = merge_sort(items[mid:])  # recurse 

 return merge(left, right)        # combine in order

#built in-sort

nums.sort()   # in place; returns None                

new = sorted(nums)           # returns a new list 

sorted(nums, reverse=True)   # descending 



accounts.sort(key=lambda a: a.balance, reverse=True)

#two pointers

def has_pair(nums, target):       # nums is sorted 

lo, hi = 0, len(nums) - 1 

while lo < hi: 

s = nums[lo] + nums[hi] 

if s == target: return True 

elif s < target: lo += 1  # need a bigger value 

else: hi -= 1             # need a smaller value 

return False



#sliding window


def max_window(nums, k): 

window = sum(nums[:k]) 

best = window 

for i in range(k, len(nums)): 

window += nums[i] - nums[i - k]   # slide 

best = max(best, window) 

 return best 
