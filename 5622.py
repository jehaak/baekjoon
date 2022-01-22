# list로 변환 후 아스키코드 처리하고 A아스키코드 값 빼서 
# //3 했을 때 값 따라 숫자 부여할 예정
word = input()
word = list(word)
word = list(map(ord, word))
word = list(map(lambda x : (x-65)//3, word))
print(word)
# 중간에 4개가 한묶음인게 있다..