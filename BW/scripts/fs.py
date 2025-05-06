import os

os.makedirs('new_folder', exist_ok = True)

print(os.path)

file_path = os.path.join('new_folder', 'demo.txt')

with open(file_path, 'a') as f:
    f.write('hello guys')


with open(file_path,'a') as f:
    f.write('\n\neeee guys')

with open(file_path,'r') as f:
    content = f.read()
    print(content)




