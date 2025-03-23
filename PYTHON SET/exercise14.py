"""The intersection_update() method will also keep ONLY the duplicates, 
but it will change the original set instead of returning a new set."""

set1 = {"Google","Microsoft","Duckchain","Apple"}
set2 = {"Duckchain"}
set1.intersection_update(set2)
print(set1)

set1 = {"apple", 1,  "banana", 0, "cherry"}
set2 = {False, "google", 1, "apple", 2, True}

set3 = set1.intersection(set2)

print(set3)