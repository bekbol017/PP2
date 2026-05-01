import os
import shutil
os.makedirs("source_dir", exist_ok=True)
os.makedirs("dest_dir", exist_ok=True)
for name in ["file1.txt", "file2.py", "file3.csv"]:
    with open(f"source_dir/{name}", "w") as f:
        f.write(f"Content of {name}\n")

#1
shutil.move("source_dir/file1.txt", "dest_dir/file1.txt")
print(f"dest_dir contains: {os.listdir('dest_dir')}")

#2
shutil.move("source_dir/file2.py", "source_dir/renamed.py")
print(f"source_dir contains: {os.listdir('source_dir')}")

#3
os.rename("source_dir/renamed.py", "source_dir/script.py")
print(f"After rename: {os.listdir('source_dir')}")

#4
for fname in os.listdir("source_dir"):
    if fname.endswith(".csv"):
        shutil.move(f"source_dir/{fname}", f"dest_dir/{fname}")
print(f"dest_dir: {os.listdir('dest_dir')}")

#5
if os.path.exists("dest_dir_copy"):
    shutil.rmtree("dest_dir_copy")
shutil.copytree("dest_dir", "dest_dir_copy")
print(f"Copied dest_dir → dest_dir_copy: {os.listdir('dest_dir_copy')}")

# Cleanup
shutil.rmtree("source_dir")
shutil.rmtree("dest_dir")
shutil.rmtree("dest_dir_copy")