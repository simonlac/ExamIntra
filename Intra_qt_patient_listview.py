# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'intra_patient_listview.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(567, 611)
        self.listView_Patient = QtWidgets.QListView(Dialog)
        self.listView_Patient.setGeometry(QtCore.QRect(80, 250, 381, 241))
        self.listView_Patient.setObjectName("listView_Patient")
        self.label_lst_patient_15_25 = QtWidgets.QLabel(Dialog)
        self.label_lst_patient_15_25.setGeometry(QtCore.QRect(100, 220, 361, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_lst_patient_15_25.setFont(font)
        self.label_lst_patient_15_25.setObjectName("label_lst_patient_15_25")
        self.pushButton_quitter = QtWidgets.QPushButton(Dialog)
        self.pushButton_quitter.setGeometry(QtCore.QRect(160, 500, 191, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_quitter.setFont(font)
        self.pushButton_quitter.setObjectName("pushButton_quitter")
        self.label_montant = QtWidgets.QLabel(Dialog)
        self.label_montant.setGeometry(QtCore.QRect(160, 130, 251, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_montant.setFont(font)
        self.label_montant.setObjectName("label_montant")
        self.lbedit_montant = QtWidgets.QLineEdit(Dialog)
        self.lbedit_montant.setGeometry(QtCore.QRect(160, 170, 211, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.lbedit_montant.setFont(font)
        self.lbedit_montant.setObjectName("lbedit_montant")
        self.label_erreur_montant = QtWidgets.QLabel(Dialog)
        self.label_erreur_montant.setGeometry(QtCore.QRect(160, 120, 421, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_erreur_montant.setFont(font)
        self.label_erreur_montant.setObjectName("label_erreur_montant")
        self.label_erreur_nb_visite = QtWidgets.QLabel(Dialog)
        self.label_erreur_nb_visite.setGeometry(QtCore.QRect(160, 20, 421, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_erreur_nb_visite.setFont(font)
        self.label_erreur_nb_visite.setObjectName("label_erreur_nb_visite")
        self.label_nb_visite = QtWidgets.QLabel(Dialog)
        self.label_nb_visite.setGeometry(QtCore.QRect(160, 30, 251, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_nb_visite.setFont(font)
        self.label_nb_visite.setObjectName("label_nb_visite")
        self.lbedit_nbvisite = QtWidgets.QLineEdit(Dialog)
        self.lbedit_nbvisite.setGeometry(QtCore.QRect(160, 70, 211, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.lbedit_nbvisite.setFont(font)
        self.lbedit_nbvisite.setObjectName("lbedit_nbvisite")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_lst_patient_15_25.setText(_translate("Dialog", "La liste des patients entre 15 et 25"))
        self.pushButton_quitter.setText(_translate("Dialog", "Quitter"))
        self.label_montant.setText(_translate("Dialog", "Montant d\'une visite"))
        self.label_erreur_montant.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#ff0000;\">le montant n\'entre pas dans les paramètres.</span></p></body></html>"))
        self.label_erreur_nb_visite.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#ff0000;\">le nombre de visite n\'entre pas dans les paramètres.</span></p></body></html>"))
        self.label_nb_visite.setText(_translate("Dialog", "Nombre de visite(s)"))
