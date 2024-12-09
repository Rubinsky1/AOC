def readfile_dict_2_array(infile):
    my_dict = {}
    with open(infile, "r") as file:
        lines = file.readlines()

    route = lines[0]

    for line in lines[2:]:
        line = line.strip()
        key, value = line.split(" = ")
        left, right = value[1:-1].split(", ")
        my_dict[key] = (left, right)
    return route, my_dict

def zoekroute(route, dict):
    stap = "AAA"
    aantal = 0
    while(True):
        for i in range(len(route)):
            afslag = route[i]
            if(afslag == 'L'):
                stap = dict[stap][0]
            elif(afslag == 'R'):
                stap = dict[stap][1]
            else:
                aantal -=1
            aantal += 1
            if(stap == "ZZZ"):
                return aantal


def zoekroute_multi(route, network):
    # Step 1: Identify all starting nodes ending with "A"
    nodes = [node for node in network if node.endswith("A")]
    aantal = 0  # Step counter
    
    # Step 2: Process until all active nodes end with "Z"
    while True:
          # To store the next active nodes after this step
        for i in range(len(route)):
            afslag = route[i]
            if aantal == 2:
                print("doesnot work")
            if afslag == 'L' or afslag == 'R':
                next_nodes = []
                for node in nodes:
                    # Determine the next node based on the current instruction
                    if afslag == 'L':
                        next_nodes.append(network[node][0])
                    elif afslag == 'R':
                        next_nodes.append(network[node][1])
                    
        # Check if all active nodes end with "Z"
                aantal += 1
                if all(node.endswith("Z") for node in next_nodes):
                    return aantal  # All nodes are "Z", return the step count
            
                nodes = next_nodes