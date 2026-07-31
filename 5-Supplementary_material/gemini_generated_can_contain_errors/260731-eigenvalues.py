import math

lambda_plus = (1+math.sqrt(5))/2
lambda_minus = (1-math.sqrt(5))/2

print(f'lambda_plus={lambda_plus}, lambda_minus={lambda_minus}')

print(lambda_plus**4/math.sqrt(5) - lambda_minus**4/math.sqrt(5))
print(lambda_plus**5/math.sqrt(5) - lambda_minus**5/math.sqrt(5))
print(lambda_plus**6/math.sqrt(5) - lambda_minus**6/math.sqrt(5))
print(lambda_plus**18/math.sqrt(5) - lambda_minus**18/math.sqrt(5))
print(lambda_plus**91/math.sqrt(5) - lambda_minus**91/math.sqrt(5))

