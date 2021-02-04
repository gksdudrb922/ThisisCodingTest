def solution(words,queries):
  reverse_words=[]
  for i in range(len(words)):
    reverse_words.append(words[i][::-1])
  reverse_words=sorted(reverse_words,key=lambda x:(len(x),x))
  words=sorted(words,key=lambda x:(len(x),x))
  result=[]
  print(words)
  print()
  print(reverse_words)

  for i in range(len(queries)):
    query=queries[i]
    if query[0]!='?':
      x=query[:len(query)-query.count('?')]
      count=count_by_value(words,x,len(query))
    else:
      query=query[::-1]
      x=query[:len(query)-query.count('?')]
      count=count_by_value(reverse_words,x,len(query))
    result.append(count)
  return result

def count_by_value(words,x,length):
  n=len(words)
  a=first(words,x,0,n-1,length)
  if a==None:
    return 0
  b=last(words,x,0,n-1,length)
  return b-a+1

def first(words,target,start,end,length):
  if start>end:
    return None
  mid=(start+end)//2
  if len(words[mid])==length and words[mid][:len(target)]==target and (mid==0 or length>len(words[mid-1]) or words[mid-1][:len(target)]!=target):
    return mid
  elif len(words[mid])<length or (len(words[mid])==length and words[mid][:len(target)]<target):
    return first(words,target,mid+1,end,length)
  else:
    return first(words,target,start,mid-1,length)

def last(words,target,start,end,length):
  if start>end:
    return None
  mid=(start+end)//2
  if len(words[mid])==length and words[mid][:len(target)]==target and (mid==len(words)-1 or length<len(words[mid+1]) or words[mid+1][:len(target)]!=target):
    return mid
  elif len(words[mid])>length or (len(words[mid])==length and words[mid][:len(target)]>target):
    return last(words,target,mid+1,end,length)
  else:
    return last(words,target,start,mid-1,length)



words=["frodo","front","frost","frozen","frame","kakao"]
queries=["fro??", "????o", "fr???", "fro???", "pro?"]
print(solution(words,queries))