from tkinter import *
from tkinter.ttk import *


class MainPanel(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)

        # first setup two StringVars. They will be linked to a Label and an Entry widget.
        # we should keep a reference to these two StringVars, because we will call their method
        # to read/write widget content.
        self.msg2show = StringVar()
        self.text_input = StringVar()

        # this is a fixed Label widget whose display will no change.
        # No need to keep a reference(meaning to assign it to a variable).
        Label(self, text='If you click the button, the text in the entry widget will show above.').pack()

        # this is a variable Label widget whose display is decided by the linked variable `self.msg2show`
        Label(self, textvariable=self.msg2show).pack()

        # this is a variable Entry widget whose content is saved into `self.text_input`
        Entry(self, textvariable=self.text_input).pack()

        # this is the button who will trigger `self.set_msg` on click.
        Button(self, text='Set message', command=self.set_msg).pack()

    def set_msg(self):
        # get out what in the Entry widget through calling the `get()` method of `self.text_input`
        text_in_entry_widget = self.text_input.get()
        # and print it into console, for checking.
        print(text_in_entry_widget)

        # then we set that text into self.msg2show, and since it is linked with the variable Label widget
        # the display of that Label will then be set to text_in_entry_widget.
        self.msg2show.set(text_in_entry_widget)

        # You can see here I print the `text_in_entry_widget` to console as well as to a Label.
        # You can do it in the same way.

if __name__ == '__main__':
    root = Tk()
    MainPanel(root).pack()
    root.mainloop()