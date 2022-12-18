#2. Напишите программу для. проверки истинности утверждения 
#¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

print(f'¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z')
for x in [0,1]:
    for y in [0,1]:
        for z in [0,1]:
            number1 = not (x or y or z)
            number2 = not x and not y and not z
            result = number1 = number2
            print(f'¬({x} ⋁ {y} ⋁ {z}) = ¬{x} ⋀ ¬{y} ⋀ ¬{z} -> {result}')
            
