import StoreSQL
import Act_function

# 함수 호출 예시
busan_df = StoreSQL.search_store_by_region("부산", "dong_NM", "반여2동")
gangwon_df = StoreSQL.search_store_by_region("강원", "dong_NM", "무실동")

print(busan_df)
print(gangwon_df)

# 기능 구현 - 배우리
view_plot_chart = Act_function.visualize_store_data("부산", "dong_NM", "반여2동")

print(view_plot_chart)
