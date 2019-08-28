blue_eyes = {"Olivia","Lili","Hali","Jack","Amilia"}
blonde_hair = {"Hali", "Jack", "Amilia", "Mia", "Joshua"}
smell_hcm = {"Hali","Amilia"}
test_ptc = {"Hali", "Lili", "Amilia", "Lora"}
O_blood = {"Mia","Joshua","Lili","Olivia"}
b_blood = {"Amilia","Jack"}
a_blood = {"Hali"}
ab_blood = {"Joshua", "Lora"}

print(blue_eyes.union(blonde_hair))

print(blonde_hair.intersection(blue_eyes))

print(blonde_hair.difference(blue_eyes))

print(blonde_hair.symmetric_difference(blue_eyes))

print(smell_hcm.issubset(blonde_hair))

print(test_ptc.issuperset(smell_hcm))

print(a_blood.isdisjoint(O_blood))