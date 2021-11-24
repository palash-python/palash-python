# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 11:35:03 2021

@author: User
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Nov 12 22:48:29 2021

@author: User
"""

import math
import PySimpleGUI as sg

sg.theme('DarkAmber')

def beta(x,y):
        return math.gamma(float(x))*math.gamma(float(y))/math.gamma(float(x)+float(y))

event_list=[]
result=0
Ans=0
global value

layout1=[[sg.Input('', enable_events=True,expand_y=True,s=(2,1), change_submits=True, focus=True, key='-INPUT-', size=(38,6))],
    [sg.Button(button_text='sin',size=(9,1)),sg.Button(button_text="cos",size=(9,1)),sg.Button(button_text="tan",size=(9,1))],
             [sg.Button(button_text='asin',size=(9,1)),sg.Button(button_text="acos",size=(9,1)),sg.Button(button_text="atan",size=(9,1))],
             [sg.Button(button_text='sinh',size=(9,1)),sg.Button(button_text="cosh",size=(9,1)),sg.Button(button_text="tanh",size=(9,1))],
             [sg.Button(button_text='asinh',size=(9,1)),sg.Button(button_text="acosh",size=(9,1)),sg.Button(button_text="atanh",size=(9,1))],
             [sg.Button(button_text='factorial',size=(9,1)),sg.Button(button_text="gamma",size=(9,1)),sg.Button(button_text="beta",size=(9,1))],
             [sg.Button(button_text='pow',size=(9,1)),sg.Button(button_text="log",size=(9,1)),sg.Button(button_text="exp",size=(9,1))],
             [sg.Button(button_text='1',size=(2,1)),sg.Button(button_text='2',size=(2,1)),
              sg.Button(button_text='3',size=(2,1)),sg.Button(button_text='4',size=(2,1)),
              sg.Button(button_text='5',size=(2,1)),sg.Button(button_text='6',size=(2,1)),
              sg.Button(button_text='7',size=(2,1)),sg.Button(button_text='8',size=(2,1))],
             [sg.Button(button_text='9',size=(2,1)),sg.Button(button_text='0',size=(2,1)),
              sg.Button(button_text='pi',size=(2,1)),sg.Button(button_text='e',size=(2,1)),
              sg.Button(button_text='+',size=(2,1)),sg.Button(button_text='-',size=(2,1)),
              sg.Button(button_text='*',size=(2,1)),sg.Button(button_text='/',size=(2,1))],
             [sg.Button(button_text='(',size=(2,1)),sg.Button(button_text=')',size=(2,1)),
              sg.Button(button_text='.',size=(2,1)),sg.Button(button_text=',',size=(2,1)),
              sg.Button(button_text='=',size=(2,1)),
              sg.Button(button_text='del',size=(3,1)),sg.Button(button_text='clear',size=(5,1))],
             [sg.Button(button_text='Input',size=(5,1)),sg.Button(button_text='Ans',size=(3,1)),sg.Button("Exit")]
             ]
window1=sg.Window("Scientific Calculator by Palash",layout1,size=(300,380),element_justification='left',
                  background_color="red3",titlebar_text_color=("yellow"))
    
while(1):
    event1, values1 = window1.read()
    
    
    if event1=="Exit" or event1==sg.WIN_CLOSED:
        break
    
    elif event1== "=" :
        try:
            s=""
            for i in event_list:
                if i in ["sin","cos","tan","asin","acos","atan","sinh","cosh","tanh","asinh","acosh","atanh",
                         "factorial","gamma","pow","log","exp","pi","e"]:
                    s+="math."+i
                else:
                    s+=i
            result=eval(s)
            Ans=result
            sg.Popup("Your answer is: {}=".format(s),result)
            event_list=[]
            window1['-INPUT-'].update(result)#['-INPUT-'][:-1])
            result=0
        except SyntaxError :
            sg.Popup("SyntaxError. You entered wrong values: {} . Try again.".format("".join(event_list)))
            event_list=[]
            window1['-INPUT-'].update("")#['-INPUT-'][:-1])
        except ValueError :
            sg.Popup("ValueError. You entered wrong values: {} . Try again.".format("".join(event_list)))
            event_list=[]
            window1['-INPUT-'].update("")#['-INPUT-'][:-1])
        except TypeError :
            sg.Popup("TypeError. You entered wrong values: {} . Try again.".format("".join(event_list)))
            event_list=[]
            window1['-INPUT-'].update("")#['-INPUT-'][:-1])
        except KeyError :
            sg.Popup("KeyError. You entered wrong values: {} . Try again.".format("".join(event_list)))
            event_list=[]
            window1['-INPUT-'].update("")
        except AttributeError :
            sg.Popup("AttributeError. You entered wrong values: {} . Try again.".format("".join(event_list)))
            event_list=[]
            window1['-INPUT-'].update("")
        except NameError :
            sg.Popup("NameError. You entered wrong values: {} . Try again.".format("".join(event_list)))
            event_list=[]
            window1['-INPUT-'].update("")
        except ZeroDivisionError :
            sg.Popup("ZeroDivisionError. You entered wrong values: {} . Try again.".format("".join(event_list)))
            event_list=[]
            window1['-INPUT-'].update("")
            
    elif event1=="del":
        event_list=event_list[0:-1]
        window1['-INPUT-'].update(event_list)#['-INPUT-'][:-1])
        
    elif event1=="clear":
        event_list=[]
        window1['-INPUT-'].update(event_list)#['-INPUT-'][:-1])
    
    elif event1=='-INPUT-':
        
        try:
            value=list(values1.values())[0][-1]
            #sg.Print(value)
            #sg.Popup(value)
            if value=="=" :#list(values1.values())[0][-1] == "=" :
                try:
                    s="".join(event_list)
                    for i in ["sin","cos","tan","asin","acos","atan","sinh","cosh","tanh","asinh","acosh","atanh",
                                 "factorial","gamma","pow","log","exp","pi","e"]:
                        s=s.replace(i,"math."+i)
                    result=eval(s)
                    Ans=result
                    sg.Popup("Your answer is: {}=".format(s),result)
                    event_list=[]
                    window1['-INPUT-'].update(result)#['-INPUT-'][:-1])
                    result=0
                except SyntaxError :
                    sg.Popup("SyntaxError. You entered wrong values: {} . Try again.".format("".join(event_list)))
                    event_list=[]
                    window1['-INPUT-'].update("")#['-INPUT-'][:-1])
                except ValueError :
                    sg.Popup("ValueError. You entered wrong values: {} . Try again.".format("".join(event_list)))
                    event_list=[]
                    window1['-INPUT-'].update("")#['-INPUT-'][:-1])
                except TypeError :
                    sg.Popup("TypeError. You entered wrong values: {} . Try again.".format("".join(event_list)))
                    event_list=[]
                    window1['-INPUT-'].update("")#['-INPUT-'][:-1])
                except KeyError :
                    sg.Popup("KeyError. You entered wrong values: {} . Try again.".format("".join(event_list)))
                    event_list=[]
                    window1['-INPUT-'].update("")
                except AttributeError :
                    sg.Popup("AttributeError. You entered wrong values: {} . Try again.".format("".join(event_list)))
                    event_list=[]
                    window1['-INPUT-'].update("")
                except NameError :
                    sg.Popup("NameError. You entered wrong values: {} . Try again.".format("".join(event_list)))
                    event_list=[]
                    window1['-INPUT-'].update("")
                except ZeroDivisionError :
                    sg.Popup("ZeroDivisionError. You entered wrong values: {} . Try again.".format("".join(event_list)))
                    event_list=[]
                    window1['-INPUT-'].update("")
                
            elif value ==" " :
                event_list=event_list[0:-1]
                window1['-INPUT-'].update(event_list)
                #sg.Popup(value)
            else:
                #value=list(values1.values())[0][-1]
                event_list.append(value)
                window1['-INPUT-'].update(event_list)
                #sg.Popup(event_list)
            
        except IndexError :
            sg.Popup("IndexError. You entered wrong values: {} . Try again.".format("".join(event_list)))
            event_list=[]
            window1['-INPUT-'].update("")
    
    elif event1=='Input':
        layout2=[[sg.Input()],[sg.OK()]]
        win2=sg.Window('Type your inputs here',layout2)
        event2,values2=win2.read()
        if event2=="OK":
            s="".join(list(values2.values()))
            for i in ["sin","cos","tan","asin","acos","atan","sinh","cosh",
                      "tanh","asinh","acosh","atanh","factorial","gamma","pow","log","exp","pi","e"]:
                s=s.replace(i,'math.'+i)
            try:
                result=eval(s)
                window1['-INPUT-'].update(result)
                Ans=result
                result=0
            except:
                sg.Popup("Error. Enter correct values.")
                window1['-INPUT-'].update("")
        win2.close()
    else:
       event_list.append(event1)
       window1['-INPUT-'].update(event_list)#['-INPUT-'][:-1])
       
    
window1.close()