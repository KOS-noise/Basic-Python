# Modules to load with: from test_package import *

# __init.py 는 해당 폴더가 패키지임을 알려주고, 패키지와 관련된 초기화 처리를 하는 파일.
# __init__.py 에 __all__ 이라는 이름의 리스트를 만드는데, 이 리스트에 지정한 모듈들이 from <패키지 이름> import * 를 할 때 전부 읽어 들여집니다. 
__all__ = ["module_a", "module_b"]

print("test_package 패키지를 읽어 들였습니다.")
