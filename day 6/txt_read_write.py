# working with text files
# try:
#     # f = open('notes.txt', 'r', encoding='utf-8')
#     # content = f.read()

#     # print(content)
#     # f.close()

#     with open('notes.txt', 'r', encoding='utf-8') as f:
#         content = f.read()
#         print(content)
# except FileNotFoundError as ex:
#     print('Error: ', ex)

lines = ['Reading text files\n', 'Writing text files\n', 'Working with Python Files\n', 'Writing into a text file\n', 'Handling file exceptions\n', 'Adding one more line here\n']

new_lines = ['testing how append more works\n']

try:
    with open('sample.txt', 'w', encoding='utf-8') as f:
        for line in new_lines:
            f.write(line)

        # f.writelines(lines)
    
    print("Writing done")
        # print(content)
except FileNotFoundError as ex:
    print('Error: ', ex)