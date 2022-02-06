# pathlib
# Path позволяет работать с файлами и папками в ООП

from pathlib import Path

cd = Path('.')

print(f"{cd}, {type(cd)}")
print(f"{cd.name}, {type(cd.name)}")
print(f"{cd.absolute()}, {type(cd.absolute())}")

for child in cd.iterdir():
    pass
    """
    if str(child) == '.gitignore':
        print(f"File: {child}")
        print("-"*10, "file name:", child, "-"*10)
        #print(type(child)
        with child.open() as f:
            print(f.read())
        print("-"*50, "End", "-"*50)
        f.close()
    """
    """
    if not child.is_dir() and str(child) != 'index.html':
        with child.open(encoding="utf-8") as f:
            print(f"File: {child}")
            print(f"File name: {child.name}")
            
            print("-"*50, "file name:", child, "-"*50)
            # Проблема с кодировкой utf-8, читает файлы только с кодировкой cp1251
            # Используем encoding="utf-8": open(encoding="utf-8")
            # "wb", "r", "w"
            print(f.read())
            print("-"*50, "End", "-"*50)
            f.close()
    """
#Path(f'{cd.name}/documents') 

dir_doc = cd / 'documents'
print(f"{dir_doc}, {type(dir_doc)}")
print(f"{dir_doc.name}, {type(dir_doc.name)}")
print(f"{dir_doc.absolute()}, {type(dir_doc.absolute())}")

for child_doc in dir_doc.iterdir():
    print(f"File: {child_doc}")

# End