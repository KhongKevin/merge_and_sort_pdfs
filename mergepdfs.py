# Author - Kevin Khong Lightweight merge/sort pdf files 


import os

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QFileDialog
from PyQt5.QtGui import QPixmap
from PyPDF2 import PdfFileMerger

class PDFMerger(QWidget):
    def __init__(self):
        super().__init__()

        self.merger = PdfFileMerger()
        self.init_ui()
        self.setGeometry(100, 300, 300, 100)


    # method called by button
    def changeColor(self):
  
        # if button is checked
        if self.button.isChecked():
  
            # setting background color to light-blue
            self.button.setStyleSheet("background-color : lightblue")
  
        # if it is unchecked
        else:
  
            # set background color back to light-grey
            self.button.setStyleSheet("background-color : lightgrey")
        
    # Create a vertical layout to arrange the buttons
    def init_ui(self):
        self.setWindowTitle('PDF Merger')
        

        # Create a button to select the PDF files
        btn_select_pdfs = QPushButton('Select PDFs', self)
        btn_select_pdfs.clicked.connect(self.select_pdfs)

        # Create a button to merge the PDF files
        btn_merge = QPushButton('Merge', self)
        btn_merge.clicked.connect(self.merge_pdfs)
        
        # creating a push button
        self.button = QPushButton("Sort By Date", self)
    
        # setting checkable to true
        self.button.setCheckable(True)
        # setting calling method by button
        self.button.clicked.connect(self.changeColor)
  
        # setting default color of button to light-grey
        self.button.setStyleSheet("background-color : lightgrey")
  
        # show all the widgets
        self.update()
        self.show()
  
    
        vbox = QVBoxLayout()
        vbox.addWidget(btn_select_pdfs)
        vbox.addWidget(btn_merge)
        vbox.addWidget(self.button)
        self.setLayout(vbox)



    def select_pdfs(self):
        # Open a file dialog to select the PDF files
        file_names, _ = QFileDialog.getOpenFileNames(
            self, 'Select PDFs', os.getenv('HOME'), 'PDF Files (*.pdf)'
        )
        if self.button.isChecked():
            file_names = sorted(file_names, key=lambda t: -os.stat(t).st_mtime)
        # Add the selected PDF files to the merger
        for file_name in file_names:
            self.merger.append(file_name)

    def merge_pdfs(self):
        # Open a file dialog to select the output PDF file
        output_file_name, _ = QFileDialog.getSaveFileName(
            self, 'Save PDF', os.getenv('HOME'), 'PDF Files (*.pdf)'
        )

        # Merge the PDF files
        self.merger.write(output_file_name)
        self.merger.close()

        # Show a message box to confirm that the PDF files have been merged
        messagebox.information(
            self, 'PDF Merger', 'PDF files have been merged successfully!'
        )

if __name__ == '__main__':
    app = QApplication([])
    pdf_merger = PDFMerger()
    pdf_merger.show()
    app.exec_()
