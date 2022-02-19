import sys

equation = sys.argv[1].strip()
print(equation)
if equation.find('<') != -1:
    sign = 'L' # less than
else: sign = 'G' # greater than
if '=' in equation: radius = float(equation[9:])
else: radius = float(equation[8:])
print(radius)

divNum = 1/(radius**.5)

weights = [[3.0433*divNum, -1.7874*divNum, -2.0136,
            -0.1642*divNum, -3.5452*divNum, 1.9793,
            0.1655*divNum,  6.8517*divNum, -5.2608,
            -3.1045*divNum, -1.5895*divNum, -1.9144],
           [8.8160,  -7.0506,   1.5918,   8.8067, -26.2797,
            8.5657, -10.2592, -28.1814, -17.2571,  14.6948,
            -2.3127, -17.2769], [-20.3747, -17.4696,  29.7105],
           [1.0028]]

print('layer cts: [3, 4, 3, 1, 1]')
for layer in weights:
    print(layer)
