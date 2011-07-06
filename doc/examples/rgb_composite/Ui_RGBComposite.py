# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rgb_composite.ui'
#
# Created: Fri Jun 24 10:42:15 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_RGBComposite(object):
    def setupUi(self, RGBComposite):
        RGBComposite.setObjectName(_fromUtf8("RGBComposite"))
        RGBComposite.resize(1031, 894)
        self.centralwidget = QtGui.QWidget(RGBComposite)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(-1, -1, 1031, 848))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.outerContainer = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.outerContainer.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.outerContainer.setMargin(0)
        self.outerContainer.setMargin(0)
        self.outerContainer.setObjectName(_fromUtf8("outerContainer"))
        self.previewImageContainer = QtGui.QHBoxLayout()
        self.previewImageContainer.setContentsMargins(-1, 10, -1, -1)
        self.previewImageContainer.setObjectName(_fromUtf8("previewImageContainer"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.previewImageContainer.addItem(spacerItem)
        self.compositePreview = QtGui.QGraphicsView(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.compositePreview.sizePolicy().hasHeightForWidth())
        self.compositePreview.setSizePolicy(sizePolicy)
        self.compositePreview.setMinimumSize(QtCore.QSize(512, 512))
        self.compositePreview.setMaximumSize(QtCore.QSize(512, 512))
        self.compositePreview.setObjectName(_fromUtf8("compositePreview"))
        self.previewImageContainer.addWidget(self.compositePreview)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.previewImageContainer.addItem(spacerItem1)
        self.outerContainer.addLayout(self.previewImageContainer)
        self.dateForm = QtGui.QHBoxLayout()
        self.dateForm.setContentsMargins(10, -1, 10, -1)
        self.dateForm.setObjectName(_fromUtf8("dateForm"))
        self.label = QtGui.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.dateForm.addWidget(self.label)
        self.dateTimeEdit = QtGui.QDateTimeEdit(self.verticalLayoutWidget)
        self.dateTimeEdit.setCalendarPopup(True)
        self.dateTimeEdit.setObjectName(_fromUtf8("dateTimeEdit"))
        self.dateForm.addWidget(self.dateTimeEdit)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.dateForm.addItem(spacerItem2)
        self.outerContainer.addLayout(self.dateForm)
        self.wavelengthForm = QtGui.QHBoxLayout()
        self.wavelengthForm.setMargin(10)
        self.wavelengthForm.setObjectName(_fromUtf8("wavelengthForm"))
        self.redContainer = QtGui.QVBoxLayout()
        self.redContainer.setObjectName(_fromUtf8("redContainer"))
        self.redLabel = QtGui.QLabel(self.verticalLayoutWidget)
        self.redLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.redLabel.setObjectName(_fromUtf8("redLabel"))
        self.redContainer.addWidget(self.redLabel)
        self.redPreview = QtGui.QHBoxLayout()
        self.redPreview.setObjectName(_fromUtf8("redPreview"))
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.redPreview.addItem(spacerItem3)
        self.redPreviewImage = QtGui.QGraphicsView(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.redPreviewImage.sizePolicy().hasHeightForWidth())
        self.redPreviewImage.setSizePolicy(sizePolicy)
        self.redPreviewImage.setMaximumSize(QtCore.QSize(128, 128))
        self.redPreviewImage.setObjectName(_fromUtf8("redPreviewImage"))
        self.redPreview.addWidget(self.redPreviewImage)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.redPreview.addItem(spacerItem4)
        self.redContainer.addLayout(self.redPreview)
        self.redWavelength = QtGui.QHBoxLayout()
        self.redWavelength.setObjectName(_fromUtf8("redWavelength"))
        self.redWavelengthLabel = QtGui.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.redWavelengthLabel.sizePolicy().hasHeightForWidth())
        self.redWavelengthLabel.setSizePolicy(sizePolicy)
        self.redWavelengthLabel.setMinimumSize(QtCore.QSize(90, 0))
        self.redWavelengthLabel.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.redWavelengthLabel.setObjectName(_fromUtf8("redWavelengthLabel"))
        self.redWavelength.addWidget(self.redWavelengthLabel)
        self.redWavelengthSelect = QtGui.QComboBox(self.verticalLayoutWidget)
        self.redWavelengthSelect.setObjectName(_fromUtf8("redWavelengthSelect"))
        self.redWavelength.addWidget(self.redWavelengthSelect)
        self.redContainer.addLayout(self.redWavelength)
        self.redWeight = QtGui.QHBoxLayout()
        self.redWeight.setObjectName(_fromUtf8("redWeight"))
        self.redWeightLabel = QtGui.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.redWeightLabel.sizePolicy().hasHeightForWidth())
        self.redWeightLabel.setSizePolicy(sizePolicy)
        self.redWeightLabel.setMinimumSize(QtCore.QSize(90, 0))
        self.redWeightLabel.setObjectName(_fromUtf8("redWeightLabel"))
        self.redWeight.addWidget(self.redWeightLabel)
        self.redWeightSlider = QtGui.QSlider(self.verticalLayoutWidget)
        self.redWeightSlider.setOrientation(QtCore.Qt.Horizontal)
        self.redWeightSlider.setObjectName(_fromUtf8("redWeightSlider"))
        self.redWeight.addWidget(self.redWeightSlider)
        self.redContainer.addLayout(self.redWeight)
        self.wavelengthForm.addLayout(self.redContainer)
        self.greenContainer = QtGui.QVBoxLayout()
        self.greenContainer.setObjectName(_fromUtf8("greenContainer"))
        self.greenLabel = QtGui.QLabel(self.verticalLayoutWidget)
        self.greenLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.greenLabel.setObjectName(_fromUtf8("greenLabel"))
        self.greenContainer.addWidget(self.greenLabel)
        self.greenPreview = QtGui.QHBoxLayout()
        self.greenPreview.setObjectName(_fromUtf8("greenPreview"))
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.greenPreview.addItem(spacerItem5)
        self.greenPreviewImage = QtGui.QGraphicsView(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.greenPreviewImage.sizePolicy().hasHeightForWidth())
        self.greenPreviewImage.setSizePolicy(sizePolicy)
        self.greenPreviewImage.setMaximumSize(QtCore.QSize(128, 128))
        self.greenPreviewImage.setObjectName(_fromUtf8("greenPreviewImage"))
        self.greenPreview.addWidget(self.greenPreviewImage)
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.greenPreview.addItem(spacerItem6)
        self.greenContainer.addLayout(self.greenPreview)
        self.greenWavelength = QtGui.QHBoxLayout()
        self.greenWavelength.setObjectName(_fromUtf8("greenWavelength"))
        self.greenWavelengthLabel = QtGui.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.greenWavelengthLabel.sizePolicy().hasHeightForWidth())
        self.greenWavelengthLabel.setSizePolicy(sizePolicy)
        self.greenWavelengthLabel.setMinimumSize(QtCore.QSize(90, 0))
        self.greenWavelengthLabel.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.greenWavelengthLabel.setObjectName(_fromUtf8("greenWavelengthLabel"))
        self.greenWavelength.addWidget(self.greenWavelengthLabel)
        self.greenWavelengthSelect = QtGui.QComboBox(self.verticalLayoutWidget)
        self.greenWavelengthSelect.setObjectName(_fromUtf8("greenWavelengthSelect"))
        self.greenWavelength.addWidget(self.greenWavelengthSelect)
        self.greenContainer.addLayout(self.greenWavelength)
        self.greenWeight = QtGui.QHBoxLayout()
        self.greenWeight.setObjectName(_fromUtf8("greenWeight"))
        self.greenWeightLabel = QtGui.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.greenWeightLabel.sizePolicy().hasHeightForWidth())
        self.greenWeightLabel.setSizePolicy(sizePolicy)
        self.greenWeightLabel.setMinimumSize(QtCore.QSize(90, 0))
        self.greenWeightLabel.setObjectName(_fromUtf8("greenWeightLabel"))
        self.greenWeight.addWidget(self.greenWeightLabel)
        self.greenWeightSlider = QtGui.QSlider(self.verticalLayoutWidget)
        self.greenWeightSlider.setOrientation(QtCore.Qt.Horizontal)
        self.greenWeightSlider.setObjectName(_fromUtf8("greenWeightSlider"))
        self.greenWeight.addWidget(self.greenWeightSlider)
        self.greenContainer.addLayout(self.greenWeight)
        self.wavelengthForm.addLayout(self.greenContainer)
        self.blueContainer = QtGui.QVBoxLayout()
        self.blueContainer.setObjectName(_fromUtf8("blueContainer"))
        self.blueLabel = QtGui.QLabel(self.verticalLayoutWidget)
        self.blueLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.blueLabel.setObjectName(_fromUtf8("blueLabel"))
        self.blueContainer.addWidget(self.blueLabel)
        self.bluePreview = QtGui.QHBoxLayout()
        self.bluePreview.setObjectName(_fromUtf8("bluePreview"))
        spacerItem7 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.bluePreview.addItem(spacerItem7)
        self.bluePreviewImage = QtGui.QGraphicsView(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bluePreviewImage.sizePolicy().hasHeightForWidth())
        self.bluePreviewImage.setSizePolicy(sizePolicy)
        self.bluePreviewImage.setMaximumSize(QtCore.QSize(128, 128))
        self.bluePreviewImage.setObjectName(_fromUtf8("bluePreviewImage"))
        self.bluePreview.addWidget(self.bluePreviewImage)
        spacerItem8 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.bluePreview.addItem(spacerItem8)
        self.blueContainer.addLayout(self.bluePreview)
        self.blueWavelength_2 = QtGui.QHBoxLayout()
        self.blueWavelength_2.setObjectName(_fromUtf8("blueWavelength_2"))
        self.blueWavelengthLabel_2 = QtGui.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.blueWavelengthLabel_2.sizePolicy().hasHeightForWidth())
        self.blueWavelengthLabel_2.setSizePolicy(sizePolicy)
        self.blueWavelengthLabel_2.setMinimumSize(QtCore.QSize(90, 0))
        self.blueWavelengthLabel_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.blueWavelengthLabel_2.setObjectName(_fromUtf8("blueWavelengthLabel_2"))
        self.blueWavelength_2.addWidget(self.blueWavelengthLabel_2)
        self.blueWavelengthSelect_2 = QtGui.QComboBox(self.verticalLayoutWidget)
        self.blueWavelengthSelect_2.setObjectName(_fromUtf8("blueWavelengthSelect_2"))
        self.blueWavelength_2.addWidget(self.blueWavelengthSelect_2)
        self.blueContainer.addLayout(self.blueWavelength_2)
        self.blueWeight = QtGui.QHBoxLayout()
        self.blueWeight.setObjectName(_fromUtf8("blueWeight"))
        self.blueWeightLabel = QtGui.QLabel(self.verticalLayoutWidget)
        self.blueWeightLabel.setObjectName(_fromUtf8("blueWeightLabel"))
        self.blueWeight.addWidget(self.blueWeightLabel)
        self.blueWeightSlider = QtGui.QSlider(self.verticalLayoutWidget)
        self.blueWeightSlider.setOrientation(QtCore.Qt.Horizontal)
        self.blueWeightSlider.setObjectName(_fromUtf8("blueWeightSlider"))
        self.blueWeight.addWidget(self.blueWeightSlider)
        self.blueContainer.addLayout(self.blueWeight)
        self.wavelengthForm.addLayout(self.blueContainer)
        self.outerContainer.addLayout(self.wavelengthForm)
        RGBComposite.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(RGBComposite)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        RGBComposite.setStatusBar(self.statusbar)
        self.menubar = QtGui.QMenuBar(RGBComposite)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1031, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        RGBComposite.setMenuBar(self.menubar)
        self.actionSave = QtGui.QAction(RGBComposite)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.menuFile.addAction(self.actionSave)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(RGBComposite)
        QtCore.QMetaObject.connectSlotsByName(RGBComposite)

    def retranslateUi(self, RGBComposite):
        RGBComposite.setWindowTitle(QtGui.QApplication.translate("RGBComposite", "SunPy - RGB Composite Image Demo", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("RGBComposite", "Date:", None, QtGui.QApplication.UnicodeUTF8))
        self.redLabel.setText(QtGui.QApplication.translate("RGBComposite", "Red", None, QtGui.QApplication.UnicodeUTF8))
        self.redWavelengthLabel.setText(QtGui.QApplication.translate("RGBComposite", "Wavelength: ", None, QtGui.QApplication.UnicodeUTF8))
        self.redWeightLabel.setText(QtGui.QApplication.translate("RGBComposite", "Weight: ", None, QtGui.QApplication.UnicodeUTF8))
        self.greenLabel.setText(QtGui.QApplication.translate("RGBComposite", "Green", None, QtGui.QApplication.UnicodeUTF8))
        self.greenWavelengthLabel.setText(QtGui.QApplication.translate("RGBComposite", "Wavelength: ", None, QtGui.QApplication.UnicodeUTF8))
        self.greenWeightLabel.setText(QtGui.QApplication.translate("RGBComposite", "Weight: ", None, QtGui.QApplication.UnicodeUTF8))
        self.blueLabel.setText(QtGui.QApplication.translate("RGBComposite", "Blue", None, QtGui.QApplication.UnicodeUTF8))
        self.blueWavelengthLabel_2.setText(QtGui.QApplication.translate("RGBComposite", "Wavelength: ", None, QtGui.QApplication.UnicodeUTF8))
        self.blueWeightLabel.setText(QtGui.QApplication.translate("RGBComposite", "Weight: ", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("RGBComposite", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave.setText(QtGui.QApplication.translate("RGBComposite", "Save", None, QtGui.QApplication.UnicodeUTF8))

