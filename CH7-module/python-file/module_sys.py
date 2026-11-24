import sys

# 명령 매개변수를 출력한다

print(sys.argv)
print("------")


# 컴퓨터 환경과 관련된 정보를 출력한다 
print("getwindowsversion:()", sys.getwindowsversion())
print("---")
print("copyright:", sys.copyright)
print("---")
print("version:", sys.version)

# 프로그램 강제종료
sys.exit()


# powershell 또는 cmd로 이 파일을 실행시켜볼까요 
# >> python module_sys.py 10 20 30