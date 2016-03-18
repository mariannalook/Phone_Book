from test import menu
from model import *
from module import showBook
from Info import all_information

while True:
    key = menu()
    if key =='1':
        Edit_information().add()
    elif key=="2":
        Edit_information().edit_record()
    elif key =="3":
        Edit_information().delete_record()
    elif key=="4":
        Edit_information().sort()
    elif key =="5":
        Edit_information().see_all()
    elif key =="6":
        exit()
    else:
        print("Uncorrect. Please,try again")