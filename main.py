from util import create_files, create_folders, validate_path, path_exists
from util import write_to_file, create_menu, clear, success_prompt, get_common_paths
from util import overwrite_prompt

def main():
    clear() # Clear terminal (For aesthetic purposes ;D)
    while True:
        try:
            option = create_menu("Cabinet", ["New File", "New Folder", "Quit"])
            if option == 0:
                files_menu()
            elif option == 1:
                folders_menu()
            elif option == 2:
                break
            else:
                continue
        except ValueError:
            continue
    
    clear()

def files_menu():
    option = create_menu("Files", ["Create new files", "Write to file", "Back"])
    if option == 0:
        path_name = get_path()
        if not path_name:
            clear() 
            return
        
        print("Enter file names below:\n")
        file_paths, names = get_new_paths(path_name, "file", 0)

        if not file_paths: 
            clear()
            return
        create_files(file_paths)
        success_prompt(path_name, names, "files")
    elif option == 1:
        path = get_path()
        if not path:
            clear() 
            return
        
        file_path = get_new_paths(path, "file", 1)
        
        if not file_path:
            clear()
            return
        else:
            write_to_file(file_path)
        clear()
    else:
        return

def folders_menu():
    option = create_menu("Folders", ["Create new folders", "Add files to folder", "Back"])
    if option == 0:
        path_name = get_path()
        if not path_name: 
            clear()
            return
        
        print("Enter folder names below:\n")
        folder_paths, names = get_new_paths(path_name, "folder", 0)

        if not folder_paths:
            clear() 
            return
        create_folders(folder_paths)
        success_prompt(path_name, names, "folders")
    elif option == 1:
        # TODO: Implement function to add files to a new folder
        pass
    else:
        pass

def get_path():
    common_paths = get_common_paths()
    selected_option = create_menu("Enter path", common_paths)
    
    if selected_option == 5 or selected_option == None:
        return None
    elif selected_option == 4:
        while True:
            try:
                path_name = input("Enter custom path: ")  
                if validate_path(path_name) != None:
                    return path_name
    
            except KeyboardInterrupt:
                return None
    else:
        return common_paths[selected_option]
    

def get_new_paths(path, s, n):
    paths = []
    names = []
    while True:
        try:
            name = input(f"{s}: ")
            if name == ".":
                return paths, names
            
            if not path_exists(f"{path}/{name}", paths, s):
                if n == 1:
                    return f"{path}/{name}"
                else:
                    paths.append(f"{path}/{name}")
                    names.append(name)
            else:
                if n == 1:
                    selected_option = overwrite_prompt()
                    if selected_option == 0:
                        return f"{path}/{name}"
                    else:
                        return None
                else:
                    continue
            
        except ValueError:
            continue
        except KeyboardInterrupt:
            return [None, None]


if __name__ == "__main__":
    main()
