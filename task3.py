# 3. Прочитайте файл 'complex.txt' и построчно выведите считанные комплексные числа,
# которые по модулю больше или равны определенному числу, строку "меньше" для меньших.
# Примечание: в связи с особенностью системы DiSpace файл упакован в zip-архив.

with open('files/complex.txt') as f:
    nums = f.read()
a = []
nums = nums.split()
nums = [complex(x) for x in nums]
low = 10
for num in nums:
    if abs(num) <= low:
        print(num)
    else:
        a.append(num)
print('Строка из оставшихся элементов:', a)