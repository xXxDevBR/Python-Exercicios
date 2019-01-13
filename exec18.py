import math

ang = float(input("Digite o ângulo: "))

sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))

print("O seno de {} é {}".format(ang, sen))
print("O cosseno de {} é {}".format(ang, cos))
print('A tangente de {} é {}'.format(ang, tan))
