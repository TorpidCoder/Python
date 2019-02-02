Sample_list = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]

#print(sorted(Sample_list))

new_Sample_list = []

for vals in Sample_list:
    if(vals not in new_Sample_list):
        new_Sample_list.append(vals)



print(new_Sample_list)
