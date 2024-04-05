first_side = int(input("İlk Kenar:"))
second_side = int(input("İkinci Kenar:"))
third_side = int(input("Üçüncü Kenar:"))

if first_side + second_side + third_side - max(first_side, second_side, third_side) <= max(first_side, second_side, third_side):
    print(first_side,second_side,third_side, "ile üçgen çizilemez!")
else:
    print(first_side,second_side,third_side, "ile üçgen çizilebilir!")
