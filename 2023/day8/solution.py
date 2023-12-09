import math

def parsed_input(lines):
    parsed_lines = lines.split('\n\n')

    instructions = parsed_lines.pop(0).strip()

    instructions = instructions.replace('R', '1').replace('L', '0')
    nodes = parsed_lines[0].strip().split('\n')

    node_neighbour = {}
    for node in nodes:
        node_neighbour[node.strip().split('=')[0].strip()] = node.strip().split('=')[1].strip()[1:-1].split(', ')
    return node_neighbour, instructions

def get_nodes(node_neighbour):
    starting_nodes = []
    ending_nodes = []
    for node, node_neighbour in node_neighbour.items():
        if node[-1] == 'A':
            starting_nodes.append(node)
        elif node[-1] == 'Z':
            ending_nodes.append(node)
    return starting_nodes, ending_nodes

def part_one(lines):
    node_neighbour, instructions = parsed_input(lines)
    current_node = 'AAA'
    count = 0
    while current_node != 'ZZZ':
        for instruction in instructions:
            current_node = node_neighbour[current_node][int(instruction)]
            count += 1
            if current_node == 'ZZZ':
                return count
        
def part_two(lines):
    node_neighbour, instructions = parsed_input(lines)
    starting_nodes, ending_nodes = get_nodes(node_neighbour)

    paths = []
    for current_node in starting_nodes:
        count = 0
        while current_node not in ending_nodes:
            for instruction in instructions:
                current_node = node_neighbour[current_node][int(instruction)]
                count += 1
                if current_node in ending_nodes:
                    paths.append(count)
                    break
    return math.lcm(*paths)

with open('input.txt') as file:
    lines = file.read().strip()

print(part_one(lines))

print(part_two(lines))