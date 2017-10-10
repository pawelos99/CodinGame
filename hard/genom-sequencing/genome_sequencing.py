# get input
n = int(input())
sequence = [input() for _ in range(n)]

# select starting genome
start_genome = max(sequence, key=lambda x: len(x))
result_genome = start_genome

# loop over other genomes searching for best match
for genome in sequence:
    if genome == start_genome:
        continue
    if genome in result_genome:
        continue

    # loop over all possibilities of genom in front of result_genom
    front = 0
    for y in range(1, len(genome)):
        temp = genome[-y:]
        if result_genome.startswith(temp):
            front = y

    # loop over all possibilities of genom at the end of result_genom
    end = 0
    for y in range(1, len(genome)):
        temp = genome[:y]
        if result_genome.endswith(temp):
            end = y

    # select the best possibility from front and end
    if front > end:
        result_genome = genome[:-front] + result_genome
    else:
        result_genome = result_genome + genome[end:]

print(len(result_genome))
