# File Handling Review
from pathlib import Path


# this __file__ is where thhe refence python script as the location
BASE_DIR = Path(__file__).resolve().parent
file_path = BASE_DIR / "test-files" / "file1.txt"


f = open(file_path, "rt")
text = f.read()
f.close()
print(text)

# In depth
with open(file_path, "r") as f:
    data = f.read()
    print(data)

with open(file_path, "r+") as f:
    data = "some data"
    original_file = f.read()
    print(data)
    new_file = f.write(data)
    print(new_file)

# Listing the files
files = BASE_DIR / "test-files"
the_files = files.iterdir()
for item in the_files:
  if item.is_file():
    print(item.name)
    
    
