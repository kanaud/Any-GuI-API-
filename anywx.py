#!/usr/bin/env python
#Author:Manjeet Singh
#first append the event before calling an event    
#author Manjeet Singh Kanaud 
import wx
now_position=[180,10]
def default_postion(w):
        now_position[1]=now_position[1]+10+w
        return now_position
        
''' WX_frame : On it widget can be appended '''
class frame(wx.Frame):
    parent = None
    Type = "frame"
    parent=None
                                        #default id of the frame -1
    id=wx.NewId()
                                        #default title of the frame "frame"
    title="frame"
                                        #default position of the frame pos
    pos=(300, 150)
                                        #default size of the frame 
    size=(600,750)
    def __init__(self, id=-1, title="frame",width=750,height=500):
        self.app = wx.App(False)
        wx.Frame.__init__(self, self.parent, id, title, wx.DefaultPosition, wx.Size(width, height))
        self.panel = wx.Panel(self, -1)


    def show(self):
        self.Centre()
        self.Show(True)
        #self.Centre()
        self.app.MainLoop()
        return

# THE FUNCTION TO ADDs widgetS ON THE FRAME 
    def append(self,widget):
        widget_type = type(widget)
       # print widget_type
                                                                                                                        
                                                                                                                        # if widget is of type text_area
        if(widget_type==text_area or isinstance(widget,text_area)):
            widget.suk = wx.TextCtrl(self.panel, -1, widget.text,  widget.pos, widget.size, style=wx.TE_MULTILINE)
        
                                                                                                                                #if widget is of type text_area
        elif(widget_type==text_field or isinstance(widget,text_field)):
            widget.suk = wx.TextCtrl(self.panel, -1, widget.label,  widget.pos, widget.size)
                                                                                                                        #if widget is of type button
        elif(widget_type==button or isinstance(widget,button)):
            widget.suk = wx.Button(self.panel, -1, widget.label,  widget.pos, widget.size)
            if(widget.callback != None ):
                widget.suk.Bind(wx.EVT_BUTTON, widget.callback)
                                                                                                                        #if widget is of type check_box

        elif(widget_type==check_box or isinstance(widget,check_box)):
            widget.suk = wx.CheckBox(self.panel, -1, widget.label,  widget.pos,widget.size)
            widget.suk.SetValue(widget.value)
                                                                                                                       
        
        elif(widget_type==combo_box or isinstance(widget,combo_box)):
            widget.suk = wx.ComboBox(self.panel, -1,widget.default,widget.pos,widget.size,widget.labels,style=wx.CB_READONLY)
            
                                                                                                                #if widget is of type static_text
        elif(widget_type==static_text or isinstance(widget,static_text)):
            widget.suk = wx.StaticText(self.panel, -1,widget.label,widget.pos,widget.size)
                                                                                                                
                                                                                                                                 #if widget is of type radio_buttons
        elif(widget_type==radio_buttons or isinstance(widget,radio_buttons)):
            widget.suk = []
            radio_suk = wx.RadioButton(self.panel, -1, widget.labels[0], widget.positions[0],widget.size,style=wx.RB_GROUP)
            widget.suk.append(radio_suk)
            for i in range(1,len(widget.labels)):
                radio_suk = wx.RadioButton(self.panel, -1, widget.labels[i], widget.positions[i],widget.size)
                widget.suk.append(radio_suk)
                                                                                                                                               
            if(widget.selected_index != None):
                widget.suk[widget.selected_index].SetValue(True)
        elif(widget_type==Slider or isinstance(widget,Slider)):
            widget.instance = wx.Slider(self.panel, -1,minValue=widget._from, maxValue=widget._to, pos=widget.position, size=widget.size,  style=wx.SL_HORIZONTAL) 
  elif(widget_type==SpinBox or isinstance(widget,SpinBox)):
	     widget.instance = wx.SpinCtrl(self.panel,-1,size = widget.size,pos = widget.pos,min=widget._from,max=widget._to)             
	     #widget.instance.SetRange=(widget._from,widget._to)
	     #widget.instance.SetMax=200
	     
	     
	     
	                                                                                          #if widget is of type combo_box

#class Widget:
   # pass



''' WIDGET: text_field '''
class text_field(wx.TextCtrl):
    suk = None
                                #default text in the text field
    label="default text" 
                                #default position
    pos=(45,56)    
                                #default size 
    size=(80,100) 
                                
    visibility=True                            #constructor of text_field
                                
    def __init__(self):
        tmp=1
                                #function sets text in the  in the text_field
    def set_text(self,text):
        if(self.suk == None):
            self.text = text
        else:
            self.suk.SetValue(text)
        return True
                                #get the text in the text_field
    def get_text(self):
        if(self.suk == None):
            return self.text
        else:
            return self.suk.GetValue()

''' WIDGETS:static_text for appending static text in the application '''
class static_text(wx.StaticText):
    suk = None
    parent=None
    id=-1
                                #function is used to specify the default_postion
    p=default_postion(0)         
                                #default position         
    pos=(p[0],p[1])      
                                #default label
    label="static text"   
                                #default size
    size=(45,50)
                                
    default_postion(15)
                                        #default constructor for static_text
    def __init__(self):
        tmp=1


''' WIDGETS: text_area '''
class text_area(wx.TextCtrl):
    suk = None
                        #default position of text area
    pos=(60,80);
                        #default size of text_area
    size=(100,200)
                                #default text in text_area
    text="this is default temp"
                                #constructor for the class
    def __init__(self):
        tmp=1
                        #user defined default text
    def set_text(self,text):
        if(self.suk == None):
            self.text = text
        else:
            self.suk.SetValue(text)
        return True
                        #function to get the text in the text_area
    def get_text(self):
        if(self.suk == None):
            return self.text
        else:
            return self.suk.GetValue()

                       #append text in the text area 
    def append_text(self,text):
        if(self.suk == None):
            self.text = self.suk.GetValue() + text
        else:
            self.suk.AppendText(text)
        return True              
                        #clear the text_area
    def clear(self):
        self.suk.Clear()
        return True






''' WIDGETS: Button '''
class button(wx.Button):
    suk = None
    callback = None
    id=-1
                        #function for specifing default position
    p=default_postion(0)
                                #defined default position of the button
    pos=(p[0],p[1])
               #print p
                                #default size of the button
    size=(185,35)
    default_postion(35)
                                        #default label of the button
    label="button"
    def __init__(self):
        tmp=1
                                #function to define an event on clickListener
    def onclick(self,method):
        if(self.suk == None):
            self.callback = method
        else:
            self.suk.Bind(wx.EVT_BUTTON, method)
        return True

''' WIDGETS: check box    '''
class check_box(wx.CheckBox):
    suk = None
    value = False
    parent =None
                                        #default label for check_box
    label="check box"
    
    p=default_postion(0)
                                                #default size of the chack_box
    size=(150,20)
    pos=(p[0],p[1])
                                        #constructor for chack_box
    def __init__(self):
        tmp=1
                                                #set_value function sets the default user value for check box
    def set_value(self,value):
        if(self.suk == None):
            self.value = value
        else:
            self.suk.SetValue(value)
                                                #get_text function returns the value of the check_box
    def get_value(self):
        if(self.suk == None):
            return self.value
        else:
            return self.suk.IsChecked()

''' WIDGETS: radio_buttons '''
class radio_buttons(wx.RadioButton):
    suk = None
    selected_index = None
    parent=None
                                #default size of the radio buttons group
    size=(45,50)
                                #constructor for radio_buttons
    def __init__(self):
        self.labels = []
        self.positions = []
       # self.size = wx.Size(width, height)
                                        #this function appends radio button
    def append_rb(self,label,X,Y):
        self.labels.append(label)
        self.positions.append((X,Y))
        return True

    def get_value(self):
        for i in range(len(self.suk)):
            if(self.suk[i].GetValue()):
                return self.labels[i]
        return None

    def set_true(self,index):
        if(self.suk == None):
            self.selected_index = index
        else:
            button_suk = self.suk[index]
            button_suk.SetValue(True)

''' WIDGET: combo_box '''
class combo_box(wx.ComboBox):
    suk = None
    labels=[]
    pos=(45,80)
    size=(45,60)
    default="<default>"
    def __init__(self):
        tmp=1

    def get_value(self):
            if(self.suk == None):
                return self.value
            else:
                return self.suk.GetValue()



''' WIDGETS: Slider '''
class Slider(wx.Slider):
    instance = None
    def __init__(self,_from,_to,X,Y,width,height):
        self.position = (X,Y)
        self.size = wx.Size(width, height)
        self._from = _from
        self._to = _to

    def getValue(self):
        return self.instance.GetValue()

class SpinBox(wx.SpinButton):
    instance = None

    def __init__(self,_from,_to,X,Y,width,height):
	self.pos = (X,Y)
	self.size = wx.Size(width,height)
	self._from = _from
	self._to = _to

    def getValue(self):
	return self.instance.GetValue()
