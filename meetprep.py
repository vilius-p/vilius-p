#!/usr/bin/pythonr3

import datetime
import os

notes_dir = "/home/<username>/Notes/"  # Absolute path to Notes directory
work_dir = notes_dir + datetime.datetime.now().strftime(
    "%Y/%m/%V"
)  # Absolute path to current week's directory according to JNOTE
line_extract = ">"  # Specify symbol your lines will start with for extraction
comment_list = []
week_notes = []


def scan_dir():
    dir_notes = os.listdir(work_dir)
    for item in dir_notes:
        if "week_summary" in item:
            pass
        elif ".md" and not "scanned" in item:
            week_notes.append(item)


def scan_note():
    for notename in week_notes:
        with open(work_dir + "/" + notename, "r") as day_file:
            for line in day_file:
                if line.startswith(line_extract):
                    clean_line = line.strip(line_extract + " ")
                    comment_list.append(clean_line)


def write_talkpoints():
    with open(work_dir + "/" + "week_summary.md", "a") as week_summary:
        week_summary.writelines(comment_list)


def rename_note():
    for note in week_notes:
        new_name = note.replace(".md", "-scanned.md")
        os.renames(work_dir + "/" + note, work_dir + "/" + new_name)
        print("Changed " + note + " to " + new_name)


scan_dir()
scan_note()
write_talkpoints()
rename_note()
print("Files modified:", week_notes)
print("In directory:", work_dir)

