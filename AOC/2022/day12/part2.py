nbl = open('data.txt').read().split('\n')
total = 0

graph = {}
lista = []
for iline, line  in enumerate(nbl):
	lista.append([c for c in line])

index = 0
starts = []
end = 0

def charclosed(a, b):
	if ord(a) + 1 >= ord(b):
		return True
	return False

for iline, line  in enumerate(lista):
	for jrow, row  in enumerate(line):
		if row == 'S':
			lista[iline][jrow] = 'a'
			row = 'a'
		if row == 'E':
			end = index
			lista[iline][jrow] = 'z'
			row = 'z'
		if row == 'a':
			starts.append(index)
		tmp = []
		if jrow + 1 < len(line) and charclosed(row, line[jrow + 1]):
			tmp.append(index + 1)
		if jrow > 0 and charclosed(row, line[jrow - 1]):
			tmp.append(index - 1)
		if iline + 1 < len(lista) and charclosed(row, lista[iline + 1][jrow]):
			tmp.append(index + len(line))
		if iline > 0 and charclosed(row, lista[iline - 1][jrow]):
			tmp.append(index - len(line))
		graph[index] = tmp
		index += 1

# shortest_path funciton from onestepcode.com/graph-shortest-path-python
def shortest_path(graph, node1, node2):
    path_list = [[node1]]
    path_index = 0
    # To keep track of previously visited nodes
    previous_nodes = {node1}
    if node1 == node2:
        return path_list[0]
    while path_index < len(path_list):
        current_path = path_list[path_index]
        last_node = current_path[-1]
        next_nodes = graph[last_node]
        # Search goal node
        if node2 in next_nodes:
            current_path.append(node2)
            return current_path
        # Add new paths
        for next_node in next_nodes:
            if not next_node in previous_nodes:
                new_path = current_path[:]
                new_path.append(next_node)
                path_list.append(new_path)
                # To avoid backtracking
                previous_nodes.add(next_node)
        # Continue to next path in list
        path_index += 1
    # No path is found
    return []

maxlen = float('inf')
for s in starts:
	sp = shortest_path(graph, s, end)
	if len(sp) != 0:
		maxlen = min(len(sp), maxlen)
print('Part 2: {}'.format(maxlen + 1))

