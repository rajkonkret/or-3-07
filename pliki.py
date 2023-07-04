# pliki
# kontekst menadzer
# Character Meaning
#     --------- ---------------------------------------------------------------
#     'r'       open for reading (default)
#     'w'       open for writing, truncating the file first
#     'x'       create a new file and open it for writing
#     'a'       open for writing, appending to the end of the file if it exists
#     'b'       binary mode
#     't'       text mode (default)
#     '+'       open a disk file for updating (reading and writing)
with open('test.log', "w", encoding='utf-8') as fh:
    fh.write("Powitanie\n")
    fh.write("Kolejne\n")
    fh.write("jeszcze jedno\n")

with open('test.log', 'w', encoding='utf-8') as f:
    f.write("Radek\n")

with open('test.log', 'a', encoding='utf-8') as file:
    file.write("dodane\n")
    file.write("dośdane\n")

with open('test.log', 'r', encoding='utf-8') as f:
    lines = f.read()

print(lines)
