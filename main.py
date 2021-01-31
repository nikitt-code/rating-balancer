stars = {
  5: 4,
  4: 0,
  3: 0,
  2: 0,
  1: 0
}
add = 3

sum_bad = stars[1] + stars[2] + stars[3]
sum_good = stars[4] + stars[5]

if add <= 3 and sum_good//2 > sum_bad:
  stars[add+1] += 1
elif add >= 3 and sum_bad//2 >= sum_good and (stars[1]+stars[2])//2 > stars[3]:
  stars[add-1] += 1
else:
  stars[add] += 1

print(stars)