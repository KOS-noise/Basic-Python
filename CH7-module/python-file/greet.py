# 이 셀을 실행하면 greet.py 파일이 만들어진다. 
import sys

script_name = sys.argv[0]
name = sys.argv[1]
age = int(sys.argv[2])

print(script_name)
print(f"Hello, {name}. Next year you will be {age + 1}.")
