# 모듈 : 미리 정의된 함수 코드를 모아 놓은 파이썬 파일
import math

print(math.pow(3,8)) # 제곱
print(math.sqrt(64)) # 제곱근
print(math.gcd(72, 24)) # 최대공약수


# 이렇게 함수를 만들고 같은 프로젝트 폴더안에 있으면 import해서 쓸 수 있따.
# 모듈 파일
'''
def add(a, b):
    return a + b
'''

# 모듈을 사용할 파일
'''
import 파일이름
print(파일이름.add(3,5))
'''