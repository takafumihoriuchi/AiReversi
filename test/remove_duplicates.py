def remove_duplicates(list):
  if list == []:
    return []
  ans = []
  ans.append(list[0])
  for i in range(1,len(list)):
    dirtybit = 0
    for j in ans:
      if list[i]==j:
        dirtybit = 1
    if dirtybit==0:
      ans.append(list[i])
  return ans
  
print(remove_duplicates([1,1,2,2,3,4,5,5]))