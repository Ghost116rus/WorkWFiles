import os


def GetPaths(FileName):
    return os.path.join(FileName), os.path.abspath(FileName)


path, absPath = GetPaths("numbers.txt")
print(f"Путь до файла: {path},\nАбсолютный путь: {absPath}")
