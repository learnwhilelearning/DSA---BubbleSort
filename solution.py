#there are two code, run them seperately

#challenge 1
def bubble_sort(arr):
  
  end = len(arr)

  for i in range(end-1):
    for j in range(end -1):
      if (arr[j]<arr[j+1]):
        tmp = arr[j]
        arr[j]=arr[j+1]
        arr[j+1]=tmp
  
if __name__=='__main__':
  elements = [11,5,9,1,6,14,12,11,13]

  bubble_sort(elements)
  print(elements)



