import tkinter as tk

class MyClass:
    call_count =0
    def words(): 
        MyClass.call_count += 1
        words100 =[
        {"Spanish": "el", "English": "the"},
        {"Spanish": "de", "English": "of"},
        {"Spanish": "que", "English": "that"},
        {"Spanish": "y", "English": "and"},
        {"Spanish": "a", "English": "to"},
        {"Spanish": "en", "English": "in"},
        {"Spanish": "un", "English": "a"},
        {"Spanish": "ser", "English": "to be"},
        {"Spanish": "se", "English": "oneself"},
        {"Spanish": "no", "English": "no"},
        {"Spanish": "haber", "English": "to have"},
        {"Spanish": "por", "English": "for"},
        {"Spanish": "con", "English": "with"},
        {"Spanish": "para", "English": "for"},
        {"Spanish": "como", "English": "like"},
        {"Spanish": "estar", "English": "to be"},
        {"Spanish": "tener", "English": "to have"},
        {"Spanish": "lo", "English": "it"},
        {"Spanish": "pero", "English": "but"},
        {"Spanish": "más", "English": "more"},
        {"Spanish": "hacer", "English": "to do"},
        {"Spanish": "o", "English": "or"},
        {"Spanish": "ese", "English": "that"},
        {"Spanish": "sí", "English": "yes"},
        {"Spanish": "su", "English": "his/her/their"},
        {"Spanish": "al", "English": "to the"},
        {"Spanish": "del", "English": "of the"},
        {"Spanish": "se", "English": "oneself"},
        {"Spanish": "las", "English": "the (feminine plural)"},
        {"Spanish": "en", "English": "in"},
        {"Spanish": "este", "English": "this"},
        {"Spanish": "ya", "English": "already"},
        {"Spanish": "ver", "English": "to see"},
        {"Spanish": "porque", "English": "because"},
        {"Spanish": "dar", "English": "to give"},
        {"Spanish": "cuando", "English": "when"},
        {"Spanish": "él", "English": "he"},
        {"Spanish": "muy", "English": "very"},
        {"Spanish": "sin", "English": "without"},
        {"Spanish": "vez", "English": "time (instance)"},
        {"Spanish": "mucho", "English": "much/many"},
        {"Spanish": "saber", "English": "to know"},
        {"Spanish": "qué", "English": "what"},
        {"Spanish": "sobre", "English": "on/about"},
        {"Spanish": "mi", "English": "my"},
        {"Spanish": "alguno", "English": "some"},
        {"Spanish": "nos", "English": "us"},
        {"Spanish": "ir", "English": "to go"},
        {"Spanish": "me", "English": "me"},
        {"Spanish": "tú", "English": "you (informal)"},
        {"Spanish": "te", "English": "you (informal)"},
        {"Spanish": "él", "English": "he"},
        {"Spanish": "ella", "English": "she"},
        {"Spanish": "ellos", "English": "they (masculine)"},
        {"Spanish": "ellas", "English": "they (feminine)"},
        {"Spanish": "nosotros", "English": "we"},
        {"Spanish": "vosotros", "English": "you all (informal)"},
        {"Spanish": "usted", "English": "you (formal)"},
        {"Spanish": "ustedes", "English": "you all (formal)"},
        {"Spanish": "uno", "English": "one"},
        {"Spanish": "dos", "English": "two"},
        {"Spanish": "tres", "English": "three"},
        {"Spanish": "cuatro", "English": "four"},
        {"Spanish": "cinco", "English": "five"},
        {"Spanish": "seis", "English": "six"},
        {"Spanish": "siete", "English": "seven"},
        {"Spanish": "ocho", "English": "eight"},
        {"Spanish": "nueve", "English": "nine"},
        {"Spanish": "diez", "English": "ten"},
        {"Spanish": "aquí", "English": "here"},
        {"Spanish": "ahí", "English": "there"},
        {"Spanish": "allí", "English": "there (distant)"},
        {"Spanish": "quién", "English": "who"},
        {"Spanish": "qué", "English": "what"},
        {"Spanish": "cuál", "English": "which"},
        {"Spanish": "dónde", "English": "where"},
        {"Spanish": "por qué", "English": "why"},
        {"Spanish": "cómo", "English": "how"},
        {"Spanish": "cuándo", "English": "when"},
        {"Spanish": "cuánto", "English": "how much"},
        {"Spanish": "qué", "English": "what"},
        {"Spanish": "este", "English": "this"},
        {"Spanish": "ese", "English": "that"},
        {"Spanish": "aquel", "English": "that (over there)"},
        {"Spanish": "quien", "English": "who"},
        {"Spanish": "cual", "English": "which"},
        {"Spanish": "mismo", "English": "same"},
        {"Spanish": "nuevo", "English": "new"},
        {"Spanish": "bueno", "English": "good"},
        {"Spanish": "mejor", "English": "better"},
        {"Spanish": "peor", "English": "worse"},
        {"Spanish": "primero", "English": "first"},
        {"Spanish": "último", "English": "last"}
        ]
        i = (MyClass.call_count)-1
        word=words100[i]
        wordDisplay= words100[i+1]
        wordSpa=wordDisplay['Spanish']
        wordEng=word['English']
        text= tk.Label(mainframe, text=f'What is {wordSpa} in English?', background='beige')
        text.grid(row=2,column=30)
        MyClass.begin(wordEng)
        
    def begin(Eng):
        Ans = entry.get()
        Y0rN = MyClass.YesorNo(Eng, Ans)
        if Y0rN == 'true':
            kk= tk.Label(mainframe, text='Correct')
            kk.grid(row=2,column =2)
            kk.after(1000, kk.destroy)
            entry.delete(0, 'end')
            
        else: 
            kk= tk.Label(mainframe, text='False')
            kk.grid(row=2,column =2)
            kk.after(1000, kk.destroy)
            entry.delete(0, 'end')
            

            cc= tk.Label(mainframe, text=f'The correct answer is: {Eng}', font= 20)
            cc.grid(row=10,column =2)
            cc.after(3000, cc.destroy)


    def YesorNo(Eng, Ans):
        if Eng == Ans:
            return 'true'
        else: 
            return 'false'

def Enter(event=None):
    button.invoke()


root = tk.Tk()
root.title("Spanish Learning App")
root.geometry('500x500')
mainframe = tk.Frame(root, background="beige")
mainframe.pack(fill='both',expand=True)
text = tk.Label(mainframe,text='Welcome to Spanish 101', background='beige', font=('Times New Roman', 30))
text.grid(row=0, column=30, padx=100)

text= tk.Label(mainframe, text=f'What is el in English?', background='beige')
text.grid(row=2,column=30,)

entry = tk.Entry(root, width=50)
entry.pack()

button= tk.Button(root, text='Enter your Answer:',command=MyClass.words)
button.pack()
root.bind('<Return>', Enter)


root.mainloop()





