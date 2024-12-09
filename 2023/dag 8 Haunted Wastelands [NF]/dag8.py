from dag8funct import readfile_dict_2_array, zoekroute, zoekroute_multi



route, dict = readfile_dict_2_array("dag8.txt")


            
print("Deel 1: ",zoekroute(route, dict))
print("Deel 2: ",zoekroute_multi(route, dict))