outdoors ={"chaitanya", "kartik" , "me"}
indoors = {"chaitanya","soumya" ,"vedansh"}
every = {"chaitanya", "vedansh", "me","roshni"}


only = outdoors-indoors -every #differecne
print(only)


both = outdoors & every #intersection
print(both)

each = outdoors|indoors |every #union
print(each)

uncommon = outdoors ^ indoors ^ every
print(uncommon)