print('input your height [m]: ', end ='')
height = float(input())

print('input your weight [kg]: ', end ='')
weight = float(input())

bmi = weight / height ** 2
print('Your BMI is ' + str(bmi))
