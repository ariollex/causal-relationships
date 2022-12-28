def intersection_of_classes(formatcauses, userchoise, info):
    for i in range(len(formatcauses)):
        if formatcauses[userchoise][1] == formatcauses[i][1] and userchoise != i:
            info.append(['Случай связан с', formatcauses[i][1], 'классом'])
            break