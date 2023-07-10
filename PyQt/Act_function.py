# act_function.py
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import StoreSQL


def visualize_store_data(region_name, region_level, search_area):
    df = StoreSQL.search_store_by_region(region_name, region_level, search_area)

    if df is None:
        print("해당 지역의 데이터가 없습니다.")
        return

    # 한글 폰트 설정
    if plt.rcParams["font.family"] != "Malgun Gothic":
        plt.rcParams["font.family"] = "Malgun Gothic"

    count_by_category = df["INDS_LCLS_NM"].value_counts()

    plt.figure()
    count_by_category.plot(kind="bar")
    plt.xlabel("업종 대분류")
    plt.ylabel("상점 수")
    plt.title("지역별 상점 수")
    plt.savefig("graph.png")  # 그래프를 이미지 파일로 저장

    return "graph.png"  # 이미지 파일명 반환

    # fig, ax = plt.subplots()

    #     count_by_category = df["분류"].value_counts()
    #     patches, texts, _ = ax.pie(
    #         count_by_category,
    #         labels=count_by_category.index,
    #         autopct="%1.1f%%",
    #         startangle=90,
    #     )
    #     ax.axis("equal")
    #     legend_labels = count_by_category.index
    #     ax.legend(patches, legend_labels, loc="center left", bbox_to_anchor=(-0.2, 0.5))

    #     # 그래프를 이미지 파일로 저장
    #     plt.savefig("pi.png")
    #     pixmap = QPixmap("pi.png")
