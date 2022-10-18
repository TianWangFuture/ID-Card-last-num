import PySimpleGUI as sg
layout = [
	[sg.Text('请输入身份证号前十七位:')],
	[sg.InputText()],
	[sg.OK()]
  [sg.Text('made with TWFuture (有转载部分） ')]
]
window = sg.Window('TWFuture-ID-card-last-num',layout)
event,value = window.Read()
axc = value [0]
temp = zip(axc[0:17], [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2])
temp2 = map(lambda x:int(x[0])*x[1], temp)
temp3 = sum(temp2)
temp4 = '10X98765432'[temp3 % 11]
sg.Popup("你的身份证号最后一位是",temp4)



