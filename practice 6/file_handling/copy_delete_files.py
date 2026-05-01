import os
import shutil
with open("original.txt", "w") as f:
    f.write("This is the original file.\nLine 2.\nLine 3.\n")

#1
shutil.copy("original.txt", "copy1.txt")
print("Copied original.txt → copy1.txt")

#2
shutil.copy2("original.txt", "copy2_with_meta.txt")
print("Copied with metadata → copy2_with_meta.txt")

#3
os.makedirs("backup", exist_ok=True)
shutil.copy("original.txt", "backup/original_backup.txt")
print("Backup saved to backup/original_backup.txt")

#4
if os.path.exists("copy1.txt"):
    os.remove("copy1.txt")
    print("copy1.txt deleted")
else:
    print("File not found")

#5
if os.path.exists("backup"):
    shutil.rmtree("backup")
    print("backup/ folder deleted entirely")