import ruamel.std.zipfile as zipraum
import os
import zipfile as zipper
import shutil

directory = 'zips'
filetype = 'jpg'
destination = 'readUKIndex'


for file in os.listdir(directory):

        if file.endswith(".zip"):

        #Clean up jpgs from zip
        zipraum.delete_from_zip_file(directory +'/'+ file, pattern='.*.'+filetype)

        #Read first file from zip
        myzip = zipper.ZipFile(directory +'/'+ file,'r')
        firstFile = myzip.namelist()[0]
        myzip.close()

        # check if renaming is necessary
        if (file[:10]==firstFile[:10]):
            print ("OK")
        else:
            print ("rename\n", firstFile[:10]+"-"+file[11:])

            #Rename zip file according to the date of the first XML
            os.rename(directory +'/'+ file,directory +'/'+firstFile[:10]+"-"+file[11:])

        print (file) #Print previous file name

# move all files to the destination folder
for file in os.listdir(directory):

    src_file = os.path.join(directory, file)
    dst_file = os.path.join(destination, file)
    shutil.move(src_file, dst_file)

print ("all files treated and placed to the destination directory!")