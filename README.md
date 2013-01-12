                                                     ANY GUI

Introduction

python has many GUI tool kits available  such as :

1)                                                     WxPython
2)	Tkinter
3)	pyQT
4)	pyGTK
5)	pyjs(Python javasccript)
6)	easyGUI  , etc.

	the goal of the project is to provide the user API to the users for most used tool kits
like wxPython,Tkinter,pyQT,pyGTK.

ANY GUI API

using toolkits:
wxPYTHON : from anygui import anywx
pyGTK : from anygui import anygtk
pyQT : from anygui import anyqt
tkinter : from anygui import anytk

Widgets :

in anygui API there is only one top widget frame and rest all the widgets are added to
the frame.
In rest of documentation lets assume the selected tool kit is imported as a
eg.
	from anygui import anywx as a
anygui api automatically assigns default values for ol widgets .
Frame:
frame can be added by making an instance of class frame present in anygui api
eg
	f=g.frame(id,title,width,height)
	
	id=id of the frame instance  				 	  default value=-1
	title=title that appear on the top of the frame   as string           default value=frame
	width=width of the frame 					  default value =750
	height=height of the frame 				              default value=500

Append function:
all other widgets other then top level frame widget has to be added to the farme by calling
append function of the frame
	eg. For adding static_text call f.append(static_text)
		where static_text is the instance of widget static_text



show function :
should be executed at the end of the app to run the api .
	Eg
		f.show()

Static Text:

To add static text to the frame in our application by using class static_text
eg
	s=static_text()

in anygui all other attributes of the widget are class variable of that widget
these attributes can be used to edit widgets for a user defined value

class variable of static_text
	1)position of static text
	pos=(x,y)
	
		x=width
	 	y=height
	2)size of static text
	size=(x,y)
		x=width
		y=height
		
	3)label=” ”
		label of static text as a string
		default=”static text”	

	
Button:
to add button in the frame make a instance of widget button
	eg.
		b=button()
	
	button variables are :
	
	1) pos =(x,y)
		assigning position to the button
		eg.
			b.pos=(20,45)

	2) size=(x,y)
		size of the button
		eg.
			b.size=(20,45)

	3) label=” “
		label on the button
		eg.
			b.label=”click button”

	button widget also has pre defined functions:

	1) onclick(function)
		here function defines the function that is executed on button click
Check Box:
to add check box in the frame make a instance of the widget check_box

	eg.
	
		c=check_box()
check box variable are :
	
	1) pos =(x,y)
		assigning position to the checkbox
		eg.
			c.pos=(20,45)

	2) size=(x,y)
		size of the checkbox
		eg.
			c.size=(20,45)

	3) label=” “
		label on the checkbox
		eg.
			c.label=”check box 1”

check_box also has following functions
	
	set value:     set_value(BOOL)
		can be used to set check box to clicked =true or not clicked = false
			eg.
				c.set_value(True)
	get value: get_value()
		returns boolian value for a checkbox either true for clicked and
				false for not clicked

Combo box:
To add combo box in the frame make a instance of the widget combo_box

	eg.
	
		c=combo_box()
check box variable are :
	
	1) pos =(x,y)
		assigning position to the combo box
		eg.
			c.pos=(20,45)

	2) size=(x,y)
		size of the combo box
		eg.
			c.size=(20,45)

	3) labels=[]
		options in the combo box can be assigned by label list
		eg.
			c.label=[“vol 1”,”vol2”,.........]
	4)default
		user defined default value for the combo box
		eg
			c.default=” vol 3”	

check_box also has following functions

	get value: get_value()
		returns string value for a combo box of the choice selected

			s=c.get_value()

Text feild:
To add  single line text field  in the frame make a instance of the widget text_field

	eg.
	
		c=text_feild()
check box variable are :
	
	1) pos =(x,y)
		assigning position to the text_feild
		eg.
			c.pos=(20,45)

	2) size=(x,y)
		size of the text_feild
		eg.
			c.size=(20,45)

	3) label=” ”
		assigning user defined default text in the text_feild
		eg.
			c.label=”this is text in text feild”


check_box also has following functions

	1)get text: get_text()
		returns string of the text present in the text feild

			s=c.get_text()
	
	
	3)set text: set_text(string str)
	
		set  string of the text  in the text feild

			s=c.set_text(“this is in text feild”)	
	

Text Area:
To add multiline text area  in the frame make a instance of the widget text_area

	eg.
	
		c=text_area()
check box variable are :
	
	1) pos =(x,y)
		assigning position to the text_area
		eg.
			c.pos=(20,45)

	2) size=(x,y)
		size of the text_area
		eg.
			c.size=(20,45)

	3) text=” ”
		assigning user defined default text in the text_area
		eg.
			c.text=”this is text in text area”
		

text_area also has following functions

	1)get text: get_text()
		returns string of the text present in the text area

			s=c.get_text()
	2)clear: clear()
			clear the text present in the text area  

			s=c.clear()
	
	3)set text: set_text(string str)
	
		set  string of the text  in the text area

			s=c.set_text(“this is in text area”)	
	4)append text: append_text(string str)
		appends string of the text present in the text area to the string passed
			in the function

			s=c.append_text(“this string will get appended”)

Radio buttons:
To add radio button set in the frame make a instance of the widget radio_buttons

	eg.
	
		c=radio_buttons()
to add single radio button in the grup use append_rb function
		append_rb(label,weidth,height)
	eg.
		c.appendr_rb(label,width,height)
check box variable are :
	

	1) size=(x,y)
		size of the radio button grup
		eg.
			c.size=(20,45)

		

radio_buttons  also has following functions

	1)get value: get_value()
		returns string of the label that was clicked  

			s=c.get_value()

	
	3)set_true: set_true(int n)
	
		set radio button n to be clicked

			c.set_true(2)	
	
