
r=int(input())
s=r*r
area=3.14*s
print(area)


v=input()
count=0
for i in v:
  if i in 'aeiouAEIOU':
    count=count+1
print(count)



s=input()
count=0
for i in s:
    if i not in 'AEIOUaeiou':
        count+=1
print(count)




l = [30, 42, 56, 70, 45, 35]
l1 = []

for i in l:
    if i % 5 == 0:
        l1.append(i - 5)
    else:
        l1.append(i)

print(l1)





l=[20,35,45,30,60,75,85,45,25,40]
l1=[]
l2=[]
for i in (l):
    if (l.index(i)%2==0):
        l1.append(i)
    else:
        l2.append(i)
print(l1)
print(l2)






l = [20, 35, 45, 30, 60, 75, 85, 45, 25, 40]
l1 = []
l2 = []

for i in l:
    if i % 2 == 0:
        l1 = l1 + [i]
    else:
        l2 = l2 + [i]

print( sum(l1))
print( sum(l2))





l = [20, 35, 45, 30, 60, 75, 85, 45, 25, 40]
l1 = []
l2 = []

for i in range(len(l)):
    if l[i] % 2 == 0:
        l1 = l1 + [i]
    else:
        l2 = l2 + [i]

print(sum(l1))
print(sum(l2))





l = ['ojas', 'ghambeera', 'surya', 'devara', 'arjun', 'sarkar', 'rocky', 'saaho', 'deva','Dhanush']
n = []
for name in l:
    if name[0].lower() == 'd':
        n.append(name)
print(n)





s = {'mumbai': 50, 'hyd': 40, 'delhi': 30, 'dubai': 20, 'jaipur': 100, 'kol': 350, 'chennai': 200, 'dadar': 200}

for i in s:
    if s[i] < 100:
        print(i)




s = {'mumbai': 50, 'hyd': 40, 'delhi': 30, 'dubai': 20, 'jaipur': 100, 'kol': 350, 'chennai': 200, 'dadar': 200}

def City_le(s):
  l = []
  for i in s:
    if (s[i] < 100):
      l.append(i)
  return l

print(City_le(s))





def calc_area(r):
  s=r*r
  a=3.14*s
  return a

r=int(input())
print(calc_area(r))




def count_vowels(v):
  c=0
  for i in v:
    if i in 'aeiouAEIOU':
      c=c+1
  return c

v=input()
print(count_vowels(v))





def process_list(l):
  l1 = []
  for i in l:
    if i % 5 == 0:
      l1.append(i - 5)
    else:
      l1.append(i)
  return l1

l = [30, 42, 56, 70, 45, 35]
print(process_list(l))






def split_list(l):
  l1=[]
  l2=[]
  for i in range(len(l)):
    if i % 2 == 0:
      l1.append(l[i])
    else:
      l2.append(l[i])
  return l1, l2

l=[20,35,45,30,60,75,85,45,25,40]
l1, l2 = split_list(l)
print(l1)
print(l2)




def sum_even_odd(l):
  l1 = []
  l2 = []
  for i in l:
    if i % 2 == 0:
      l1 = l1 + [i]
    else:
      l2 = l2 + [i]
  print(sum(l1))
  print(sum(l2))

l = [20, 35, 45, 30, 60, 75, 85, 45, 25, 40]
sum_even_odd(l)





def sum_even_odd(l):
  l1 = []
  l2 = []
  for i in range(len(l)):
    if l[i] % 2 == 0:
      l1 = l1 + [l[i]]
    else:
      l2 = l2 + [l[i]]
  print(sum(l1))
  print(sum(l2))

l = [20, 35, 45, 30, 60, 75, 85, 45, 25, 40]
sum_even_odd(l)





def filter_names(l):
  n = []
  for name in l:
    if name[0].lower() == 'd':
      n.append(name)
  return n

l = ['ojas', 'ghambeera', 'surya', 'devara', 'arjun', 'sarkar', 'rocky', 'saaho', 'deva','Dhanush']
print(filter_names(l))





def vow(text):
    vowels= "aeiouAEIOU"
    vowel=[]
    cons = []
    count1=0
    count2=0
    for i in text:
        if i.isalpha():
            if i in vowels:
                count1 += 1
            else:
                count2 += 1
    return count1,count2
text = input()
count1,count2=vow(text)

print("Vowel:", count1)
print("Cons:", count2)





def count(s):
  v=0
  c=0
  if ghgh:
    c+=1
  else:
    v+=1
  return{'vowel ':v,'const':c}