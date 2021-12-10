import glob

def CreateAListofFileNames(path):
    return glob.glob(path)

def ListToFile(l, path):
    with open(path, 'w') as f:
        for item in l:
            f.write("%s\n" % item)
    
def Main():
    imageNames = CreateAListofFileNames('images\\*.jpg')
    print(imageNames)
    ListToFile(imageNames, 'image_list.txt')
    print('--end--')
    
if __name__ == '__main__':
    Main()


