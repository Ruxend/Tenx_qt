#！/usr/bin/env python3
#-*- coding:utf-8 -*-
from PyQt5.QtWidgets import (QApplication,QMainWindow,QDockWidget,QWidget,QFrame,QLabel,
						QLineEdit,QTextEdit,QPushButton,QDialog,QSlider,QMessageBox,
						QInputDialog,QFileDialog,QFontDialog,QColorDialog,QToolBar,
						QMenuBar,QStatusBar,QGroupBox,QGridLayout,QHBoxLayout,QVBoxLayout,
						QFormLayout,QListWidget,QScrollBar,QDesktopWidget,QProgressBar,
						QTextBrowser,QComboBox)
from PyQt5.QtGui import (QFont,QIcon,QPixmap,QMovie,QColor,QTextCursor,QPalette)
from PyQt5.QtCore import (Qt,QFile,QTimer,QDateTime,QThread,pyqtSignal,pyqtSlot,
						QBasicTimer,QCoreApplication)
# from PyQt5.QtMultimedia import QAudioInput,QAudioOutput,QAudioDeviceInfo
from random import randint
from res import res
# from eth import eth
# from xlwt_style import style

"""二级窗体内容"""
class ui_Tenx():
	# def __init__(self, parent=None):
	# 	super().__init__(parent)
	def setupUi(self, QMainWindow):
		self.setWindowTitle("Tool of Vip Video") 				# 设置窗口标题
		self.setWindowIcon(QIcon(res.path("res\\win.ico")))		# 设置窗口图标
		self.resize(600, 500) # 设置窗口大小
		"""窗体居中"""
		screen = QDesktopWidget().screenGeometry()				# 获取屏幕坐标系
		size = self.geometry()									# 获取窗口坐标系
		self.move(int((screen.width()-size.width())/2), int((screen.height()-size.height())/2) ) # 窗体居中显示
		# 中心QWidget####################################################
		self.master = QWidget(self)
		self.frame = QFrame(self.master)
		self.frame_grid = QGridLayout(self.master) 				# 主布局管理
		self.frame_grid.setContentsMargins(10, 0, 10, 0) 		# 布局四周留白大小(left,top,right,bottom)
		# 添加group布局组
		self.frame_grid.addWidget(self.frame_groupbox_1(), 0, 0, 1, 8) 	# 调取group布局组添加至主布局
		self.frame_grid.addWidget(self.frame_groupbox_2(), 1, 0, 1, 8) 	# 调取group布局组添加至主布局

		self.master.setLayout(self.frame_grid) 						# 显示QWidget布局
		self.setCentralWidget(self.master) 							# 将QWidget控件设为中心
		self.menubar()  											# 调取菜单栏/工具栏
		self.statusbar() 											# 调取状态栏
		self.createWidget()  										# 调取中心QWidget窗体控件
		# self.dock_Widget() 										# 调取中心Dock窗体控件

	def frame_groupbox_1(self):
		self.frame_groupbox_1 = QGroupBox(self.frame) 				# 布局组
		self.frame_groupbox_1.setObjectName("groupbox_1")
		self.frame_groupbox_1.setFont(QFont("Arial Narrow", 9, QFont.Normal))
		self.frame_groupbox_1.setTitle("Input area") 				# 设置group组标题
		self.frame_groupbox_1.setAlignment(Qt.AlignLeft)			# 设置group组标题对齐方式
		self.frame_groupbox_1.setFlat(True) 						# group组默认边框_去除(True)/显示(False)
		# self.frame_groupbox_1.setCheckable(True)					# group可选状态_可选(True)/不可选(False)
		# self.frame_groupbox_1.setChecked(False) 					# group默认状态_选中(True)/不勾选(False)
		self.groupbox_1_grid_1 = QGridLayout(self.frame_groupbox_1) # group布局组内布局方式
		self.groupbox_1_grid_1.setObjectName("grid_1")
		self.groupbox_1_grid_1.setContentsMargins(10, 10, 10, 10) 	# 布局四周留白大小(left,top,right,bottom)
		self.groupbox_1_grid_1.setSpacing(5) 						# 控件之间的间距
		self.frame_groupbox_1.setLayout(self.groupbox_1_grid_1) 	# 将子布局添加至group组
		return self.frame_groupbox_1

	def frame_groupbox_2(self):
		self.frame_groupbox_2 = QGroupBox(self.frame) 				# 布局组
		self.frame_groupbox_2.setObjectName("groupbox_2")
		self.frame_groupbox_2.setFont(QFont("Arial Narrow", 9, QFont.Normal))
		self.frame_groupbox_2.setTitle("Output area") 				# 设置group组标题
		self.frame_groupbox_2.setAlignment(Qt.AlignLeft)			# 设置group组标题对齐方式
		self.frame_groupbox_2.setFlat(True) 						# group组默认边框_去除(True)/显示(False)
		# self.frame_groupbox_2.setCheckable(True)					# group可选状态_可选(True)/不可选(False)
		# self.frame_groupbox_2.setChecked(False) 					# group默认状态_选中(True)/不勾选(False)
		self.groupbox_2_grid_1 = QGridLayout(self.frame_groupbox_2) # group布局组内布局方式
		self.groupbox_2_grid_1.setObjectName("grid_2")
		self.groupbox_2_grid_1.setContentsMargins(10, 10, 10, 10) 	# 布局四周留白大小(left,top,right,bottom)
		self.groupbox_2_grid_1.setSpacing(5) 						# 控件之间的间距
		self.frame_groupbox_2.setLayout(self.groupbox_2_grid_1) 	# 将子布局添加至group组
		return self.frame_groupbox_2

	def dock_Widget(self):
		self.Dock = QDockWidget("Dockable", self)
		self.Dock.setObjectName("dock")
		self.dock_grid = QListWidget()							# 布局
		self.dock_grid.addItem('Item1')
		self.dock_grid.addItem('Item2')
		self.dock_grid.addItem('Item3')
		self.dock_grid.addItem('Item3')
		self.Dock.setWidget(self.dock_grid) 					# 添加布局
		self.Dock.setFloating(False) 							# 浮动状态_窗口外(True)/窗口内(False)
		self.addDockWidget(Qt.LeftDockWidgetArea, self.Dock) 	# 添加Dock控件

	"""
	菜单栏/状态栏/工具栏
	"""
	def menubar(self):
		"""菜单栏"""
		self.menubar = self.menuBar()
		# 一级菜单
		self.file = self.menubar.addMenu("File(&F)")
		self.help = self.menubar.addMenu("Help(&H)")
		# 二级菜单
		# file_open = self.file.addAction("Open(&O)")
		# file_open.triggered.connect(self.file_open)		# 动作与槽连接
		self.file.addSeparator()
		file_quit = self.file.addAction("Exit(&E)")
		file_quit.triggered.connect(self.close) 		# 动作与槽连接

		self.file.addSeparator()
		help_about = self.help.addAction("About(&A)")
		help_about.triggered.connect(self.help_about)
		# # 工具栏
		# self.toolbar_file = self.addToolBar("文件")
		# self.toolbar_file.setMovable(False) 			# 在工具栏的位置_可移动(True)/固定(False)
		# self.toolbar_file.addAction(file_open)
		# self.toolbar_file.addSeparator()
		# self.toolbar_file.addAction(file_quit)

	def statusbar(self):  	# 状态栏
		self.statusbar = QStatusBar(self)
		self.statusbar.setObjectName("statusbar")
		self.timer = QTimer()  								# 当前时间计时器
		self.timer.start()
		self.timer.timeout.connect(self.showtime)  			# 超时设定
		self.statusbar_label_time = QLabel()
		self.statusbar_label_progressbar = QLabel()
		self.progressbar = QProgressBar(self.statusbar)  	# Progressbar
		self.progressbar.setObjectName("progressbar")
		self.progressbar.setValue(0)  						# 设置进度条的初始值
		self.progressbar.setInvertedAppearance(False) 		# True进度条从左到右(水平进度条)/从上到下(垂直进度条)
		self.basictimer = QBasicTimer()  					# 进度条计时器
		self.step = 0
		self.progressbar.hide() 							# 设置初始状态
		self.setStatusBar(self.statusbar)
		self.statusbar.addPermanentWidget(self.statusbar_label_time)
		self.statusbar.addPermanentWidget(self.progressbar)

	def help_about(self):
		self.about = QMessageBox(self)
		self.about.setWindowTitle("About")
		self.about.setWindowIcon(QIcon(res.path("res\\win.ico")))
		self.about.setText(f"{res.author}\n\n{res.myappid}   ")
		self.about.setStandardButtons(QMessageBox.Ok)
		self.about.button(QMessageBox.Ok).setText("确定")
		self.about.exec()
		# QMessageBox.about(self, "About", "Version 1.0.0")

	def showtime(self):
		time = QDateTime.currentDateTime()
		timeDisplay = time.toString("yyyy/MM/dd hh:mm:ss ddd")
		self.statusbar_label_time.setText(timeDisplay)
		# self.statusbar.showMessage(timeDisplay)

	def createWidget(self):
		_translate = QCoreApplication.translate
		"""控件内容"""
		conText = (("请输入视频链接:", "entry_1"),
					("选择通道:", "combo_1"))
		for self.index, self.r in enumerate(conText):
			for self.cindex, self.c in enumerate(self.r):
				if self.c == "请输入视频链接:":
					self.label_1 = QLabel()
					self.label_1.setObjectName("label_1")
					self.label_1.setText(_translate("self", self.c))
					self.label_1.setFont(QFont("微软雅黑", 9, QFont.Normal))
					self.groupbox_1_grid_1.addWidget(self.label_1, self.index, self.cindex, 1, 1)
				elif self.c == "entry_1":
					self.entry_1 = QLineEdit()
					self.entry_1.setObjectName("entry_1")
					self.entry_1.setFont(QFont("微软雅黑", 9, QFont.Normal))
					self.entry_1.setPlaceholderText("Please input here(Must be selected)") 	# 设置浮显文字
					self.entry_1.setAlignment(Qt.AlignLeft)
					self.label_1.setBuddy(self.entry_1) 							# 伙伴关系
					self.groupbox_1_grid_1.addWidget(self.entry_1, self.index, self.cindex, 1, 6)
				if self.c == "选择通道:":
					self.label_2 = QLabel()
					self.label_2.setObjectName("label_2")
					self.label_2.setText(_translate("self", self.c))
					self.label_2.setFont(QFont("微软雅黑", 9, QFont.Normal))
					self.groupbox_1_grid_1.addWidget(self.label_2, self.index, self.cindex, 1, 1)
				elif self.c == "combo_1":
					self.combo_1 = QComboBox()
					self.combo_1.setObjectName("combo_1")
					self.combo_1.setCurrentIndex(0)    # 设置默认显示的值，不设置则默认为0
					self.groupbox_1_grid_1.addWidget(self.combo_1, self.index, self.cindex, 1, 2)

		# "text"
		self.text = QTextBrowser()#QTextEdit()
		self.text.setObjectName("text")
		self.text.verticalScrollBar().setValue(self.text.verticalScrollBar().maximum()) # 滚动条最大值关联文本
		self.text.setFont(QFont("微软雅黑", 9, QFont.Normal))
		self.groupbox_2_grid_1.addWidget(self.text, 0, 0, 1, 8)
		# "Confirm"
		self.btn_confirm = QPushButton()
		self.btn_confirm.setObjectName("btn_confirm")
		self.btn_confirm.setText(_translate("self", "Confirm(&C)"))
		self.btn_confirm.setToolTip("Running")
		# self.btn_confirm.setAutoRepeat()
		self.btn_confirm.setFont(QFont("微软雅黑", 9, QFont.Normal))
		self.btn_confirm.setStyleSheet("QPushButton:hover{background-color:limegreen}")
		self.frame_grid.addWidget(self.btn_confirm, 3, 3, 1, 1)
		# "Quit"
		self.btn_quit = QPushButton()
		self.btn_quit.setObjectName("btn_quit")
		self.btn_quit.setText(_translate("self", "Quit(&Q)"))
		self.btn_quit.setToolTip("Quit")
		self.btn_quit.setFont(QFont("微软雅黑", 9, QFont.Normal))
		self.btn_quit.setStyleSheet("QPushButton:hover{background-color:orangered}")
		self.frame_grid.addWidget(self.btn_quit, 3, 4, 1, 1)



# ui_Tenx()