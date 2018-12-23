
# coding: utf-8

# In[ ]:

########## part1
files_ok = []
path = './../notes/Factors'
files = list_files(path)  
for filename in files:    
    if filename[0] <> '.':
        # print path + '/' + filename
        files_ok.append( path + '/' + filename )

path = './../notes/Archive'
files = list_files(path)  
for filename in files:    
    if filename[0] <> '.':
        # print path + '/' + filename
        files_ok.append( path + '/' + filename )
        
zip_files('backup1', files_ok)

########## part2
files_ok = []
path = './../notes/CodeSample'
files = list_files(path)  
for filename in files:    
    if filename[0] <> '.':
        # print path + '/' + filename
        files_ok.append( path + '/' + filename )
        
zip_files('backup2', files_ok)

########## part3 not downloaded
files_ok = []
path = './../notes/Reference'
files = list_files(path)  
for filename in files:    
    if filename[0] <> '.':
        # print path + '/' + filename
        files_ok.append( path + '/' + filename )
        
zip_files('backup3', files_ok)

########## part4
files_ok = []
path = './../notes'
files = list_files(path)  
for filename in files:    
    if filename[0] <> '.':
        # print path + '/' + filename
        files_ok.append( path + '/' + filename )
        
zip_files('backup4', files_ok)

########## part5
files_ok = []
path = './../lib'
files = list_files(path)  
for filename in files:    
    if filename[0] <> '.':
        print path + '/' + filename
        files_ok.append( path + '/' + filename )

zip_files('backup5', files_ok)

