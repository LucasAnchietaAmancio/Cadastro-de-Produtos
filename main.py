from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout,QComboBox,QTableWidgetItem,QTableWidget,QMdiSubWindow,QTextEdit
from PySide6.QtCore import QCoreApplication, QPropertyAnimation  
from PySide6 import QtCore 
from PySide6.QtGui import QMouseEvent
from PySide6.QtCore import (Qt,QPoint) 
from ui_main import Ui_Form
import sys
import mysql.connector
import random
import os
from PySide6.QtGui import QIcon


class MainWindow(QMainWindow, Ui_Form):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.moving = False
        self.offset = QPoint()

        self.central_widget = QWidget(self)  

        self.setCentralWidget(self.central_widget)  

        self.setupUi(self.central_widget)

        self.setWindowTitle("Cadastro de Produtos")
        
        self.coluna_remov = 2  # Índice da coluna a ser removida
        self.tableWidget.removeColumn(self.coluna_remov)
        self.cod_ramdom = str(random.randint(12417,35546))
        self.sql_consulta = "SELECT codprd, descricao, quantidade, fornecedor FROM produtos LIMIT 40"
        #######################################################
        #botao
        self.pushButton_10.clicked.connect(self.abrir_menu)
        self.pushButton_7.clicked.connect(self.sair)
        self.pushButton.clicked.connect(self.fechar)
        self.pushButton_11.clicked.connect(self.sair)
        self.pushButton_4.clicked.connect(self.fechar)
        self.pushButton_3.clicked.connect(self.maximizar)
        self.pushButton_2.clicked.connect(self.minimizar)
        self.pushButton_13.clicked.connect(self.consulta)
        self.pushButton_16.clicked.connect(self.cancelar)
        self.setWindowFlags(Qt.FramelessWindowHint)
        #######################################################
        #pagina
        self.pushButton_9.clicked.connect(lambda: self.paginas.setCurrentWidget(self.home))
        self.pushButton_8.clicked.connect(lambda: self.paginas.setCurrentWidget(self.cadastro))
        self.pushButton_14.clicked.connect(self.cadastro_sql)
       # Insere uma nova linha na posição final
        self.maximized = False
        # Adicionando itens na nova linha 
        self.lineEdit.setText(self.cod_ramdom)
        
        
        self.tableWidget.setColumnWidth(0, 150)  # Define a largura da primeira coluna
        self.tableWidget.setColumnWidth(1, 210)  # Define a largura da segunda coluna
        self.tableWidget.setColumnWidth(2, 100)
        self.tableWidget.setColumnWidth(3, 100)

        if getattr(sys, 'frozen', False):
            diretorio_icone = os.path.join(sys._MEIPASS, "icons")  # Caminho no executável
        else:
            diretorio_icone = "icons"  # Caminho durante o desenvolvimento

        # Carregar os ícones individualmente
        self.icone_inicio = QIcon(os.path.join(diretorio_icone, "botao-de-inicio.png"))
        self.icone_usuario = QIcon(os.path.join(diretorio_icone, "adicionar-usuario.png"))
        self.icone_fechar = QIcon(os.path.join(diretorio_icone, "botao-fechar.png"))
        self.icone_casa = QIcon(os.path.join(diretorio_icone, "casa.png"))
        self.icone_sair = QIcon(os.path.join(diretorio_icone, "sair (1).png"))
        self.icone_documento = QIcon(os.path.join(diretorio_icone, "novo-documento.png"))
        self.icone_menu_aberto = QIcon(os.path.join(diretorio_icone, "menu-aberto.png"))

        # Definir o ícone principal da janela
        self.setWindowIcon(self.icone_inicio)

    def conect(self):
        self.conn = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "root",
        database = "paineldb",
        )
        self.Cursor = self.conn.cursor()   
    

    def selecionar_valor(self, text):
        # Atualizando o label com o valor selecionado
        self.label.setText(f"Você selecionou: {text}")
        print(f"Valor selecionado: {text}")


    def sair(self):
        
        tamanho = self.frame_16.height()

        if tamanho == 0:
            novo = 50
        else:
            novo = 0    
        self.animation = QtCore.QPropertyAnimation(self.frame_16,b"maximumHeight")
        self.animation.setDuration(200)
        self.animation.setStartValue(tamanho)
        self.animation.setEndValue(novo)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()
               
#########################################################REALIZA UM INSERT DOS DADOS COLETADOS                           
    def cadastro_sql(self):
        self.line_cod = self.lineEdit.text()
        self.line_desc = self.lineEdit_2.text()
        self.line_quant = self.lineEdit_3.text()
        self.line_preco_compra = self.lineEdit_4.text()
        self.line_preco_venda = self.lineEdit_5.text()
        self.box = self.comboBox.currentText()
        ##if self.line_desc == '' or self.line_preco_venda == '':
            ##print("informações inválidas")
            
            ####colocar uma mensagem na tela dizendo que a descrição ou o preço não foi digitado###
            ##return False
        ##else:
        try:
            
            self.dados = (int(self.line_cod),str(self.line_desc),int(self.line_quant),float(self.line_preco_compra),float(self.line_preco_venda),str(self.box))

            self.sql_cadastro = "INSERT INTO produtos (codprd,descricao,precocompra,precovenda,quantidade,fornecedor) VALUES (%s,%s,%s,%s,%s,%s)"

            self.Cursor.execute(self.sql_cadastro,self.dados)

            self.conn.commit()

            self.Cursor.close()

            self.conn.close()

            print("Cadastro salvo")

        except:
             
            print("falha na validação dos dados")    
#####################################################################################################################   

#########################################################MAXIMIZA MINHA TELA E REPOSICIONA AS COLUNAS DA QtableWidget
    def maximizar(self):
         try:
            if not self.maximized:

             self.showMaximized()
             self.tableWidget.setColumnWidth(0, 390)  # Define a largura da primeira coluna
             self.tableWidget.setColumnWidth(1, 510)  # Define a largura da segunda coluna
             self.tableWidget.setColumnWidth(2, 390)
             self.tableWidget.setColumnWidth(3, 500)
             self.maximized = True

            else:
             
             self.showNormal()
             self.tableWidget.setColumnWidth(0, 150)  # Define a largura da primeira coluna
             self.tableWidget.setColumnWidth(1, 210)  # Define a largura da segunda coluna
             self.tableWidget.setColumnWidth(2, 100)
             self.tableWidget.setColumnWidth(3, 100)
             self.maximized = False
         except:
        
             return True
##################################################################################################################

#########################################################
    def minimizar(self):
        window.showMinimized() 
#########################################################

    def fechar(self):
        window.close()       
#########################################################


    def abrir_menu(self):
        width = self.left_menu.width()

        if width  == 9:
            new = 300
        else:
            new = 9
        self.animacao = QtCore.QPropertyAnimation(self.left_menu, b"maximumWidth")
        self.animacao.setDuration(500)
        self.animacao.setStartValue(width)
        self.animacao.setEndValue(new)
        self.animacao.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animacao.start() 
####################################### REALIZA UMA CONSULTA SQL QUE RETORNA VALORES PARA DENTO DOS ITENS DA QtableWidget
    def consulta(self):
        try:
            self.conect()
            self.Cursor = self.conn.cursor()   
             
            self.sql = self.sql_consulta

            self.Cursor = self.conn.cursor()
            

            self.Cursor.execute(self.sql)

            try:
                dados = self.Cursor.fetchall()
            except:
                print(f"Erro ao buscar dados")
                return False
            

            self.tableWidget.setRowCount(len(dados))
            

            for row, text in enumerate(dados): 

                for column, data in enumerate(text): 

                    item = QTableWidgetItem(str(data))

                    self.tableWidget.setItem(row, column, item)
                
        except:
            print("Erro ao executar a consulta")
##################################################################################################################


########################################################## ZERA OS VALORES RETORNADOS NA CONSULTA E TERMINA O CURSOR 
    def cancelar(self):
        self.tableWidget.setRowCount(0)
        self.lineEdit.setText('')
        self.lineEdit_2.setText('')
        self.lineEdit_3.setText('')
        self.lineEdit_4.setText('')
        self.lineEdit_5.setText('')
        self.Cursor.close()
#####################################################################################################################


######################################################### DEIXA A TELA FELXIVEL PARA INTERAÇÕES COM O MOUSE
    def mousePressEvent(self, event: QMouseEvent):

            if event.button() == Qt.LeftButton:
                self.moving = True
                self.offset = event.pos()  

    def mouseMoveEvent(self, event: QMouseEvent):

            if self.moving:
                self.move(event.globalPos() - self.offset)

    def mouseReleaseEvent(self, event: QMouseEvent):

            if event.button() == Qt.LeftButton:
                self.moving = False  
##################################################################################################################
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())