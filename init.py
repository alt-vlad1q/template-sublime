import os, sys

def change_project_name(filepath, project_name, file_template='template-sublime'):
    with open(filepath, 'r') as file :
        filedata = file.read()
    filedata = filedata.replace(file_template, project_name)
    with open(filepath, 'w') as file:
        file.write(filedata)
    file.close()

if len(sys.argv) != 2:
    print 'Usage:', sys.argv[0], ' [project_name]'
else:
    change_project_name('./CMakeLists.txt', sys.argv[1])
    change_project_name('./template.sublime-project', sys.argv[1])
    os.rename(r'./template.sublime-project', r'./' + sys.argv[1].lower() + '.sublime-project')
    os.rename(os.getcwd(), os.getcwd().replace("template-sublime", sys.argv[1]))
    os.system('git remote remove origin')