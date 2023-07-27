import controller

class File_reader():
    def __init__(self, file, summary, possible_return_trip):
        self.__file = file
        self.__summary = summary
        self.__possible_return_trip = possible_return_trip


    def readfile(self):
        self.__lines = self.__file.readlines()
        self.__controller = controller.Controller(self.__summary, self.__possible_return_trip)

        for self.__line in self.__lines:
            # Format lines, remove the newline and split into a list
            self.__line = self.__line.replace("\n", "").split(" ")

            self.__controller.handle(self.__line)
