X = int(input())

sticks = [64]
stick_length = 64

while stick_length != X:
  shortest_stick = sticks.pop()
  half_stick = shortest_stick / 2
  stick_length = half_stick + sum(sticks)
  sticks.append(half_stick)
  if stick_length < X:
    sticks.append(half_stick)

  sticks.sort(reverse=True)

print(len(sticks))