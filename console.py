import argparse
from control import Control
from Data.data import ContactBook
from Model.model import Model


class Console:
    @staticmethod
    def readConsole():
        parser = argparse.ArgumentParser()
        parser.add_argument("argument", help="add new contact", type=str)
        args = parser.parse_args()
        if args.argument == "add":
            Console().addInput()
        elif args.argument == "delete":
            Console().deleteInput()
        elif args.argument == "edit":
            Console().editInput()
        elif args.argument == "show":
            Console().showInput()
        else:
            print("invalid argument")

    @staticmethod
    def addInput():
        read, write = Model().setTypeSerial()
        book = ContactBook(read())
        Control().addInput(book)
        write(book)

    @staticmethod
    def editInput():
        read, write = Model().setTypeSerial()
        book = ContactBook(read())
        Control().editInput(book)
        write(book)

    @staticmethod
    def deleteInput():
        read, write = Model().setTypeSerial()
        book = ContactBook(read())
        Control().deleteInput(book)
        write(book)

    @staticmethod
    def showInput():
        read, write = Model().setTypeSerial()
        book = ContactBook(read())
        Control().showInput(book)
