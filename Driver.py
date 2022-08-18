from SudokuGenerator import Generator

print('Welcome to my sudoku generator!')
print('It is designed to generate a fully complete Sudoku solution, '
      'then change it into a puzzle based on your desired difficulty')
a = (input('Enter 1 to continue: '))
if a == '1':
    Generator()
else:
    print('im sorry you dont want to play :(')
