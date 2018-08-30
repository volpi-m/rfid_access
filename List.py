from Page import *
import tkinter.ttk as ttk


class List(Page):

    """Page where all the presents users are listed"""

    def __init__(self, *args, **kwargs):
        global listbox, var_add, var_del, combo
        Page.__init__(self, *args, **kwargs)

        # Init invisible frame to place correctly the list
        fr1 = tk.Frame(self, width=1, height=50)
        fr1.grid(row=0, column=1)
        fr2 = tk.Frame(self, width=50, height=1)
        fr2.grid(row=1, column=0)

        # Init scrollable list
        scroll = tk.Scrollbar(self, orient=tk.VERTICAL)
        scroll.grid(row=1, column=2, sticky=tk.NS, rowspan=50)
        listbox = tk.Listbox(self, yscrollcommand=scroll.set, width=50, height=16, font=BIG_FONT)
        listbox.bind('<<ListboxSelect>>', self.selection)
        listbox.grid(row=1, column=1, rowspan=50)
        scroll.config(command=listbox.yview)

        # Init invisible frames to place in the grid
        fr3 = tk.Frame(self, width=20, height=1)
        fr3.grid(row=1, column=3)
        fr4 = tk.Frame(self, width=1, height=15)
        fr4.grid(row=3, column=4)
        fr5 = tk.Frame(self, width=1, height=25)
        fr5.grid(row=5, column=4)
        fr6 = tk.Frame(self, width=1, height=15)
        fr6.grid(row=8, column=4)

        # Init labels
        label_add = tk.Label(self, text="Ajouter un élève à la liste", font=BIG_FONT)
        label_del = tk.Label(self, text="Retirer un élève de la liste", font=BIG_FONT)

        # Init var for entry
        var_add = tk.StringVar()
        var_del = tk.StringVar()

        # Init entry
        combo = ttk.Combobox(self, width=19, font=BIG_FONT, textvariable=var_add)
        entry_del = tk.Entry(self, textvariable=var_del, font=BIG_FONT)

        # Init buttons to interact with the list
        button_add = tk.Button(self, text="Ajouter", font=BIG_FONT, command=lambda: self.add_to_list(self))
        button_del = tk.Button(self, text="Retirer", font=BIG_FONT, command=self.del_from_list)

        # Setup widgets on the screen
        label_add.grid(row=1, column=4)
        combo.grid(row=2, column=4)
        button_add.grid(row=4, column=4)
        label_del.grid(row=6, column=4)
        entry_del.grid(row=7, column=4)
        button_del.grid(row=9, column=4)

        new_order = (combo, button_add, entry_del, button_del)
        for w in new_order:
            w.lift()

    def lift_list(self):
        bdd = Page.get_bdd(self)
        first, last = bdd.get_names()
        i = 1
        values = []
        while i < len(first):
            values.append(first[i][0] + " " + last[i][0])
            i += 1
        combo.config(values=values)
        self.lift()

    @staticmethod
    def add_to_list(self):
        name = var_add.get()
        listbox.insert(tk.END, name)

    @staticmethod
    def del_from_list():
        to_del = var_del.get()
        size = listbox.size()
        list_values = listbox.get(0, size)
        i = 0
        while i < size:
            if list_values[i] == to_del:
                listbox.delete(i)
                break
            i += 1

    @staticmethod
    def selection(self):
        try:
            print(listbox.get(listbox.curselection()))
        except tk.TclError:
            pass