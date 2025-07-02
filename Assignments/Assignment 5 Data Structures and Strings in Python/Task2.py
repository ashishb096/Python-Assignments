lst=[i+1 for i in range(10)]
print("Original list:",lst)

new_lst=lst[0:5]
print("Extracted first five elements:", new_lst)

rev_new_lst=new_lst[::-1]
print("Reversed Extracted elements:", rev_new_lst
      )