import re 

sourceFile = open('c:\\work\\PV3.txt','rt')
copyFile = open('c:\\work\\PV3_copy.txt','wt',encoding='utf-8')

#많은 라인의 파일이면 
#한번에 한줄씩 읽어서 처리한다.  
#파일의 EOF(End Of File)이 아니면 계속 읽도록 한다. 
line = sourceFile.readline()
while (line != ''):
    if (re.search("\d{4}", line)):
        copyFile.write(line)
    line = sourceFile.readline()

sourceFile.close() 
copyFile.close()

print("작업 완료")






