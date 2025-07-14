#!/usr/bin/env python3
import os
import shutil

def organize_files_by_extension(folder):
    for filename in os.listdir(folder):
        if os.path.isfile(os.path.join(folder, filename)):
            ext = filename.split('.')[-1]
            target_dir = os.path.join(folder, ext + "_files")
            os.makedirs(target_dir, exist_ok=True)
            shutil.move(os.path.join(folder, filename), os.path.join(target_dir, filename))

organize_files_by_extension(".")

