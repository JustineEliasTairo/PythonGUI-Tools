
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



    # End def __init__(self): 
    
    
    
        
    


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