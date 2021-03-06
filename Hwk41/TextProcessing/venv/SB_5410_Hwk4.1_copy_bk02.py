# BSSD Homework 4.1
# Scott Bing
# Text Manipulation

from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageDraw, ImageTk
import tkinter.font as font
import string
import re

def process_file(fname, enc):
    #open file for 'r'eading
    with open(fname, 'r', encoding=enc) as file:
        dat = file.read()   #read file
        dat = perform_re(dat)
    return(dat.split())  #return read data
#end process_file(fname, enc):

def write_results(fname, data, enc):
    #open file for 'w'riting
    with open(fname, 'w', encoding = enc) as file:
        file.write(data)
#end def write_results(fname, data, enc):

def words_to_dict(all_words, dictionary):
    for w in all_words: #for each word
        w = clean_word((w))
        if w in dictionary:  #if the word was counted before
            dictionary[w] += 1  #increment te count
        else:
            dictionary[w] = 1   #begin count for a new word
#end def word_to_dict(all_words, dictionary):

def clean_word(word):
    for p in string.punctuation:
        word = word.replace(p, "")
    return word.lower() #return the word as lowercase
#end def clean_word(word):

def perform_re(text):
    text = re.sub(r'(CHAPTER) ([IVXLC]+.)', '\\1\\2', text)
    return text






class Application(Frame):
    """ GUI application that creates a story based on user input. """

    def __init__(self, master):
        """ Initialize Frame. """
        super(Application, self).__init__(master)

        self.grid()
        self.create_widgets()


    def create_widgets(self):
        """ Create widgets to get story information and to display story. """

        self.stories = ["Alice Through the Looking Glass",
                   "Peter Rabit",
                   "King James Bible",
                   "The Time Machine",
                   "A Tale of Two Cities"]

        Label(self,
              text="Hwk 4.1 - Text Comparison Application",
              font=("Helvetica", 16, 'bold'),
              highlightbackground='#3E4149',
              ).grid(row=0, column=0, sticky=W, pady=4)

        Label(self,
                    text="Choose two stories to compare:",
                    font=("Helvetica", 14)
                    ).grid(row=1, column=0, sticky=W, pady=4)

        # create vertical check button
        self.is_alice = BooleanVar()
        Checkbutton(self,
                    text=self.stories[0],
                    variable=self.is_alice,
                    font=("Helvetica", 12)
                    ).grid(row=2, column=0, sticky=W, pady=3)

        # create vertical check button
        self.is_peter = BooleanVar()
        Checkbutton(self,
                    text=self.stories[1],
                    variable=self.is_peter,
                    font=("Helvetica", 12)
                    ).grid(row=3, column=0, sticky=W, pady=3)

        # create vertical check button
        self.is_bible = BooleanVar()
        Checkbutton(self,
                    text=self.stories[2],
                    variable=self.is_bible,
                    font=("Helvetica", 12)
                    ).grid(row=4, column=0, sticky=W, pady=3)

        # create vertical check button
        self.is_time = BooleanVar()
        Checkbutton(self,
                    text=self.stories[3],
                    variable=self.is_time,
                    font=("Helvetica", 12)
                    ).grid(row=5, column=0, sticky=W, pady=3)

        # create vertical check button
        self.is_cities = BooleanVar()
        Checkbutton(self,
                    text=self.stories[4],
                    variable=self.is_cities,
                    font=("Helvetica", 12)
                    ).grid(row=6, column=0, sticky=W, pady=7)

        Label(self,
              text="Results:",
              font=("Helvetica", 14)
              ).grid(row=7, column=0, sticky=W, pady=4)

        # set up orginal story frame
        self.results_frame = LabelFrame(self,
                   text="Results",
                   font=("Helvetica", 14)
                   ).grid(row=8, column=0, sticky=W, pady=4)

        self.results_frame = Text(self.results_frame,
             #text = "Some Text",
             height=10,
             width=50,
             wrap=WORD)
        Text(self.results_frame.grid(row=8, column=0, sticky=W, pady=4))

        btnFont = font.Font(weight="bold")
        btnFont = font.Font(size=20)

        # create a the generate button
        Button(self,
               text="Generate",
               command=self.getStates,
               # bg='blue',
               # fg='#ffffff',
               highlightbackground='#3E4149',
               font=btnFont).grid(row=9, column=0, sticky=NSEW)

        # Button(self,
        #       text="Search:",
        #       font=("Helvetica", 14)
        #       ).grid(row=10, column=0, sticky=W, pady=4)
        #
        # searchToken = Entry(self,
        #       text="Search:",
        #       font=("Helvetica", 14)
        #       ).grid(row=10, column=0, sticky=E, pady=4)

        # first setup two StringVars. They will be linked to a Label and an Entry widget.
        # we should keep a reference to these two StringVars, because we will call their method
        # to read/write widget content.
        self.msg2show = StringVar()
        self.searchToken = StringVar()

        # this is a fixed Label widget whose display will no change.
        # No need to keep a reference(meaning to assign it to a variable).
        Label(self, text='Select a story above and enter a search word.').grid(row=11, column=0, sticky=W, pady=4)

        # this is a variable Entry widget whose content is saved into `self.searchToken`
        Entry(self, textvariable=self.searchToken).grid(row=12, column=0, sticky=W, pady=4)

        # this is the button who will trigger `self.search` on click.
        Button(self, text='Search', command=self.getStates).grid(row=13, column=0, sticky=W, pady=4)

        # this is a variable Label widget whose display is decided by the linked variable `self.msg2show`
        Label(self, textvariable=self.msg2show).grid(row=14, column=0, sticky=W, pady=4)

    def search(self, fileName):
        #self.msg2show = StringVar()
        # get out what in the Entry widget through calling the `get()` method of `self.searchToken`
        search_token = self.searchToken.get()
        # and print it into console, for checking.
        print(search_token)
        
        unique_words = {}  # dictionary for word counts
        words = process_file("peter_rabbit.txt", "utf-8")
        words_to_dict(words, unique_words)

        print("Found {0} unique words.".format(len(unique_words.keys())))
        print("Here are a few: ")
        print(list(unique_words.keys())[:5])  # print first few unique words
        result = unique_words.get('python', 0)
        print("Python appears {0} times in the text.".format(result))

        srch_str = search_token
        if srch_str in unique_words.keys():
            print("down appears {0} times in the text.".format(unique_words[srch_str]))
        else:
            print(srch_str, "not in text.")
            # this is a variable Label widget whose display is decided by the linked variable `self.msg2show`
            Label(self, textvariable=self.msg2show).grid(row=14, column=0, sticky=W, pady=4)


        # then we set that text into self.msg2show, and since it is linked with the variable Label widget
        # the display of that Label will then be set to search_token.
        self.msg2show.set(search_token)

        # You can see here I print the `search_token` to console as well as to a Label.
        # You can do it in the same way.
        
    
    def getStates(self):
        # process file selections
        params = (int(self.is_alice.get()),
                  int(self.is_peter.get()),
                  int(self.is_bible.get()),
                  int(self.is_time.get()),
                  int(self.is_cities.get()))

        print(params)

        # process the files
        self.process(params)

    def process(self, params):
        #storyFiles = ["alice.txt", "peter_rabbit.txt", "the_bible.txt", "time_machine.txt", "two_cities.txt"]
        #setup dictionar of books
        books = {
            'alice.txt' : 'Alice Through the Looking Glass',
            'peter_rabbit.txt'   : 'Peter Rabbit',
            'the_bible.txt'  	 : 'King James Bible',
            'time_machine.t'	 : 'The Time Machine',
            'two_cities.txt'  	 : 'A Tale of Two Cities'
        }

        for i in range(len(params)):
            if params[i] == 1:
                # fileName = storyFiles[i]
                # print("list(books.keys())[i]", list(books.keys())[i])
                fileName = list(books.keys())[i]
                # print("fileNamee = ", fileName)
                print("\nStatistics For:   " ,books[fileName])
                #results(fileName)
                self.search(fileName)

    def results(fileName):
        unique_words = {}  # dictionary for word counts
        words = process_file(fileName, "utf-8")
        words_to_dict(words, unique_words)

        print("Found {0} total words.".format(len(words)))
        print("Found {0} unique words.".format(len(unique_words.keys())))
        # print("Here are a few: ")
        # print(list(unique_words.keys())[:5])    #print first few unique words
        # result = unique_words.get('python', 0)
        # print("Python appears {0} times in the text.".format(result))

        # srch_str = 'down'
        # if srch_str in unique_words.keys():
        #     print("down appears {0} times in the text.".format(unique_words[srch_str]))
        # else:
        #     print(srch_str, "not in text.")

        print("Raw TTR: ", len(unique_words.keys()) / len(words))
        print("Pct TTR: ", str(round((len(unique_words.keys()) / len(words)) * 100)) + "%")

        # join the words in the list with new line char
        # write_results("perline.txt", "\n".join(words), "utf-8")



# main
def main():
    root = Tk()
    root.title("BSSD 5410 Homework 4.1 Scott Bing")
    app = Application(root)


    root.mainloop()

if __name__ == "__main__":
    main()