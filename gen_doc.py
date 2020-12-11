from pydoc import render_doc, plain
from pathlib import PurePath, Path
import base64
from datetime import datetime, date, time, timedelta
import sqlite3

def write_file(output_file, content):
    with open(output_file, "w") as file:
        file.write(content)

p = PurePath(r"C:\Users\mod69\Desktop\pythondocs")

write_file(p / "int.txt", plain(render_doc(int)))
write_file(p / "float.txt", plain(render_doc(float)))
write_file(p / "str.txt", plain(render_doc(str)))
write_file(p / "list.txt", plain(render_doc(list)))
write_file(p / "tuple.txt", plain(render_doc(tuple)))
write_file(p / "dict.txt", plain(render_doc(dict)))
write_file(p / "set.txt", plain(render_doc(set)))
write_file(p / "datetime.txt", plain(render_doc(datetime)))
write_file(p / "date.txt", plain(render_doc(date)))
write_file(p / "time.txt", plain(render_doc(time)))
write_file(p / "timedelta.txt", plain(render_doc(timedelta)))
write_file(p / "base64.txt", plain(render_doc(base64)))
write_file(p / "sqlite3.txt", plain(render_doc(sqlite3)))
write_file(p / "PurePath.txt", plain(render_doc(PurePath)))
write_file(p / "Path.txt", plain(render_doc(Path)))