import os


try:
    os.system("python -m PyQt5.uic.pyuic -x sidebar.ui -o ui_sidebar.py")
    
except Exception as e:
    print(e)
    pass

# try:
#     os.system(" pyrcc5  resource.qrc -o resource_rc.py")
    
# except Exception as e:
#     print(e)
#     pass