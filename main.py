
import numpy as np
import random
import time
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
import matplotlib.pyplot as plt

sizeArray = 40
#class that stores a list
class Sort:
    list = []
    sortedList = []
    #initialize list and sortedList
    def __init__(self, size):
        for i in range(0, size):
            x = random.uniform(0.0, 1.0)
            self.list.append(x)
        self.sortedList = self.list

#merge two sorted halves of a list
def merge(list, l, m, r):
    left = []
    right = []
    sizeL = m-l+1
    sizeR = r-m
    oldList = list
    #create sublists left and right
    left = list[l:m+1]
    right = list[m+1:r+1]
    #print(f"Size L:{sizeL} Size R:{sizeR} and left and right is: {left} {right}")

    #merge these lists
    i = j = 0
    k = l
    #copy till one list empty
    while(i < sizeL and j < sizeR):
        if(left[i] <= right[j]):
            #list[i + l] = list[k]
            list[k] = left[i]
            i += 1
        else:
            #list[m + 1 + j] = list[k]
            list[k] = right[j]
            j += 1
        k += 1
        saveImage(list)

    while(i < sizeL):
        list[k] = left[i]
        k += 1
        i += 1
        saveImage(list)
    while (j < sizeR):
        list[k] = right[j]
        k += 1
        j += 1
        saveImage(list)
    #print(list)
#recursive mergesort funciton
def mergeSort(list, l, r):
    #print(f"mergeSort {list} from {l} to {r}: {list[l:r+1]}")
    if (r>l):
        m = (r-l) // 2 + l
        mergeSort(list, l, m)
        mergeSort(list, m + 1, r)
        #print(f"Lets merge! List:{list}, l:{l}, m:{m}, r:{r}")
        merge(list, l, m, r)

#saves an image of a list
def saveImage(list):
    data = np.array(list)
    data = np.reshape(data, (1, len(data)))
    dataTemp = data
    data = createSquare(data, dataTemp, list)
    img = plt.imshow(data, interpolation='antialiased')
    img.set_cmap('hot')
    plt.axis('off')
    plt.savefig("test.png", bbox_inches='tight')
    plt.draw()
    plt.pause(0.00000001)
    plt.clf()

def createSquare(data, dataTemp, list):
    for i in range(len(list)):
        data = np.append(dataTemp, data, axis=0)
    return data
arr1 = Sort(sizeArray)
print(f"List to sort is {arr1.list}")
saveImage(arr1.list)
mergeSort(arr1.sortedList, 0, len(arr1.list)-1)
print(f"Sorted list is {arr1.list}")
saveImage(arr1.list)

# class MyWindow(QMainWindow):
#     def __init__(self):
#         super(MyWindow, self).__init__()
#         self.setGeometry(200, 200, 300, 300)
#         self.setWindowTitle("Sorting Demonstration")
#         self.initUI()
#
#     def initUI(self):
#         self.label = QtWidgets.QLabel(self)
#         self.label.setText("Label")
#         self.label.move(50,50)
#         self.b1 = QtWidgets.QPushButton(self)
#         self.b1.setText("Click Me")
#         self.b1.clicked.connect(self.clicked)
#
#     def clicked(self):
#         self.label.setText("You Clicked Button")
#         self.update()
#     def update(self):
#         self.label.adjustSize()
# def window():
#
#     app = QApplication(sys.argv)
#     win = MyWindow()
#
#     win.show()
#     sys.exit(app.exec_())
#
# window()

