import os
import re
try:
    from tkinter import *
    from tkinter import messagebox
except ImportError:
    pass
import logging
logging.basicConfig(level=logging.INFO,
                    format=' %(asctime)s - %(levelname)s - %(message)s')

match_list_regex = r"(List<.*>) (.*);"


def get_all_files_for_extension(filepath, extension):
    files = []
    for root, dirs, filenames in os.walk(filepath):
        for filename in filenames:
            full_path = os.path.join(root, filename)
            files.append(full_path)
    return files


def having_list_item(line):
    matches = re.finditer(match_list_regex, line)
    for _, match in enumerate(matches):
        return match.group(1), match.group(2)
    return None, None


def capitalize_word(word):
        return word[0].upper() + word[1:]


def print_file(file_path):
    with open(file_path, "r+") as f:
        lines = f.read().splitlines()
        for line in lines:
            if having_list_item(line):
                logging.info(line)


def make_setter_function(var_type, var_name):
    string = "\npublic void set"+capitalize_word(var_name)
    string = string + "(" + var_type + " " + var_name + ") {\n"
    string = string + "\tthis." + var_name + " = " + var_name + ";\n"
    string = string + "}\n"
    return string


def read_file(file_path):
    with open(file_path, "r") as in_file:
        buf = in_file.readlines()

    with open(file_path, "w") as out_file:
        for line in buf:
            var_type, var_name = having_list_item(line)
            if var_name:
                logging.info(file_path)
                function_in_string = make_setter_function(var_type, var_name)
                line = line + "\n" + function_in_string
            out_file.write(line)


def generate_setter(file_path):
    java_files = get_all_files_for_extension(file_path, "")
    for file in java_files:
        read_file(file)

def cli():
    adding_list_setter(input("Full File Path:"))

def gui():
    def start_population():
        adding_list_setter(entry_path.get(), True)

    master = Tk()
    master.wm_title("Setter Generator")

    label_input_path = Label(master, text="Enter the filepath: ").grid(row=0, sticky=W)
    entry_path = Entry(master)
    entry_path.grid(row=0, column=1)

    Button(master, text='Generate List Setter', command=start_population).grid(row=1, column=0, sticky=W)

    mainloop()


def adding_list_setter(file_path, tkEnabled=False):
    if len(file_path) == 0:
        logging.error("Please Enter the valid path")
        try:
            if(tkEnabled):
                messagebox.showinfo("Error", "Please Enter the valid path")
        except:
            pass
        return
    logging.info(file_path)
    if "generated-sources\jax-ws" not in file_path and "generated-sources/jax-ws" not in file_path :
        option = input("You are not in generated sources, possibly sources may change. Do you want to continue (y/n): ")
        if option == "y":
            generate_setter(file_path)
    else:
        generate_setter(file_path)


if __name__ == "__main__":
    cli()
