from PyQt5 import QtCore
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
from matplotlib import pyplot as plt
from matplotlib.backend_bases import FigureCanvasBase
import Act_function as ACT
import pandas as pd


class Ui_MainWindow(object):
    search_si = None

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1600, 850)
        MainWindow.setCursor(QCursor(Qt.ArrowCursor))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QRect(0, 0, 220, 480))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)

        self.listView = QListView(self.verticalLayoutWidget)
        self.listView.setObjectName("listView")
        self.listView.clicked.connect(self.handle_item_selection)
        self.verticalLayout.addWidget(self.listView)

        self.verticalLayoutWidget_2 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QRect(230, 0, 420, 760))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(7)
        self.horizontalLayout.setContentsMargins(10, -1, 10, -1)
        self.lineEdit = QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setTabletTracking(True)
        self.horizontalLayout.addWidget(self.lineEdit)

        self.pushButton = QPushButton(self.verticalLayoutWidget_2)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(
            lambda: self.button_clicked(
                self.lineEdit,
                self.listView_2,
                self.label_2,
                self.label_image1,
                self.label_pi1,
            )
        )
        self.horizontalLayout.addWidget(self.pushButton)

        self.label_2 = QLabel(self.verticalLayoutWidget_2)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)

        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.listView_2 = QListView(self.verticalLayoutWidget_2)
        self.listView_2.setObjectName("listView_2")
        self.verticalLayout_2.addWidget(self.listView_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(7)
        self.horizontalLayout_4.setContentsMargins(10, -1, 10, -1)
        self.lineEdit_4 = QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_4.setTabletTracking(True)
        self.horizontalLayout_4.addWidget(self.lineEdit_4)

        self.pushButton_4 = QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(
            lambda: self.button_clicked(
                self.lineEdit_4,
                self.listView_3,
                self.label_3,
                self.label_image2,
                self.label_pi2,
            )
        )
        self.horizontalLayout_4.addWidget(self.pushButton_4)

        self.label_3 = QLabel(self.verticalLayoutWidget_2)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)

        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.listView_3 = QListView(self.verticalLayoutWidget_2)
        self.listView_3.setObjectName("listView_3")
        self.verticalLayout_2.addWidget(self.listView_3)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setGeometry(QRect(0, 0, 1309, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        MainWindow.setStatusBar(self.statusbar)

        self.label_image1 = QLabel(MainWindow)
        self.label_image1.setGeometry(QRect(660, 10, 360, 360))
        self.label_image2 = QLabel(MainWindow)
        self.label_image2.setGeometry(QRect(660, 390, 360, 360))

        self.label_pi1 = QLabel(MainWindow)
        self.label_pi1.setGeometry(QRect(1030, 10, 400, 360))

        self.label_pi2 = QLabel(MainWindow)
        self.label_pi2.setGeometry(QRect(1030, 390, 400, 360))

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", "MainWindow", None)
        )
        self.label.setText(QCoreApplication.translate("MainWindow", "검색 대상", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", "검색", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", "현재: ", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", "검색", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", "현재: ", None))
        self.insert_list()

    def handle_item_selection(self, index):
        # 선택된 아이템의 데이터 가져오기
        model = index.model()
        item = model.itemFromIndex(index)
        self.search_si = item.text()

    def insert_list(self):
        # 아이템 모델 생성
        model = QStandardItemModel()
        local = [
            "강원",
            "경기",
            "경남",
            "경북",
            "광주",
            "대구",
            "대전",
            "부산",
            "서울",
            "세종",
            "울산",
            "인천",
            "전남",
            "전북",
            "제주",
            "충남",
            "충북",
        ]
        for i in local:
            item = QStandardItem(i)
            item.setEditable(False)
            model.appendRow(item)

        self.listView.setModel(model)

    # setupUi
    def button_clicked(self, line, list_view, text, graph, pi):
        print(self.search_si)
        if self.search_si == None:
            return
        search_dong = line.text()
        graph_path = ACT.visualize_store_data(self.search_si, "dong_NM", search_dong)
        df = ACT.StoreSQL.search_store_by_region(self.search_si, "dong_NM", search_dong)
        pixmap = QPixmap(graph_path)
        graph.setPixmap(pixmap)
        graph.setScaledContents(True)

        text.setText(f"현재 : {self.search_si} {search_dong}")
        self.view_result(df, list_view, pi)

    def view_result(self, store_df, list_view, pi):
        df = pd.DataFrame(
            {
                "이름": store_df["OPEN_BIZES_NM"],
                "분류": store_df["INDS_LCLS_NM"],
                "주소": store_df["RDNM_ADR"],
            }
        )
        model = QStandardItemModel()

        for row in df.itertuples(index=False):
            name = row.이름
            category = row.분류
            add = row.주소

            item = QStandardItem(f"{name} | {category} | {add}")
            item.setEditable(False)
            model.appendRow(item)
        list_view.setModel(model)
        fig, ax = plt.subplots()

        count_by_category = df["분류"].value_counts()
        patches, texts, _ = ax.pie(
            count_by_category,
            labels=count_by_category.index,
            autopct="%1.1f%%",
            startangle=90,
        )
        ax.axis("equal")
        legend_labels = count_by_category.index
        ax.legend(patches, legend_labels, loc="center left", bbox_to_anchor=(-0.2, 0.5))

        # 그래프를 이미지 파일로 저장
        plt.savefig("pi.png")
        pixmap = QPixmap("pi.png")
        pi.setPixmap(pixmap)
        pi.setScaledContents(True)
        plt.clf()


import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

# UI 클래스 임포트
from front import Ui_MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # MainWindow 인스턴스 생성
    window = QMainWindow()

    # UI 설정을 위한 setupUi 함수 호출
    ui = Ui_MainWindow()
    ui.setupUi(window)

    # 창을 화면에 표시
    window.show()

    # 이벤트 루프 실행
    sys.exit(app.exec_())
