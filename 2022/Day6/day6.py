with open('input.txt') as file:
    datastream_buffer = file.read().strip()



for i in range(len(datastream_buffer)-4):
    if len(set(datastream_buffer[i:i+4])) == 4:
        print("Part 1:", i+4)
        break

for i in range(len(datastream_buffer)-14):
    if len(set(datastream_buffer[i:i+14])) == 14:
        print("Part 2:", i+14)
        break