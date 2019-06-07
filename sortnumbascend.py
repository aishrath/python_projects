neeturath_list = [-10, -1000, -100, 0, 10000, 100, 1000]
dundu_list = []

while neeturath_list:
  minimum = neeturath_list[0]
  for x in neeturath_list:
     if x < minimum:
        minimum = x
  dundu_list.append(minimum)
  neeturath_list.remove(minimum)

print(dundu_list)
