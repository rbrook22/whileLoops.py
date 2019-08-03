#Creating my first while loop

num_family=10
family_age_sum=185

while num_family > 0:
    print("I have %s family members living in Atlanta" %num_family)
    num_family-= 1
else: 
    print("Everyone else moved away except for %s family member" %num_family)

#incorporating a break statement
while family_age_sum < 200:
    print("Family aged summed is %s "%family_age_sum)
    family_age_sum+= 1
    if family_age_sum == 190:
        break
