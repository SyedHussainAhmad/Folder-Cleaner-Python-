'''Folder Cleaner'''
import os

def create_dir(folder):
    '''Creates folder if the folder is not present.'''
    if not os.path.exists(folder):
        os.makedirs(folder)

def move_files(folder_name, input_files):
    '''Move files into the folder.'''
    for search_file in input_files:
        os.replace(search_file,f'{folder_name}/{search_file}')

def get_list(extension):
    '''Get list of the files.'''
    return [file for file in files if os.path.splitext(file)[1].lower() in extension]


if __name__ == "__main__":
    files = os.listdir()

    # Removes current file from list as we do not want to interrupt our program file.
    # files.remove("main.py")

    # Creatig Folder to arrange files in them.
    create_dir("Images")
    create_dir("Python")
    create_dir("Docs")
    create_dir("Zip Files")
    create_dir("Videos")
    create_dir("HTML")
    create_dir("Others")
    create_dir("Packages")

    # Creating list of files consisting defined extensions.
    imgExtensions = [".png",".jpg",".jpeg"]
    images = get_list(imgExtensions)

    vidExtensions = [".mp4",".mov",".avi",".mkv",".wmv"]
    videos = get_list(vidExtensions)

    docExtensions = [".pdf",".txt",".doc",".xls",".docx"]
    docs = get_list(docExtensions)

    zipExtensions = [".zip"]
    zips = get_list(zipExtensions)

    pythonExtensions = [".py"]
    python = get_list(pythonExtensions)

    htmlExtensions = [".html"]
    html = get_list(htmlExtensions)

    # Arranging all the other files in Others folder.
    others = []
    for file in files:
        ext = os.path.splitext(file)[1].lower()
        if (ext not in docExtensions) and (ext not in imgExtensions) and (ext not in pythonExtensions)  and (ext not in htmlExtensions)  and (ext not in vidExtensions)  and (ext not in zipExtensions) and os.path.isfile(file):
            others.append(file)

    # Arranging all the other Packages which
    # are not files (eg installation package) in Packages folder.
    packages = []
    for file in files:
        ext = os.path.splitext(file)[1].lower()
        if (ext not in docExtensions) and (ext not in imgExtensions) and (ext not in pythonExtensions)  and (ext not in htmlExtensions)  and (ext not in vidExtensions)  and (ext not in zipExtensions) and (ext not in others) and (not os.path.isdir()):
            packages.append(file)

    # Now Moving files to correspoding folders.

    move_files("Images",images)
    move_files("Videos",videos)
    move_files("Docs",docs)
    move_files("Zip Files",zips)
    move_files("Python",python)
    move_files("HTML",html)
    move_files("Others",others)
    move_files("Packages",packages)
