import tkinter as tk
from tkinter import filedialog, ttk
from tkinter import messagebox
from tkcalendar import DateEntry


GRID_COLUMNS_COUNT = 4
SEMESTER_COUNT_COMBOBOX_VALUES = ('1', '2', '3', '4', '5', '6', '7', '8')


def get_new_separator(
        root: tk.Frame,
) -> tk.Frame:
    return tk.Frame(root, height=1, background='gray')


def _on_mouse_wheel(
        event: tk.Event,
        canvas: tk.Canvas,
):
    canvas.yview_scroll(
        -1 * (event.delta // 120),
        "units"
    )


def main() -> None:
    main_window = tk.Tk()
    main_window.title("Программное средство для формирования выписки из зачётно-экзаменационной ведомости")
    main_window.geometry("800x800")
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
        text="Выберите файлы зачётно-экзаменационных ведомостей в порядке их хронологического следования:",
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
        command=lambda: 0,
    )
    semester_files_button.grid(
        column=2,
        row=4,
        columnspan=2,
        padx=5,
        pady=5,
        sticky=tk.EW
    )

    semester_files_text = tk.Text(
        root,
        height=10,
        width=50,
        font=("Arial", 10),
        wrap=tk.WORD,
    )
    semester_files_text.insert(
        '1.0',
        'Файлы зачётно-экзаменационных ведомостей не выбраны...'
    )
    semester_files_text.config(state=tk.DISABLED)
    semester_files_text.grid(
        column=0,
        row=5,
        padx=5,
        pady=5,
        columnspan=4,
        sticky=tk.EW
    )

    diplomas_file_label = tk.Label(
        root,
        text="Выберите файл с темами дипломных проектов:",
        font=("Arial", 10)
    )

    diplomas_file_label.grid(
        column=0,
        row=6,
        columnspan=2,
        padx=5,
        pady=5,
        sticky=tk.W
    )

    diplomas_file_button = tk.Button(
        root,
        text='Выбор файла',
        font=("Arial", 10),
        command=lambda: 0,
    )
    diplomas_file_button.grid(
        column=2,
        row=6,
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
        row=7,
        padx=5,
        pady=5,
        columnspan=4,
        sticky=tk.EW
    )

    get_new_separator(root).grid(
        column=0,
        row=8,
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
        row=9,
        columnspan=2,
        padx=5,
        pady=5,
        sticky=tk.W
    )

    template_file_button = tk.Button(
        root,
        text='Выбор файла',
        font=("Arial", 10),
        command=lambda: 0,
    )
    template_file_button.grid(
        column=2,
        row=9,
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
        row=10,
        padx=5,
        pady=5,
        columnspan=4,
        sticky=tk.EW
    )

    get_new_separator(root).grid(
        column=0,
        row=11,
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
        row=12,
        columnspan=2,
        padx=5,
        pady=5,
        sticky=tk.W
    )

    save_directory_button = tk.Button(
        root,
        text='Выбор директории',
        font=("Arial", 10),
        command=lambda: 0,
    )
    save_directory_button.grid(
        column=2,
        row=12,
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
        row=13,
        padx=5,
        pady=5,
        columnspan=4,
        sticky=tk.EW
    )

    get_new_separator(root).grid(
        column=0,
        row=14,
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
        row=15,
        columnspan=4,
        padx=5,
        pady=5,
        sticky=tk.EW
    )

    speciality_name_entry = tk.Entry(
        root,
        font=("Arial", 10),
    )
    speciality_name_entry.grid(
        column=0,
        row=16,
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
        row=17,
        columnspan=4,
        padx=5,
        pady=5,
        sticky=tk.EW
    )

    speciality_code_entry = tk.Entry(
        root,
        font=("Arial", 10),
    )
    speciality_code_entry.grid(
        column=0,
        row=18,
        columnspan=4,
        padx=5,
        pady=5,
        sticky=tk.EW
    )

    get_new_separator(root).grid(
        column=0,
        row=19,
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
        row=20,
        columnspan=4,
        padx=5,
        pady=5,
        sticky=tk.EW
    )

    speciality_area_name_entry = tk.Entry(
        root,
        font=("Arial", 10),
    )
    speciality_area_name_entry.grid(
        column=0,
        row=21,
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
        row=22,
        columnspan=4,
        padx=5,
        pady=5,
        sticky=tk.EW
    )

    speciality_area_code_entry = tk.Entry(
        root,
        font=("Arial", 10),
    )
    speciality_area_code_entry.grid(
        column=0,
        row=23,
        columnspan=4,
        padx=5,
        pady=5,
        sticky=tk.EW
    )

    get_new_separator(root).grid(
        column=0,
        row=24,
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
        row=25,
        columnspan=4,
        padx=5,
        pady=5,
        sticky=tk.EW
    )

    start_date_dateentry = DateEntry(
        root,
        date_pattern='DD-MM-YYYY',
        locale='ru'
    )
    start_date_dateentry.grid(
        column=0,
        row=26,
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
        row=27,
        columnspan=4,
        padx=5,
        pady=5,
        sticky=tk.EW
    )

    end_date_dateentry = DateEntry(
        root,
        date_pattern='DD-MM-YYYY',
        locale='ru'
    )
    end_date_dateentry.grid(
        column=0,
        row=28,
        columnspan=4,
        padx=5,
        pady=5,
        sticky=tk.EW
    )

    get_new_separator(root).grid(
        column=0,
        row=29,
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
        row=30,
        columnspan=4,
        padx=5,
        pady=5,
        sticky=tk.EW
    )

    statement_date_dateentry = DateEntry(
        root,
        date_pattern='DD-MM-YYYY',
        locale='ru'
    )
    statement_date_dateentry.grid(
        column=0,
        row=31,
        columnspan=4,
        padx=5,
        pady=5,
        sticky=tk.EW
    )

    get_new_separator(root).grid(
        column=0,
        row=32,
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
        row=33,
        columnspan=4,
        padx=5,
        pady=5,
        sticky=tk.EW
    )

    root.mainloop()


if __name__ == '__main__':
    main()
