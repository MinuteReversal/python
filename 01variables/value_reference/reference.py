class Notepad:
    content = "666"


notepad = Notepad()
link1 = notepad
link2 = link1

link2.content = "abc"

print(notepad.content)
print(link1.content)
print(link2.content)
