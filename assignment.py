my_list = [ ] 

#append
my_list.append (10)
my_list.append (20)
my_list.append (30)
my_list.append (40)

#insert
my_list.insert(1,15)

#extend 
my_list2 = [50,60,70]
my_list.extend(my_list2)

#remove
my_list.remove(70)

#sort
my_list.sort()

#index
print(my_list.index(30))

print(my_list)