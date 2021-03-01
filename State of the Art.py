proposals = []
artnum = 0
while artnum < 3:
    name = input("Magazine name: ")
    if 'art' in name.lower():
        proposals.append(name)
        artnum += 1
print("Proposals:", ', '.join(sorted(proposals, reverse=True)))