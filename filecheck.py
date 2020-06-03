from pathlib import Path, PurePosixPath
from filecmp import dircmp

cwd = Path('./files')

def remove_prefix(text, prefix):
    if text.startswith(prefix):
        return text[len(prefix):]
    return text  # or whatever

selectables = [x for x in cwd.iterdir() if x.is_dir()]

print("Dedected options:")

for i, j in enumerate(selectables):
    #i = i + 1
    print(str(i+1) + ': ' + remove_prefix(str(PurePosixPath(j)), "files/"))

selection = input("Which CFW do you want to check? ")

#print(selectables[int(selection)-1])

disk = input("What's the location of your SD card(like D: on windows)? ")

compare = dircmp((disk), selectables[int(selection)-1], ["info.json", "manifest.install"])

if compare.right_only:
    print("Missing files: \n")
    for k in compare.right_only:
        print(k)
