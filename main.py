# main.py

# json import
# json을 사용하려면 node.js와 다르게 import가 필요
import json

# 예제를 위한 JSON 파일 경로를 변수 선언
file_path = 'data/data.json'

# 함수 작성해보기
def update_function(data):
    data.clear()
    data.update({"os": "Windows"})

def delete_function(data):
    data.clear()


# JSON 생성 함수
def create_json(data):
    # open 함수는 파일을 열 때 쓴다. 첫번째 인자로는 '파일의 경로'를, 두번째 인자로는 '모드'를 지정한다.
    # 'w'는 write의 줄임말로, 보통 '모드'라고 불리며, 'w'는 파일을 쓰기 위해 연다.(없으면 새로 생성)
    with open(file_path, 'w') as file:
        # json.dump 메서드는 Python 데이터를 JSON 형식의 문자열로 변환해 파일에 쓴다.
        # 여기서는 data 변수의 내용을 JSON 형태로 파일에 저장한다.
        json.dump(data, file, indent=4)

# JSON에 추가할 데이터 변수 선언
data_to_write = {"name": "BHN", "birth": 1997, "age": 26, "city": "Daejeon"}

# create_json 함수 호출 및 데이터 추가
create_json(data_to_write)

# JSON 읽기 함수
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
    
# read_json 함수 호출 및 JSON 데이터 읽기
json_data = read_json()

# JSON 데이터가 None이 아닌 경우
if json_data is not None:
    # JSON 데이터 출력
    print(json_data) # {'name': 'BHN', 'birth': 1997, 'age': 26, 'city': 'Daejeon'}
else: 
    # 파일이 존재하지 않는 경우
    print("파일이 없음")

# JSON 업데이트 함수
def update_json(update_function):
    try: 
        # 'r+' 모드는 읽기와 쓰기를 모두 할 수 있는 모드로, 권한이 많기 때문에 남용하면 위험하다.
        with open(file_path, 'r+') as file:
            data = json.load(file) # 파일의 내용을 읽어서, Python 데이터 타입으로 변환
            
            update_function(data) # 인자로 받은 업데이트 함수를 호출해 data를 업데이트
            # Python도 JavaScript와 동일하게 인터프리터이기에 seek, truncate처럼 위에서 아래로 순차적으로 읽는 특징을 활용한다.
            # 데이터를 읽어내는 위치도 조절할 수 있다.
            file.seek(0) # 파일의 처음으로 커서를 이동. 파일을 새로운 내용으로 '덮어쓰기'
            json.dump(data, file, indent=4) # 수정된 data를 다시 JSON 형태로 파일에 쓴다.
            file.truncate() # 파일의 현재 위치 이후의 내용을 삭제한다. "이전 파일을 삭제할까요?"의 느낌
    except FileNotFoundError:
        print("파일을 찾지 못함")
        create_json({}) # 파일이 없을 경우 새로운 파일을 생성 // 상당히 절차적인 모습이다.

# update_json 함수 호출 및 데이터 업데이트
update_json(update_function)

# JSON 삭제 함수
def delete_json(delete_function):
    try:
        with open(file_path, 'r+') as file:
            data =json.load(file) # 파일 내용을 Python 데이터 타입으로 변환
            delete_function(data)
            file.seek(0) # 파일의 처음으로 커서를 이동
            json.dump(data, file, indent=4) # 수정된 data를 다시 JSON 형태로 파일에 작성
            file.truncate() # 파일의 현재 위치 이후의 내용을 삭제
    except FileNotFoundError:
        print("파일을 찾지 못함")

# delete_json 함수 호출 및 데이터 삭제
delete_json(delete_function)


# __name__: 현재의 모듈
# __main__: 실행되는 스크립트 파일
if __name__ == "__main__":
    {
        "items": [

        ]
    }
    create_data = {"items": []}
    create_json(create_data) # JSON 파일 생성 및 데이터 쓰기

    # Update 예제: 새 아이템 추가
    def add_item(data):
        data["items"].append({"name": "BHN", "ID": "bhn1997", "Gmail": "dev.honing@gmail.com"})
    update_json(add_item) # JSON 파일 업데이트

    # Read 예제
    print(read_json()) # JSON 파일 읽기

    # Delete 예제: 아이템 삭제
    def remove_item(data):
        # 아래의 for in문을 JavaScript 방식으로 바꾸어 설명하면,
        # for (let item of data.items) {
        #     if (item.name === "BHN") {
        #         data.items.splice(data.items.indexOf(item), 1);
        #         break;
        #     }
        # }
        # 이며, Python의 반복문은 for in 문법을 사용하고, 다른 방식의 반복문을 사용하지 않는다.
        # JavaScript는 for in 문법을 지원하지만 잘 사용하지 않는데, Python은 주로 for in 문법을 사용한다.
        # Python은 반복문의 종류가 for in, while로 두 가지 뿐이다.
        # 반복문이 일관되어 '가독성'이 좋지만, JavaScript의 풍부한 반복문 지원보다는 편의성 면에서 떨어진다.

        data["items"] = [item for item in data["items"] if item["name"] != "BHN"]

    delete_json(remove_item) # JSON 파일 삭제

    # 변경된 데이터 확인
    print(read_json()) #JSON 파일 읽기
