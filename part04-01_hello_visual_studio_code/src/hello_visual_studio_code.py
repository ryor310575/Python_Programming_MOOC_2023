# Write your solution here
while True:
    name = input("Editor: ")
    name_lower = name.lower()
    if name_lower == "visual studio code":
        print("an excellent choice!")
        break
    elif name.lower() == "word" or name == "notepad":
        print("awful")
    # elif name_lower.find("visual studio code") and name_lower.find("emacs"):
    #     print("an excellent choice!")
    #     print("an excellent choice!")
    else:
        print("not good")
        # /Users/ryanortega/Library/Application Support/tmc/vscode/mooc-programming-23/part04-01_hello_visual_studio_code/src/hello_visual_studio_code.py
