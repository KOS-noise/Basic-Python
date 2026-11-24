import os

print("현재 운영체제: ",os.name)
print("현재 폴더: ", os.getcwd())
print("현재 폴더의 내부 요소: ", os.listdir())

# 폴더를 만들고 제거한다. (폴더가 비어있을 때만 제거 가능)
os.mkdir("hello")
os.rmdir("hello")



os.system("dir")

