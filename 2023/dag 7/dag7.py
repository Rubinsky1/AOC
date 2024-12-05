from dag7funct import sort, sort2, readfile_2_array

hands, bids = readfile_2_array("dag7.txt")
print("deel 1: ",sort(hands, bids))
print("deel 2: ", sort2(hands, bids))
