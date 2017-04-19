from tkinter import *
import bookprovider

def clear_list():
    book_list.delete(0, END)

def populate_fields(event):
    global selected_book_id

    book_index = book_list.curselection()[0]
    selected_book = book_list.get(book_index)
    selected_book_id = selected_book[0]

    title_value.set(selected_book[1])
    author_value.set(selected_book[2])
    year_value.set(selected_book[3])
    isbn_value.set(selected_book[4])

def populate_list():
    clear_list()
    for row in bookprovider.view_all():
        book_list.insert(END, row)

def search_book():
    clear_list()
    for row in bookprovider.search(title_value.get(), author_value.get(), year_value.get(), isbn_value.get()):
        book_list.insert(END, row)

def add_book():
    bookprovider.insert(title_value.get(), author_value.get(), year_value.get(), isbn_value.get())
    search_book()

def delete_book():
    bookprovider.delete(selected_book_id)

    populate_list()

def update_book():
    bookprovider.update(selected_book_id, title_value.get(), author_value.get(), year_value.get(), isbn_value.get())
    populate_list()

window = Tk()
window.wm_title("BookStore")

title_label = Label(window, text="Title")
title_label.grid(row=0, column=0)

author_label = Label(window, text="Author")
author_label.grid(row=0, column=2)

year_label = Label(window, text="Year")
year_label.grid(row=1, column=0)

isbn_label = Label(window, text="ISBN")
isbn_label.grid(row=1, column=2)

title_value = StringVar()
title_entry = Entry(window, textvariable=title_value)
title_entry.grid(row=0, column=1)

author_value = StringVar()
author_entry = Entry(window, textvariable=author_value)
author_entry.grid(row=0, column=3)

year_value = StringVar()
year_entry = Entry(window, textvariable=year_value)
year_entry.grid(row=1, column=1)

isbn_value = StringVar()
isbn_entry = Entry(window, textvariable=isbn_value)
isbn_entry.grid(row=1, column=3)

book_list = Listbox(window, height=6, width=35)
book_list.grid(row=2, column=0, rowspan=6, columnspan=2)

book_scroll = Scrollbar(window)
book_scroll.grid(row=2, column=2, rowspan=6)

book_list.configure(yscrollcommand=book_scroll.set)
book_scroll.configure(command=book_list.yview)
book_list.bind('<<ListboxSelect>>', populate_fields)

view_button = Button(window, text="View all", width=12, command=populate_list)
view_button.grid(row=2, column=3)

search_button = Button(window, text="Search entry", width=12, command=search_book)
search_button.grid(row=3, column=3)

add_button = Button(window, text="Add entry", width=12, command=add_book)
add_button.grid(row=4, column=3)

update_button = Button(window, text="Update entry", width=12, command=update_book)
update_button.grid(row=5, column=3)

delete_button = Button(window, text="Delete entry", width=12, command=delete_book)
delete_button.grid(row=6, column=3)

close_button = Button(window, text="Close", width=12, command=window.destroy)
close_button.grid(row=7, column=3)

window.mainloop()
