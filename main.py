# json import
# json을 사용하려면 node.js와 다르게 import가 필요
import json

# 예제를 위한 임의의 json 파일 경로
file_path = 'data/data.json'

# 함수 작성해보기
def update_function(data):
    # 내용
    return

def delete_function(data):
    # 내용
    return

def create_json(data):
    # open 함수는 파일을 열 때 쓴다. 첫번째 인자로는 '파일의 경로'를, 두번째 인자로는 '모드'를 지정한다.
    # 'w'는 write의 줄임말로, 보통 '모드'라고 불리며, 'w'는 파일을 쓰기 위해 연다.(없으면 새로 생성)
    with open(file_path, 'w') as file:
        # json.dump 메서드는 Python 데이터를 JSON 형식의 문자열로 변환해 파일에 쓴다.
        # 여기서는 data 변수의 내용을 JSON 형태로 파일에 저장한다.
        json.dump(data, file, indent=4)
