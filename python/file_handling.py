
# type: ignore
Interview Trick Questions
	•	Difference between read(), readline(), and readlines().
	•	What happens if you open a file in "w" mode that already exists? (Truncates it).
	•	How to handle very large files? (Answer: read in chunks / iterate line by line).
	•	Why prefer with open() over open() + close()? (Ensures closure even if error occurs).
	•	Difference between os.remove() and os.unlink()? (Same in most cases).
	•	How to move a file? (shutil.move).
	•	When to use "rb" vs "r"? (Binary data like images).

⸻

⚡ Quick Tip for Interviews:
	•	If asked to count words/lines/characters → use with open + iteration.
	•	If asked to reverse lines → reversed(list(f.readlines())).
	•	If asked to process huge logs → stream line by line, don’t read() entire file.


1. Opening and Closing Files
	•	Always use with open(...) – automatically closes the file.

with open("data.txt", "r") as f:
    content = f.read()
	

Modes:
	•	"r" → read (default, error if file not found)
	•	"w" → write (creates new / truncates existing)
	•	"a" → append
	•	"x" → exclusive creation (error if exists)
	•	"b" → binary (e.g., "rb")
	•	"t" → text (default, e.g., "rt")

⸻

2. Reading Files

f.read()       # whole content as string
f.readline()   # one line
f.readlines()  # list of all lines


Efficient iteration:

with open("data.txt") as f:
    for line in f:
        print(line.strip())
		

For large files:

import fileinput
for line in fileinput.input("data.txt"):
    process(line)



3. Writing Files

with open("output.txt", "w") as f:
    f.write("Hello\n")
    f.writelines(["line1\n", "line2\n"])


•	"w" overwrites.
•	"a" appends at end.


4. File Pointer

f.seek(offset, whence)
f.tell()  # current pointer position


•	whence=0 → start (default)
•	whence=1 → current position
•	whence=2 → end of file

Example:

with open("data.txt", "rb") as f:
    f.seek(0, 2)   # move to end
    size = f.tell()


5. Working with JSON / CSV

import json, csv

# JSON
with open("data.json") as f:
    data = json.load(f)   # dict
with open("out.json", "w") as f:
    json.dump(data, f, indent=4)

# CSV
with open("data.csv") as f:
    reader = csv.reader(f)
    for row in reader: print(row)


6. Exception Handling

try:
    with open("nofile.txt") as f:
        data = f.read()
except FileNotFoundError:
    print("File not found")


7. OS & Path Handling

import os

os.path.exists("data.txt")
os.path.getsize("data.txt")
os.listdir(".")

pathlib (modern way):

from pathlib import Path

p = Path("data.txt")
if p.exists():
    print(p.read_text())


8. Binary Files

with open("image.png", "rb") as f:
    data = f.read()
with open("copy.png", "wb") as f:
    f.write(data)








