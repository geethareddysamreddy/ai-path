import os
from datetime import datetime

def getfiles(folder):
    files = []
    for name in os.listdir(folder):
        path = os.path.join(folder, name)
        if os.path.isfile(path):
            files.append(path)
    return files

def getfileinfo(path):
    return {
        "name": os.path.basename(path),
        "path": path,
        "size": os.path.getsize(path),
        "ext": os.path.splitext(path)[1].lower(),
        "modified": datetime.fromtimestamp(os.path.getmtime(path))
    }

def filterfiles(files):
    ext = input("Filter by extension (py/txt/pdf or Enter for all): ").lower()
    if ext:
        if not ext.startswith("."):
            ext = "." + ext
        files = [f for f in files if f["ext"] == ext]

    sort_by = input("Sort by (name/size/date): ").lower()
    if sort_by == "size":
        files.sort(key=lambda f: f["size"], reverse=True)
    elif sort_by == "date":
        files.sort(key=lambda f: f["modified"], reverse=True)
    else:
        files.sort(key=lambda f: f["name"].lower())

    if not files:
        print("No files found.")
        return

    print(f"\n{'Name':<30} {'Size':>10} {'Ext':<8} {'Modified'}")
    print("-" * 65)
    for f in files:
        print(f"{f['name']:<30} {f['size']:>10} {f['ext']:<8} {f['modified'].strftime('%d-%m-%Y %H:%M')}")

def get_folder():
    while True:
        folder = input("Enter folder path: ").strip()
        if os.path.isdir(folder):       # ✅ validates path
            return folder
        print("Invalid path! Please enter a valid folder path.")

def main():
    folder = get_folder()
    paths = getfiles(folder)
    files = [getfileinfo(p) for p in paths]
    filterfiles(files)

main()