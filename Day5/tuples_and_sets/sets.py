#unordered
# mutalble
# does not allow duplicates
# no indexing

empty_set=set()
fruits={"apple","banana","cherry"}
print("empty set: ",empty_set)
print("set of fruits",fruits)

nums={1,2,3}
nums.add(4)
nums.remove(2)

set1={1,2,3,4,5}
set2={2,3,7,8}
print("union: ", set1 | set2)
print("intersection: ", set1.intersection(set2))

