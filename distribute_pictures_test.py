import distribute_pictures as dp

pairs = [(10, 20, "pic1"), (10, 7, "pic2"),
             (15, 10, "pic3"), (4, 10, "pic4"),
             (5, 8, "pic5"), (2, 3, "pic6"),
             (8, 4, "pic7")]


pairs2 = [(10, 10, "pic1"), (10, 10, "pic2"),
          (10, 10, "pic3"), (10, 10, "pic4"),
          (10, 10, "pic5"), (10, 10, "pic6"),
          (10, 10, "pic7"), (10, 10, "pic8"),
          (10, 10, "pic9"), (10, 10, "pic10"),
          (10, 10, "pic11"), (10, 10, "pic12")]

locations = dp.distribute_pictures(30, 40, pairs)
print("corner_x \tcorner_y \tsize_x \tsize_y \tname")
for loc in locations:
    print("{} \t\t\t{} \t\t\t{} \t\t{} \t\t{}".format(loc[0], loc[1], loc[2], loc[3], loc[4]))

print("")
locations = dp.distribute_pictures(30, 40, pairs2)
print("corner_x \tcorner_y \tsize_x \tsize_y \tname")
for loc in locations:
    print("{} \t\t\t{} \t\t\t{} \t\t{} \t\t{}".format(loc[0], loc[1], loc[2], loc[3], loc[4]))