import tkinter as tk
from tkinter import filedialog, ttk
from tkinter import messagebox
import os
from tkcalendar import DateEntry
from typing import Any
from datetime import date


state_holder: dict[str, Any] = {
    'semester_files_count': None,
    'semester_files_paths': None,
    'diploma_file_path': None,
    'template_file_path': None,
    'save_directory_path': None,
    'speciality_name': None,
    'speciality_code': None,
    'speciality_area_name': None,
    'speciality_area_code': None,
    'start_date': date.today(),
    'end_date': date.today(),
    'statement_date': date.today(),
}

GRID_COLUMNS_COUNT = 4
SEMESTER_COUNT_COMBOBOX_VALUES = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10')


def on_semester_count_combobox_selected(
        semester_count_combobox: ttk.Combobox,
) -> None:
    global state_holder
    files_count = int(semester_count_combobox.get())
    state_holder['semester_files_count'] = files_count


def push_semester_files_button(
        semester_files_listbox: tk.Listbox,
        semester_files_button_up: tk.Button,
        semester_files_button_down: tk.Button,
) -> None:
    global state_holder
    file_paths = filedialog.askopenfilenames(
        title='Выберите файлы зачётно-экзаменационных ведомостей',
        filetypes=[(
            "Файлы Excel",
            "*.xlsx"
        ), ]

    )
    if len(file_paths) != 0:
        if not all(os.path.exists(file_path) for file_path in file_paths):
            messagebox.showerror(
                title='Ошибка',
                message='Одного или нескольких выбранных файлов не существует!'
            )
            return

        state_holder['semester_files_paths'] = list(file_paths)
        semester_files_listbox.config(state=tk.NORMAL)
        semester_files_listbox.delete(0, tk.END)
        for file_path in file_paths:
            semester_files_listbox.insert(tk.END, file_path)
        semester_files_button_up.config(state=tk.NORMAL)
        semester_files_button_down.config(state=tk.NORMAL)


def push_semester_files_button_up(
        semester_files_listbox: tk.Listbox,
) -> None:
    global state_holder
    selected_indeces = semester_files_listbox.curselection()
    if not selected_indeces:
        return

    selected_index = selected_indeces[0]
    if selected_index == 0:
        return

    selected_file_path = state_holder['semester_files_paths'][selected_index]
    semester_files_listbox.delete(selected_index)
    semester_files_listbox.insert(
        selected_index-1,
        selected_file_path
    )
    semester_files_listbox.selection_set(selected_index-1)

    state_holder['semester_files_paths'][selected_index], state_holder['semester_files_paths'][selected_index - 1] \
        = state_holder['semester_files_paths'][selected_index - 1], state_holder['semester_files_paths'][selected_index]


def push_semester_files_button_down(
        semester_files_listbox: tk.Listbox,
) -> None:
    global state_holder
    selected_indeces = semester_files_listbox.curselection()
    if not selected_indeces:
        return

    selected_index = selected_indeces[0]
    if selected_index == (semester_files_listbox.size() - 1):
        return

    selected_file_path = state_holder['semester_files_paths'][selected_index]
    semester_files_listbox.delete(selected_index)
    semester_files_listbox.insert(
        selected_index + 1,
        selected_file_path
    )
    semester_files_listbox.selection_set(selected_index + 1)

    state_holder['semester_files_paths'][selected_index], state_holder['semester_files_paths'][selected_index + 1] \
        = state_holder['semester_files_paths'][selected_index + 1], state_holder['semester_files_paths'][selected_index]


def push_diplomas_file_button(
        diploma_files_text: tk.Text,
) -> None:
    global state_holder
    file_path = filedialog.askopenfilename(
        title='Выберите файл с темами дипломных проектов',
        filetypes=[(
            "Файл Excel",
            "*.xlsx"
        ), ]
    )
    if file_path != '':
        if not os.path.exists(file_path):
            messagebox.showerror(
                title='Ошибка',
                message='Выбранного файла не существует!'
            )
            return

        state_holder['diploma_file_path'] = file_path
        diploma_files_text.config(state=tk.NORMAL)
        diploma_files_text.delete('1.0', tk.END)
        diploma_files_text.insert(
            '1.0',
            state_holder['diploma_file_path']
        )
        diploma_files_text.config(state=tk.DISABLED)


def push_template_file_button(
        template_file_text: tk.Text,
) -> None:
    global state_holder
    file_path = filedialog.askopenfilename(
        title='Выберите файл шаблона выписки',
        filetypes=[(
            "Файл Excel",
            "*.xlsx"
        ), ]
    )
    if file_path != '':
        if not os.path.exists(file_path):
            messagebox.showerror(
                title='Ошибка',
                message='Выбранного файла не существует!'
            )
            return

        state_holder['template_file_path'] = file_path
        template_file_text.config(state=tk.NORMAL)
        template_file_text.delete('1.0', tk.END)
        template_file_text.insert(
            '1.0',
            state_holder['template_file_path']
        )
        template_file_text.config(state=tk.DISABLED)


def push_save_directory_button(
        save_directory_text: tk.Text,
) -> None:
    global state_holder
    directory_path = filedialog.askdirectory(
        title='Выберите директорию сохранения выписок'
    )
    if directory_path != '':
        if not os.path.exists(directory_path):
            messagebox.showerror(
                title='Ошибка',
                message='Выбранной директории не существует!'
            )
            return

        state_holder['save_directory_path'] = directory_path
        save_directory_text.config(state=tk.NORMAL)
        save_directory_text.delete('1.0', tk.END)
        save_directory_text.insert(
            '1.0',
            state_holder['save_directory_path']
        )
        save_directory_text.config(state=tk.DISABLED)


def on_key_release_entry(
        related_key: str,
        entry: tk.Entry,
) -> None:
    global state_holder
    if entry.get() == '':
        state_holder[related_key] = None
    else:
        state_holder[related_key] = entry.get()
    print(state_holder)


def on_date_entry_selected(
        related_key: str,
        dateentry: DateEntry,
) -> None:
    global state_holder
    if dateentry.get() == '':
        state_holder[related_key] = None
    else:
        state_holder[related_key] = dateentry.get_date()


def push_make_statements_button() -> None:
    global state_holder

    if any(state is None for state in state_holder.values()):
        messagebox.showerror(
            title='Ошибка',
            message='Одно или несколько полей не заполнены!'
        )
        return

    if len(state_holder['semester_files_paths']) != state_holder['semester_files_paths']:
        messagebox.showerror(
            title='Ошибка',
            message='Количество выбранных файлов зачётно-экзаменационных ведомостей '
                    'и выбранное количество зачётно-экзаменационных ведомостей не совпадают!'
        )
        return


def get_new_separator(
        root: tk.Frame,
) -> tk.Frame:
    return tk.Frame(root, height=1, background='gray')


def _on_mouse_wheel(
        event: tk.Event,
        canvas: tk.Canvas,
) -> None:
    canvas.yview_scroll(
        -1 * (event.delta // 120),
        "units"
    )


def main() -> None:
    main_window = tk.Tk()
    main_window.title("Программное средство для формирования выписки из зачётно-экзаменационной ведомости")
    main_window.geometry("888x800")
    main_window.resizable(
        width=False,
        height=False
    )

    container = tk.Frame(main_window)
    container.pack(
        fill=tk.BOTH,
        expand=True
    )

    canvas = tk.Canvas(
        container,
        highlightthickness=0,
    )
    scrollbar = ttk.Scrollbar(
        container,
        orient=tk.VERTICAL,
        command=canvas.yview
    )
    scrollbar.pack(
        side=tk.RIGHT,
        fill=tk.Y
    )
    canvas.pack(
        side=tk.LEFT,
        fill=tk.BOTH,
        expand=True
    )
    canvas.configure(yscrollcommand=scrollbar.set)

    root = tk.Frame(canvas)
    root.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )
    canvas.create_window(
        (0, 0),
        window=root,
        anchor="nw"
    )
    canvas.bind_all(
        "<MouseWheel>",
        lambda event: _on_mouse_wheel(event, canvas=canvas)
    )

    global GRID_COLUMNS_COUNT
    for i in range(GRID_COLUMNS_COUNT):
        root.grid_columnconfigure(i, weight=1)

    app_name_label = tk.Label(
        root,
        text="Формирование выписок из зачётно-экзаменационной ведомости",
        font=("Arial", 18)
    )
    app_name_label.grid(
        column=0,
        row=0,
        columnspan=4,
        padx=5,
        pady=5,
        sticky=tk.EW
    )

    get_new_separator(root).grid(
        column=0,
        row=1,
        columnspan=4,
        sticky=tk.EW
    )

    semester_count_label = tk.Label(
        root,
        text="Выберите количество зачётно-экзаменационных ведомостей:",
        font=("Arial", 10)
    )
    semester_count_label.grid(
        column=0,
        row=2,
        columnspan=2,
        padx=5,
        pady=5,
        sticky=tk.W
    )

    global SEMESTER_COUNT_COMBOBOX_VALUES
    semester_count_combobox = ttk.Combobox(root, values=SEMESTER_COUNT_COMBOBOX_VALUES, state="readonly")
    semester_count_combobox.set('Не выбрано')
    semester_count_combobox.bind(
        "<<ComboboxSelected>>",
        lambda e: on_semester_count_combobox_selected(semester_count_combobox)
    )
    semester_count_combobox.grid(
        column=2,
        row=2,
        columnspan=2,
        padx=5,
        pady=5,
        sticky=tk.EW
    )

    get_new_separator(root).grid(
        column=0,
        row=3,
        columnspan=4,
        sticky=tk.EW
    )

    semester_files_label = tk.Label(
        root,
        text="Выберите файлы зачётно-экзаменационных ведомостей и "
             "расположите их в порядке хронологического следования:",
        font=("Arial", 10)
    )
    semester_files_label.grid(
        column=0,
        row=4,
        columnspan=2,
        padx=5,
        pady=5,
        sticky=tk.W
    )

    semester_files_button = tk.Button(
        root,
        text='Выбор файлов',
        font=("Arial", 10),
        command=lambda: push_semester_files_button(
            semester_files_listbox,
            semester_files_button_up,
            semester_files_button_down
        )
    )
    semester_files_button.grid(
        column=2,
        row=4,
        columnspan=2,
        padx=5,
        pady=5,
        sticky=tk.EW
    )

    semester_files_listbox = tk.Listbox(
        root,
        height=10,
        width=50,
        font=("Arial", 10),
        selectmode=tk.SINGLE,
        activestyle=tk.NONE
    )
    semester_files_listbox.insert(
        tk.END,
        'Файлы зачётно-экзаменационных ведомостей не выбраны...'
    )
    semester_files_listbox.config(state=tk.DISABLED)
    semester_files_listbox.grid(
        column=0,
        row=5,
        padx=5,
        pady=5,
        columnspan=3,
        rowspan=2,
        sticky=tk.EW
    )

    semester_files_button_up = tk.Button(
        root,
        text='Вверх',
        font=("Arial", 10),
        state=tk.DISABLED,
        command=lambda: push_semester_files_button_up(semester_files_listbox),
    )
    semester_files_button_up.grid(
        column=3,
        row=5,
        padx=5,
        pady=5,
        sticky=tk.EW
    )

    semester_files_button_down = tk.Button(
        root,
        text='Вниз',
        font=("Arial", 10),
        state=tk.DISABLED,
        command=lambda: push_semester_files_button_down(semester_files_listbox),
    )
    semester_files_button_down.grid(
        column=3,
        row=6,
        padx=5,
        pady=5,
        sticky=tk.EW
    )

    diplomas_file_label = tk.Label(
        root,
        text="Выберите файл с темами дипломных проектов:",
        font=("Arial", 10)
    )

    diplomas_file_label.grid(
        column=0,
        row=7,
        columnspan=2,
        padx=5,
        pady=5,
        sticky=tk.W
    )

    diplomas_file_button = tk.Button(
        root,
        text='Выбор файла',
        font=("Arial", 10),
        command=lambda: push_diplomas_file_button(diplomas_file_text),
    )
    diplomas_file_button.grid(
        column=2,
        row=7,
        columnspan=2,
        padx=5,
        pady=5,
        sticky=tk.EW
    )

    diplomas_file_text = tk.Text(
        root,
        height=3,
        width=50,
        font=("Arial", 10),
        wrap=tk.WORD,
    )
    diplomas_file_text.insert(
        '1.0',
        'Файл с темами дипломных проектов не выбран...'
    )
    diplomas_file_text.config(state=tk.DISABLED)
    diplomas_file_text.grid(
        column=0,
        row=8,
        padx=5,
        pady=5,
        columnspan=4,
        sticky=tk.EW
    )

    get_new_separator(root).grid(
        column=0,
        row=9,
        columnspan=4,
        sticky=tk.EW
    )

    template_file_label = tk.Label(
        root,
        text="Выберите файл шаблона выписки:",
        font=("Arial", 10)
    )
    template_file_label.grid(
        column=0,
        row=10,
        columnspan=2,
        padx=5,
        pady=5,
        sticky=tk.W
    )

    template_file_button = tk.Button(
        root,
        text='Выбор файла',
        font=("Arial", 10),
        command=lambda: push_template_file_button(template_file_text),
    )
    template_file_button.grid(
        column=2,
        row=10,
        columnspan=2,
        padx=5,
        pady=5,
        sticky=tk.EW
    )

    template_file_text = tk.Text(
        root,
        height=3,
        width=50,
        font=("Arial", 10),
        wrap=tk.WORD,
    )
    template_file_text.insert(
        '1.0',
        'Файл шаблона выписки не выбран...'
    )
    template_file_text.config(state=tk.DISABLED)
    template_file_text.grid(
        column=0,
        row=11,
        padx=5,
        pady=5,
        columnspan=4,
        sticky=tk.EW
    )

    get_new_separator(root).grid(
        column=0,
        row=12,
        columnspan=4,
        sticky=tk.EW
    )

    save_directory_label = tk.Label(
        root,
        text="Выберите директорию сохранения выписок:",
        font=("Arial", 10)
    )
    save_directory_label.grid(
        column=0,
        row=13,
        columnspan=2,
        padx=5,
        pady=5,
        sticky=tk.W
    )

    save_directory_button = tk.Button(
        root,
        text='Выбор директории',
        font=("Arial", 10),
        command=lambda: push_save_directory_button(save_directory_text),
    )
    save_directory_button.grid(
        column=2,
        row=13,
        columnspan=2,
        padx=5,
        pady=5,
        sticky=tk.EW
    )

    save_directory_text = tk.Text(
        root,
        height=3,
        width=50,
        font=("Arial", 10),
        wrap=tk.WORD,
    )
    save_directory_text.insert(
        '1.0',
        'Директория сохранения выписок не выбрана...'
    )
    save_directory_text.config(state=tk.DISABLED)
    save_directory_text.grid(
        column=0,
        row=14,
        padx=5,
        pady=5,
        columnspan=4,
        sticky=tk.EW
    )

    get_new_separator(root).grid(
        column=0,
        row=15,
        columnspan=4,
        sticky=tk.EW
    )

    speciality_name_label = tk.Label(
        root,
        text='Введите наименование специальности:',
        font=("Arial", 10),
    )
    speciality_name_label.grid(
        column=0,
        row=16,
        columnspan=4,
        padx=5,
        pady=5,
        sticky=tk.EW
    )

    speciality_name_entry = tk.Entry(
        root,
        font=("Arial", 10),
    )
    speciality_name_entry.bind(
        '<KeyRelease>',
        lambda event: on_key_release_entry('speciality_name', speciality_name_entry)
    )
    speciality_name_entry.grid(
        column=0,
        row=17,
        columnspan=4,
        padx=5,
        pady=5,
        sticky=tk.EW
    )

    speciality_code_label = tk.Label(
        root,
        text='Введите код специальности:',
        font=("Arial", 10),
    )
    speciality_code_label.grid(
        column=0,
        row=18,
        columnspan=4,
        padx=5,
        pady=5,
        sticky=tk.EW
    )

    speciality_code_entry = tk.Entry(
        root,
        font=("Arial", 10),
    )
    speciality_code_entry.bind(
        '<KeyRelease>',
        lambda event: on_key_release_entry('speciality_code', speciality_code_entry)
    )
    speciality_code_entry.grid(
        column=0,
        row=19,
        columnspan=4,
        padx=5,
        pady=5,
        sticky=tk.EW
    )

    get_new_separator(root).grid(
        column=0,
        row=20,
        columnspan=4,
        sticky=tk.EW
    )

    speciality_area_name_label = tk.Label(
        root,
        text='Введите наименование направления специальности:',
        font=("Arial", 10),
    )
    speciality_area_name_label.grid(
        column=0,
        row=21,
        columnspan=4,
        padx=5,
        pady=5,
        sticky=tk.EW
    )

    speciality_area_name_entry = tk.Entry(
        root,
        font=("Arial", 10),
    )
    speciality_area_name_entry.bind(
        '<KeyRelease>',
        lambda event: on_key_release_entry('speciality_area_name', speciality_area_name_entry)
    )
    speciality_area_name_entry.grid(
        column=0,
        row=22,
        columnspan=4,
        padx=5,
        pady=5,
        sticky=tk.EW
    )

    speciality_area_code_label = tk.Label(
        root,
        text='Введите код направления специальности:',
        font=("Arial", 10),
    )
    speciality_area_code_label.grid(
        column=0,
        row=23,
        columnspan=4,
        padx=5,
        pady=5,
        sticky=tk.EW
    )

    speciality_area_code_entry = tk.Entry(
        root,
        font=("Arial", 10),
    )
    speciality_area_code_entry.bind(
        '<KeyRelease>',
        lambda event: on_key_release_entry('speciality_area_code', speciality_area_code_entry)
    )
    speciality_area_code_entry.grid(
        column=0,
        row=24,
        columnspan=4,
        padx=5,
        pady=5,
        sticky=tk.EW
    )

    get_new_separator(root).grid(
        column=0,
        row=25,
        columnspan=4,
        sticky=tk.EW
    )

    start_date_label = tk.Label(
        root,
        text='Выберите дату начала обучения:',
        font=("Arial", 10),
    )
    start_date_label.grid(
        column=0,
        row=26,
        columnspan=4,
        padx=5,
        pady=5,
        sticky=tk.EW
    )

    start_date_dateentry = DateEntry(
        root,
        date_pattern='DD-MM-YYYY',
        locale='ru',
        state='readonly'
    )
    start_date_dateentry.bind(
        '<<DateEntrySelected>>',
        lambda event: on_date_entry_selected('start_date', start_date_dateentry)
    )
    start_date_dateentry.grid(
        column=0,
        row=27,
        columnspan=4,
        padx=5,
        pady=5,
        sticky=tk.EW
    )

    end_date_label = tk.Label(
        root,
        text='Выберите дату конца обучения:',
        font=("Arial", 10),
    )
    end_date_label.grid(
        column=0,
        row=28,
        columnspan=4,
        padx=5,
        pady=5,
        sticky=tk.EW
    )

    end_date_dateentry = DateEntry(
        root,
        date_pattern='DD-MM-YYYY',
        locale='ru',
        state='readonly'
    )
    end_date_dateentry.bind(
        '<<DateEntrySelected>>',
        lambda event: on_date_entry_selected('end_date', end_date_dateentry)
    )
    end_date_dateentry.grid(
        column=0,
        row=29,
        columnspan=4,
        padx=5,
        pady=5,
        sticky=tk.EW
    )

    get_new_separator(root).grid(
        column=0,
        row=30,
        columnspan=4,
        sticky=tk.EW
    )

    statement_date_label = tk.Label(
        root,
        text='Выберите дату формирования выписки:',
        font=("Arial", 10),
    )
    statement_date_label.grid(
        column=0,
        row=31,
        columnspan=4,
        padx=5,
        pady=5,
        sticky=tk.EW
    )

    statement_date_dateentry = DateEntry(
        root,
        date_pattern='DD-MM-YYYY',
        locale='ru',
        state='readonly'
    )
    statement_date_dateentry.bind(
        '<<DateEntrySelected>>',
        lambda event: on_date_entry_selected('statement_date', statement_date_dateentry)
    )
    statement_date_dateentry.grid(
        column=0,
        row=32,
        columnspan=4,
        padx=5,
        pady=5,
        sticky=tk.EW
    )

    get_new_separator(root).grid(
        column=0,
        row=33,
        columnspan=4,
        sticky=tk.EW
    )

    make_statements_button = tk.Button(
        root,
        text='Выполнить формирование выписок',
        font=("Arial", 12),
        command=lambda: 0,
    )
    make_statements_button.grid(
        column=0,
        row=34,
        columnspan=4,
        padx=5,
        pady=5,
        sticky=tk.EW
    )
    root.mainloop()


if __name__ == '__main__':
    main()
