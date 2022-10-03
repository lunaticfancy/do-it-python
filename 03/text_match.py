import os
print("\n\n"+os.getcwd())
os.chdir(r'C:\Users\lunat\OneDrive\문서\python_doitself\test files')
print("\n\n"+os.getcwd())
f = open('a.txt', 'w')
f.write('나는 오늘 학교에 갔다.')
f.close()
f = open('a.txt', 'r')
print(f.read())
f.close()
with open('a.txt', 'w') as f:
    f.write('나는 오늘 학교에 안 갔다.')

f = open('a.txt', 'r')
print(f.read())
