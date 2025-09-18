import os 
import shutil


def get_files_in_folder(folder = "."):
    files = os.listdir(".")
    print("Files I found:")
    for file in files:
        if os.path.isfile(file):
            print(f"- {file}")
    return files


def get_file_extension(filename):
    _, ext = os.path.splitext(filename)
    return ext.lower()


def get_target_folder(extension, extension_map):
    return extension_map.get(extension, "Others")


def create_folder(folder_name):
    os.makedirs(folder_name, exist_ok = True)


def preview_organization(files, extension_map):
    print("Preview of file organization: \n")
    for file in files:
        if os.path.isfile(file):
            ext = get_file_extension(file)
            folder = get_target_folder(ext, extension_map)
            print(f"- {file} -> would move to {folder}")
    

def move_files(files, extension_map):
    summary = {}

    for file in files:
        if os.path.isfile(file):
            ext = get_file_extension(file)
            folder = get_target_folder(ext, extension_map)
            create_folder(folder)
            shutil.move(file, os.path.join(folder, file))
            
            if folder in summary:
                summary[folder] += 1
            else:
                summary[folder] = 1
    return summary


def show_summary(summary):
    if not summary:
        print("No files were moved!")
        return
    
    print("\n File Organization Summary:")
    print("=" * 30)
    for folder, count in summary.items():
        print(f"- {count} file(s) moved to {folder}/")
    print("=" *30)


def main():
    extension_map = {
        ".txt" : "TextFile",
        ".py" : "PythonFile",
        ".jpg" : "Images"    
    }

    files = get_files_in_folder()

    preview_organization(files, extension_map)

    confirm = input("Do you want to proceed with the organization? (y/n): ").lower().strip()
    if confirm == 'y':
        summary = move_files(files, extension_map)
        show_summary(summary)
        print("Files have been organized.")
    else:
        print("Operation Cancelled!")

if __name__ == "__main__":
    main()
 