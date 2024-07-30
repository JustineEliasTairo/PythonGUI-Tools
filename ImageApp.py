
# Import all Modules

import os
from datetime import datetime
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication,\
                            QWidget,\
                            QPushButton,\
                            QVBoxLayout,\
                            QHBoxLayout,\
                            QListWidget,\
                            QComboBox,\
                            QFileDialog,\
                            QLabel
from PyQt5.QtGui import QPixmap     # To load the image into PyQt
from PIL import Image,\
                ImageFilter,\
                ImageEnhance



# Creating a Class that inherits a super class "QWidget"
class ImageApp(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Image Editor App");
        self.resize(900,720);
        
        # Create all Obj/Widgets here
        # ---------------------------
        # - Design Here 
        # - Handle Events Here
        
        self.btn_folder      = QPushButton("Folder");
        self.file_list       = QListWidget();
        
        self.btn_left        = QPushButton("Left");
        self.btn_right       = QPushButton("Right");
        self.btn_mirror      = QPushButton("Mirror");
        self.btn_sharpness   = QPushButton("Sharpness");
        self.btn_gray        = QPushButton("B/W");
        self.btn_saturation  = QPushButton("Saturation");
        self.btn_contrast    = QPushButton("Contrast");
        self.btn_blur        = QPushButton("Blur");
        
        # Dropdown box
        self.filter_box = QComboBox();
        self.filter_box.addItem("Original");
        self.filter_box.addItem("Left");
        self.filter_box.addItem("Right");
        self.filter_box.addItem("Mirror");
        self.filter_box.addItem("Sharpness");
        self.filter_box.addItem("B/W");
        self.filter_box.addItem("Saturation");
        self.filter_box.addItem("Contrast");
        self.filter_box.addItem("Blur");
        
        self.pic_box = QLabel("Image space!");
        
        # Main Layout (Hor)
        master_Layout = QHBoxLayout();
        
        colmn1 = QVBoxLayout();
        colmn2 = QVBoxLayout();
        
        colmn1.addWidget(self.btn_folder);
        colmn1.addWidget(self.file_list);
        colmn1.addWidget(self.filter_box);
        
        colmn1.addWidget(self.btn_left);
        colmn1.addWidget(self.btn_right);
        colmn1.addWidget(self.btn_mirror);
        colmn1.addWidget(self.btn_sharpness);
        colmn1.addWidget(self.btn_gray);
        colmn1.addWidget(self.btn_saturation);
        colmn1.addWidget(self.btn_contrast);
        colmn1.addWidget(self.btn_blur);
        
        colmn2.addWidget(self.pic_box);
        
        master_Layout.addLayout(colmn1,stretch=20);
        master_Layout.addLayout(colmn2,stretch=80);
        
        # Set Master Layout to the Main Window
        self.setLayout(master_Layout);



    # End def __init__(self): 
    
    wdir = "";
    # Filter Files and extensions
    def filterFiles(self,files, extensions):
        res = [];
        for ifile in files:
            for ext in extensions:
                if ifile.endswith(ext):
                    res.append(ifile);
        
        return res;
        
    # End def filterFiles(self,files, extensions):
    
    # Choose current working directory
    def getWD(self):
        global wdir;
        wdir = QFileDialog.getExistingDirectory();
        exts = ['.PNG','.png','.svg','.jpg','.jpeg'];
        Fnames = self.filterFiles(os.listdir(wdir),exts);
        self.file_list.clear();
        
        for iFname in Fnames:
            self.file_list.addItem(iFname);
        
        return;
    
    # End def getWD(self):
    
    def load_img(self,filename):
        self.filename = filename;    
        fullname = os.path.join(wdir,self.filename);
        self.image = Image.open(fullname);
        self.original = self.image.copy();  
        tmpStr = self.filename.split('.')
        self.filename = tmpStr[0] + datetime.now().strftime('_%H_%M_%d_%m_%Y.') + tmpStr[-1]; # Give a TimeStamp a copy
        
        return;
    
    # End def load_img(self,filename):
    
    
    
        
    


# End class ImageApp():









# Start the program
if __name__ in "__main__":

    # Main App Obj and settings
    # ---------------------------
    app = QApplication([]);
    main_win = ImageApp();
    

    # Show and Run the App
    # ---------------------------
    main_win.show();
    app.exec_();

# End if __name__ in "__main__":