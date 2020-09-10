# BSSD Homework 4.1
# Scott Bing
# Text Manipulation

from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageDraw, ImageTk
from tkinter import ttk
import tkinter.font as font
import string
import re

cResults = None

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

def process(params):
    storyFiles = ["alice.txt", "peter_rabbit.txt", "the_bible.txt", "time_machine.txt", "two_cities.txt"]

    books = {
        'alice.txt' 		 : 'Alice Through the Looking Glass',
        'peter_rabbit.txt'   : 'Peter Rabbit',
        'the_bible.txt'  	 : 'King James Bible',
        'time_machine.txt'	 : 'The Time Machine',
        'two_cities.txt'  	 : 'A Tale of Two Cities'
    }

    for i in range(len(params)):
        if params[i] == 1:
            #fileName = storyFiles[i]
            print("list(books.keys())[i]", list(books.keys())[i])
            fileName = list(books.keys())[i]
            print("fileNamee = ", fileName)
            print("Statistics For: ",books[fileName])
            results(fileName)


def results(fileName):
    global cResults

    app = Application(self)

    unique_words = {}  # dictionary for word counts
    words = process_file(fileName, "utf-8")
    words_to_dict(words, unique_words)

    cResults.delete(1.0, END)
    cResults.insert(END, "Found {0} total words.".format(len(words)))
    cResults.pack()

    print("Found {0} total words.".format(len(words)))
    print("Found {0} unique words.".format(len(unique_words.keys())))
    print("Raw TTR: ", len(unique_words.keys()) / len(words))
    print("Pct TTR: ", str(round((len(unique_words.keys()) / len(words)) * 100)) + "%")


class Application(Frame):
    """ GUI application that creates a story based on user input. """

    def __init__(self, master):
        """ Initialize Frame. """
        super(Application, self).__init__(master)

        self.grid()
        self.create_widgets()

    def search(self):
        pass

    def getStates(self):

        # print("is_alice is", int(self.is_alice.get()))
        # print("is_peter is", int(self.is_peter.get()))
        # print("is_bible is", int(self.is_bible.get()))
        # print("is_time is", int(self.is_time.get()))
        # print("is_cities is", int(self.is_cities.get()))

        params = (int(self.is_alice.get()),
                  int(self.is_peter.get()),
                  int(self.is_bible.get()),
                  int(self.is_time.get()),
                  int(self.is_cities.get()))

        print(params)

        process(params)

        # print(list(int(self.is_alice.get())),
        #       (int(self.is_peter.get())),
        #       (int(self.is_bible.get())),
        #       (int(self.is_time.get())),
        #       (int(self.is_cities.get())))

    def create_widgets(self):
        """ Create widgets to get story information and to display story. """

        #set up button fonts
        btnFont = font.Font(weight="bold")
        btnFont = font.Font(size=16)

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
                    ).grid(row=3, column=0, sticky=W, pady=3)

        # create vertical check button
        self.is_peter = BooleanVar()
        Checkbutton(self,
                    text=self.stories[1],
                    variable=self.is_peter,
                    font=("Helvetica", 12)
                    ).grid(row=4, column=0, sticky=W, pady=3)

        # create vertical check button
        self.is_bible = BooleanVar()
        Checkbutton(self,
                    text=self.stories[2],
                    variable=self.is_bible,
                    font=("Helvetica", 12)
                    ).grid(row=5, column=0, sticky=W, pady=3)

        # create vertical check button
        self.is_time = BooleanVar()
        Checkbutton(self,
                    text=self.stories[3],
                    variable=self.is_time,
                    font=("Helvetica", 12)
                    ).grid(row=6, column=0, sticky=W, pady=3)

        # create vertical check button
        self.is_cities = BooleanVar()
        Checkbutton(self,
                    text=self.stories[4],
                    variable=self.is_cities,
                    font=("Helvetica", 12)
                    ).grid(row=7, column=0, sticky=W, pady=7)

        # create a the generate button
        Button(self,
               text="Compare",
               command=self.getStates,
               font=btnFont).grid(row=8, column=0, sticky=W)

        # set up mad lib story frame
        compareframe = LabelFrame(self,
                                  text="Compare Results"
                                  ).grid(row=9, column=0, sticky=W)
        cResults = Text(compareframe,
                        height=10,
                        width=50,
                        wrap=WORD,
                        state=NORMAL)


        ttk.Separator(self).grid(row=10, column=0, columnspan=99, sticky=EW, pady=7)

        Label(self,
              text="Choose one story above to search",
              font=("Helvetica", 14)
              ).grid(row=11, column=0, sticky=W, pady=3)

        Label(self,
              text="Enter Search Word: ",
              font=("Helvetica", 12)
              ).grid(row=12, column=0, sticky=W, pady=3)

        Entry(self,
              width=40
              ).grid(row=12, column=0, sticky=E, pady=3)

        # create a the generate button
        Button(self,
               text="Search",
               command=self.search,
               font=btnFont).grid(row=13, column=0, sticky=E)




# main
def main():
    root = Tk()
    root.title("BSSD 5410 Homework 4.1 Scott Bing")
    app = Application(root)


    root.mainloop()

if __name__ == "__main__":
    main()