with open('input.txt') as file:
    assignment_sections = file.read().strip().split('\n')


fully_contained_pairs = 0
overlapping_pairs = 0 

for pair in assignment_sections:

    sections = pair.split(',')
    elf_1 = sections[0].split('-')
    elf_2 = sections[1].split('-')

    value_contained = (int(elf_1[0]) - int(elf_2[0]))*(int(elf_1[1]) - int(elf_2[1]))
    value_overlapping = (int(elf_2[1]) - int(elf_1[0]))*(int(elf_2[0]) - int(elf_1[1]))


    if value_contained <= 0:
        fully_contained_pairs += 1

    if value_overlapping <= 0:
        overlapping_pairs += 1


print("Part 1:", fully_contained_pairs)
print("Part 2:", overlapping_pairs)

