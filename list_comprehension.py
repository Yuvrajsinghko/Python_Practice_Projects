# list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
# a=[x for row in list_of_lists for f in row for x in f]

# print(a)
# numbers = [-4, -3, -2, -1, 0, 2, 4, 6]

# ans=[i for i in numbers if i>0]
# print(ans)

# countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
# # output:
# # [['FINLAND','FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]

# simple_list=[x for i in countries for j in i for x in j]


# final_list=[]
# for g in simple_list:
# 	t=g.upper()
# 	final_list.append(t)

# sub_list=[]
# for con in range(len(final_list)):
# 	if con%2==0:
# 		a=simple_list[con]
# 		sub_str=a[0:3].upper()
# 		sub_list.append(sub_str)
		


# for sd in sub_list:
# 	for los in final_list:
		
# 		if sd in los:
# 			curr_index=final_list.index(los)
# 			final_list.insert(curr_index+1,sd)
# 			break

# answ_list=[[final_list[j] for j in range(3)] for i in range(3)]
# print(answ_list)


# countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
# output:
# [{'country': 'FINLAND', 'city': 'HELSINKI'},
# {'country': 'SWEDEN', 'city': 'STOCKHOLM'},
# {'country': 'NORWAY', 'city': 'OSLO'}]


# simplified_list=[x for i in countries for j in i for x in j]

# even_num=[k for k in range(len(simplified_list)) if k%2==0]
# odd_num=[p for p in range(len(simplified_list)) if p%2!=0]
# final_list=[{'country':simplified_list[even_num[i]],'city':simplified_list[odd_num[i]]} for i in range(len(odd_num))]
# print(final_list)

# names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
# # output
# # ['Asabeneh Yetaeyeh', 'David Smith', 'Donald Trump', 'Bill Gates']

# simplyfied_names=[x for i in names for k in i for x in k]

# even_num=[t for t in range(len(simplyfied_names)) if t%2==0]
# odd_num=[p for p in range(len(simplyfied_names)) if p%2!=0]

# final_name_list=[simplyfied_names[even_num[i]]+' '+simplyfied_names[odd_num[i]] for i in range(len(even_num))]
# print(simplyfied_names)
# print(final_name_list)

# new_list=[(i,1,i**i) for i in range(1,6) ]
# print(new_list)
