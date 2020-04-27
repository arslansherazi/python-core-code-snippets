from tkinter import *
from tkinter import ttk #Treeview is a Widget of ttk so it should be included to use Treeview Widget.




def callback(event):
    item=treeView.selection()
    #"item" is an array in which ids of selected items are stored.
    #If we select multiple items then their ids are stored at particular indexes of item array according to the sequence of their selection.
    #"selection" function is used to specify the actual form of selected item id.
    
    
    if(item[0]=='child1'): #This line calls a function according to id of a particular item.
        AllDownloads()

def AllDownloads():
    print("All Downloads")



if__name__="__main__"

win=Tk()

win.geometry("500x500")
win.configure(background="lightblue")
win.title("Tree View")
win.resizable(0,0)

treeView=ttk.Treeview(win)
treeView.place(x=0,y=0,width=500,height=500)

photo=PhotoImage(file='download.png')

#First parameter is Parent id under which we want to add the Child
#2nd parameter is the position under the parent where we want to add child("end" specify the last position)
#3rd Parameter is the id of child which we have added(we can give any id to child for use in future like as Parent if we want to add child under it)
#4th Parameter is the text which is to be shown as child.
#"image" specify the logo for the item.
treeView.insert('','0','child1',text='All Downloads',image=photo)
treeView.insert('child1','0','item1.2',text='Compressed')
treeView.insert('child1','1','item1.3',text='Documents')
treeView.insert('child1','2','item1.4',text='Music')
treeView.insert('child1','3','item1.5',text='Programs')
treeView.insert('child1','end','item1.6',text='Videos')


treeView.insert('','end','child2',text='Grabber Projects')
treeView.insert('child2','0','child2.1',text='Queues')
treeView.insert('child2.1','0','child2.1.1',text='Main Queue')
treeView.insert('child2.1','end','child2.1.2',text='Sync Queue')



treeView.move('child2.1.2','child2','end')
#"move" moves an item from one parent to another Parent.
#First Parameter specify the id of child which we want to move.
#2nd Parameter specify the id of parent under which we want to move the item.
#3rd Parameter specify the position under the specified parent where we want to add the item.


treeView.detach('child2.1.2')
#"detach" vanish the specified item but it still exists and can be shown or moves using "move" function.

treeView.delete('child2.1.2')
#"delete" deletes the specified item permanentaly.




                #### Columns  ####

treeView.config(columns=('Version'))#This line creates a new column whose id id "Version".(We can change id according to our choice)

treeView.column('Version',width=50,anchor='center')#This line sets attributes of column which we have created.First parameter is the column id which we have specify.
#Other parameters are used to set the attributes of our column.

treeView.heading('Version',text='Versions')#This Line sets the name of Column.First parameter is the column id which we have specify.
#2nd Attribute is used to specify the name of Column.

treeView.set('child2.1.1','Version','1.0')  #This Line is used to specify column value for a particular item in the Tree View.
#First parameter is the id of item for which we want to specify the value of column.
#2nd Parameter is id of Column under which we want to specify the column value for specified Item.
#3rd Parameter is the Column Value for the specified item.


            ### Formatting of Items ###

treeView.item('child2.1.1',tags=('item2.1.1'))  #This Line add tags in the Item.(Multiple tags can be specified separating them by comma)
#First parameter is the id of item for which we want to specify the tags.

treeView.tag_configure('item2.1.1',background='green',foreground='white')#This line apply formatting on the Item
#First parametr is the tag name which we have specified for the item on which we want to apply formatting.
#Other Parameters are used for formatting.

            ### Call a function on selecting the Item ###

treeView.bind('<<TreeviewSelect>>',callback)  #this Line call the specified function(e.g callback) when we select an item.
#and send id of that item to the function but not in string form.

treeView.config(selectmode='browse')#this line specify that user can only select one item at a time.

treeView.selection_add('item1.2') #This line automatically selects the item.(Parameter is the id of auto selected item)
treeView.selection_add('item1.3')

treeView.selection_remove('item1.2')#This line automatically un-select the item.(Parameter is the id of auto un-selected item)



win.mainloop()
