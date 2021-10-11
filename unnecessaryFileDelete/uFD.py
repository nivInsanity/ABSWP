import os, send2trash

def bytesToMegabytes(byte):

    megabyte = 0.000001 * byte
    return megabyte

def scanAndDelete():

    for root, dirs, files in os.walk('E:\\testPath'):
        for file in files:
            path = os.path.join(root, file)
            size = os.stat(path).st_size
            convertedSize = bytesToMegabytes(size)

            if convertedSize > 100:
                print('Found unnecessary file, size of it is: ' + str(size) + ' \nPath of file is: ' + path)
                send2trash.send2trash(path)
                print('File deleted.')

    print('All unnecessary files send to bin from hard disk or not found.')

scanAndDelete()