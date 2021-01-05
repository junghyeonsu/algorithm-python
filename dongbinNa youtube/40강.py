# 예외 처리
try:
    # 이 부분을 실행한다 그런데, 
    print(3 / 2)
except:
    # 오류가 난다면 except 구문을 실행
    print('0으로 나눌 수 없다.')
else:
    # except 구문이 처리가 안됐으면 else 구문 실행
    print('예외가 없었습니다!')
finally:
    # 에러 유무에 상관없이 실행되는 구문
    print("예외 처리 구문이 끝났습니다.")



try:
    print(3/0)
except Exception as e :
    # 오류가 일어났을 때 어떠한 오류가 났는지 알려줌
    print(e)