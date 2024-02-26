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
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)
