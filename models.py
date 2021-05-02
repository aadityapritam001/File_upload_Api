from database import db

def view(file_names):
    all_files=[]
    for file in file_names:
        all_files.append({'path':file})

    resp=db.insert(all_files)
    return resp
