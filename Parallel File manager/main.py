from pathlib import Path
import shutil


def file_distribute(file_extension,file_path,file_name):
    code_file_path = "/home/yuvraj/Python Practice/Parallel File manager/code files"
    image_file_path = "/home/yuvraj/Python Practice/Parallel File manager/Image files"
    video_file_path = "/home/yuvraj/Python Practice/Parallel File manager/Video files"
    text_file_path = "/home/yuvraj/Python Practice/Parallel File manager/Text files"
    categories = {
        "Images": [".jpg", ".jpeg", ".png", ".gif"],
        "Videos": [".mp4", ".mkv", ".avi"],
        "Code_files": [".pdf", ".docs",".py", ".html", ".css", ".js", ".idea", ".xml", ".iml", ".tar", ".zip"],
        "text_files":[".txt"]
    }
    Images = categories["Images"]
    Videos = categories["Videos"]
    Code_files = categories["Code_files"]
    Text_files = categories["text_files"]



    if file_extension in categories["Images"]:
        shutil.copyfile(file_path,"/home/yuvraj/Python Practice/Parallel File manager/code files")
    elif file_extension in categories["Videos"]:
        shutil.copyfile(file_path,"/home/yuvraj/Python Practice/Parallel File manager/Video files")
    elif file_extension in categories["Code_files"]:
        shutil.copyfile(file_path,"/home/yuvraj/Python Practice/Parallel File manager/code files")
    elif file_extension in categories["text_files"]:
        shutil.copyfile(file_path,"/home/yuvraj/Python Practice/Parallel File manager/Text files")



def parallel_file_manager():
    dir_name= input("Enter name of the directory you wish to organize: ")
    root = Path("/home/yuvraj")
    valid_dir_check=False
    actual_path=""
    for path in root.rglob(dir_name):
        if path.is_dir() and path.name == dir_name:
            actual_path=path.resolve()
            valid_dir_check=True
            break
    if valid_dir_check == True:
        print(actual_path)
    else:
        print(f"Directory '{dir_name}' does not exist")


    if valid_dir_check == True:

        with open("log.txt","a") as data:

            p = Path(actual_path)
            for file in p.iterdir():
                if file.is_dir():
                    if file.is_dir():
                        for i in file.iterdir():
                            file_distribute(i.suffix,i.parent)
                            data.write(f"file_suffix:{i.suffix},file_path:{i.parent},file_name:{i.name}")
                    if file.is_file():
                        file_distribute(file.suffix,file.parent)
                        data.write(f"file_suffix:{file.suffix},file_path:{file.parent},file_name:{file.name}")
                if file.is_file():
                    file_distribute(file.suffix, file.parent)
                    data.write(f"file_suffix:{file.suffix},file_path:{file.parent},file_name:{file.name}")


parallel_file_manager()