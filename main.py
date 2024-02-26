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

def read_json():
    try:
        # 'r' 모드는 파일을 읽기 위해 쓴다.
        # Node.js에서는 readFile(), readFileSync() 메서드를 사용하지만, '모드' 방식 덕분에 open() 메서드로 통일해 사용할 수 있다.
        # with as 문법을 사용하면, 파일을 열고 닫는 것을 자동으로 처리할 수 있다.
        # '연다'와 '닫는다'를 명시적으로 사용하는 것이 Python의 장점 중 하나이다.
        with open(file_path, 'r') as file:
            # json.load() 메서드는 파일의 내용을 JSON으로 파싱하여 Python 데이터 타입으로 변환한다.
            return json.load(file)
    except FileNotFoundError:
        # except는 예외가 발생했을 때 사용하는 JavaScript의 try-catch와 비슷한 문법이다.
        # None 데이터 타입은 JavaScript의 null과 비슷하다.
        return None
    


# json에 추가할 데이터 변수 선언
data_to_write = {"name": "BHN", "birth": 1997, "age": 26, "city": "Daejeon"}

# create_json 함수 호출 및 데이터 추가
create_json(data_to_write)