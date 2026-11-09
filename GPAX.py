#เก็บคะแนนแต่ละรายวิชา
English = float(input("กรอกคะแนนวิชาภาษาอังกฤษ: "))
Math = float(input("กรอกคะแนนวิชาคณิตศาสตร์: "))
Science = float(input('กรอกคะแนนวิชาวิทยาศาสตร์:'))
Social = float(input('กรอกคะแนนวิชาภูมิศาสตร์:'))


print('--- Your Score ---')
print('English:', English)
print('Math:', Math)
print('Science:', Science)
print('Social:', Social)
print()

#คำนวณ GPAX
total_score = English + Math + Science + Social
gpax = total_score / 4

print(f'GPAX: {gpax :,.2f}')