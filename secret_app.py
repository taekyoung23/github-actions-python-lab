import os

secret_value = os.getenv("SECRET_MESSAGE")

if secret_value:
    print("SECRET_MESSAGE 값 읽기 성공")
else:
    print("SECRET_MESSAGE 값 없음")