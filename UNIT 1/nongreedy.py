def brute_force_cow_transport(cowlist, weightlimit):
    result = []
    sortedcowlist = [[a,b] for a, b in sorted(cowlist.items(), key = lambda item: item[1], reverse = True)]
    print(sortedcowlist)
    while len(sortedcowlist)>0:
        total = 0
        cargo = []
        indexestopop = []
        for i in range(len(sortedcowlist)):
            cow, weight = sortedcowlist[i]
            if weight + total <= weightlimit:
                cargo.append(cow)
                total += weight
                indexestopop.append(i)
        indexestopop.sort(reverse=True)
        print(indexestopop)
        for x in indexestopop:
            sortedcowlist.pop(x)
        result.append(cargo)
    return result

# print(greedy_cow_transport({'MooMoo': 85, 'Milkshake': 75, 'Patches': 60, 'Louis': 45, 'Horns': 50,
#                             'Miss Bella': 15, 'Lotus': 10, 'Clover': 5, 'Polaris': 20, 
#                             'Muscles': 65}, 100))

print(greedy_cow_transport({'Luna': 41, 'Willow': 59, 'Rose': 42, 'Coco': 59, 'Betsy': 39, 'Abby': 28,
                            'Starlight': 54, 'Buttercup': 11}, 120))