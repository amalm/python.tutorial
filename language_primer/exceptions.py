def throw_it():
    raise Exception('oh no')

throw_it()

try:
    throw_it()
except Exception as e:
    print(e)
