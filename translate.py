import googletrans
from tkinter import *
translator = googletrans.Translator()

#! Functions And Class ==>
class BaseFrame:
    def __init__(self, master):
        def clip():
            master.clipboard_clear()
            master.clipboard_append(translator.translate(self.box.get(1.0, END), self.var.get()).text)
        master = Frame(master)
        frame1 = LabelFrame(master, text="Enter Your Text")
        frame1.pack()
        self.box = Text(frame1, width=100, height=10)
        self.box.pack(fill=BOTH)
        frame2 = LabelFrame(master, text="Enter Language")
        frame2.pack()
        self.var = StringVar()
        self.var.set("fa")
        w = OptionMenu(frame2, self.var, "en", "fa",'af', 'sq', 'am', 'ar', 'hy', 'az', 'eu', 'be', 'bn', 'bs', 'bg', 'ca', 'ny', 'co', 'hr', 'cs', 'da', 'nl', 'en', 'eo', 'et', 'tl', 'fi', 'fr', 'fy', 'gl', 'ka', 'de', 'el', 'gu', 'ht', 'ha', 'iw', 'he', 'hi', 'hu', 'is', 'ig', 'id', 'ga', 'it', 'ja', 'jw', 'kn', 'kk', 'km', 'ko', 'ku', 'ky', 'lo', 'la', 'lv', 'lt', 'lb', 'mk', 'mg', 'ms', 'ml', 'mt', 'mi', 'mr', 'mn', 'my', 'ne', 'no', 'or', 'ps', 'fa', 'pl', 'pt', 'pa', 'ro', 'ru', 'sm', 'gd', 'sr', 'st', 'sn', 'sd', 'si', 'sk', 'sl', 'so', 'es', 'su', 'sw', 'sv', 'tg', 'ta', 'te', 'th', 'tr', 'uk', 'ur', 'ug', 'uz', 'vi', 'cy', 'xh', 'yi', 'yo', 'zu')
        w.pack()
        Button(master, text="Translate", command=self.translate).pack()
        frame3 = LabelFrame(master, text="Submit")
        frame3.pack()
        self.result = Text(frame3, width=100, height=10)
        self.result.pack(fill=BOTH)
        Button(master, text="Copy", command=clip).pack()
        Button(master, text="Clean Page", command=self.clear).pack()
        master.pack(fill=BOTH)
    def translate(self):
        self.result.delete(1.0, END)
        self.result.insert(END, translator.translate(self.box.get(1.0, END), self.var.get()).text)
    def clear(self):
        self.result.delete(1.0, END)
        self.box.delete(1.0, END)

def Starter():
    if __name__ == '__main__':
        root = Tk()
        root.title("MrFeri")
        BaseFrame(root)
        root.mainloop()

Starter()