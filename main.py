import random

lower_case = 'abcdefghijklmnopqrstuvwxyz'

upper_case = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

number = '123456789'

symbols ='!@#$%^&*?\/'

size_of_pass =8

combining_randomly = lower_case+upper_case+number+symbols

passValue =''.join(random.sample(combining_randomly, size_of_pass))

print(passValue)