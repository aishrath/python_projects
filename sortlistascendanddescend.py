neeturath_list = [-10, -1000, -100, 0, 10000, 100, 1000] 
neetu_list = [] 
dundu_list = []

while neeturath_list:
   minimum = neeturath_list[0] 
   for x in neeturath_list: 
      if x < minimum: 
         minimum = x 
   neetu_list.append(minimum)
   neeturath_list.remove(minimum)

print(neetu_list)

neeturath_list = neetu_list
print(neeturath_list)

while neeturath_list:
   maximum = neeturath_list[0] 
   for x in neeturath_list: 
      if x > maximum: 
         maximum = x 
   dundu_list.append(maximum)
   neeturath_list.remove(maximum)

print(dundu_list)
