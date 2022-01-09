import os
import shutil

sourcepath='C:\\Users\\ammar_m4r3wcb\\Downloads'
sourcefiles = os.listdir(sourcepath)
destinationpath_images = 'C:\\Users\\ammar_m4r3wcb\\Downloads\\Images'
destinationpath_documents = 'C:\\Users\\ammar_m4r3wcb\\Downloads\\Documents'
destinationpath_code = 'C:\\Users\\ammar_m4r3wcb\\Downloads\\Code'

for file in sourcefiles:
    if file.endswith('.PNG') or file.endswith('.gif') or file.endswith('.jpg') or file.endswith('.svg') or file.endswith('.jpeg'): 
        shutil.move(os.path.join(sourcepath,file), os.path.join(destinationpath_images,file))
    if file.endswith('.pdf') or file.endswith('.PDF') or file.endswith('.docx'):
        shutil.move(os.path.join(sourcepath,file), os.path.join(destinationpath_documents,file))
    if file.endswith('.html') or file.endswith('.py') or file.endswith('.css') or file.endswith('.java'):
        shutil.move(os.path.join(sourcepath,file), os.path.join(destinationpath_code,file))