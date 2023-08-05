# Treasure Map - Where do you want to want to hide your treasure.

row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]

map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

position = input("Where do you want to hide the treasure? ")

row = int(position[0])
col = int (position[1])

map[col -1][row -1] = "X"

print(f"{row1}\n{row2}\n{row3}")

