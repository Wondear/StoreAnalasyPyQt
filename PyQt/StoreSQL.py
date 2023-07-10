import mysql.connector
import pandas as pd


def search_store_by_region(region_name, region_level, search_area):
    # MySQL 데이터베이스에 연결
    cnx = mysql.connector.connect(
        user="store_reader",
        password="store4567",
        host="13.125.233.228",
        database="Store_Schema",
    )

    # 커서 생성
    cursor = cnx.cursor()

    korean_to_table_name = {
        "강원": "Store_Gangwon",
        "경기": "Store_Gyeonggi",
        "경남": "Store_Gyeongnam",
        "경북": "Store_Gyeongbuk",
        "광주": "Store_Gwangju",
        "대구": "Store_Daegu",
        "대전": "Store_Daejeon",
        "부산": "Store_Busan",
        "서울": "Store_Seoul",
        "세종": "Store_Sejong",
        "울산": "Store_Ulsan",
        "인천": "Store_Incheon",
        "전남": "Store_Jeonnam",
        "전북": "Store_Jeonbuk",
        "제주": "Store_Jeju",
        "충남": "Store_Chungnam",
        "충북": "Store_Chungbuk",
    }
    region = {
        "si": "*",
        "gu_NM": "SIGUNGU_NM",
        "gu_CD": "SIGUNGU_CD",
        "dong_NM": "ADONG_NM",
        "dong_CD": "ADONG_CD",
    }

    def generate_query(table_name, region_level, search_area):
        query = f"SELECT * FROM `{table_name}` WHERE {region_level} = '{search_area}'"
        return query

    # 테이블 이름 구하기
    table_name = korean_to_table_name.get(region_name)
    region_level = region.get(region_level)

    if table_name is None:
        print("해당 지역의 데이터가 없습니다.")
        return

    # 쿼리 생성
    query = generate_query(table_name, region_level, search_area)

    # 쿼리 실행
    cursor.execute(query)

    # 결과 가져오기
    result = cursor.fetchall()

    # 컬럼 이름 가져오기
    columns = [desc[0] for desc in cursor.description]

    # DataFrame으로 변환
    df = pd.DataFrame(result, columns=columns)

    # 결과 출력
    print(df)

    # 커서와 연결 닫기
    cursor.close()
    cnx.close()

    return df
