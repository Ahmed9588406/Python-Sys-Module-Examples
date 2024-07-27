import sys

"""
# return the max integer size we can use
print("Max int size:",sys.maxsize)
"""


"""
# Command line argument
print("Sys args:",sys.argv)
"""

print(sys.argv)
# output : ['c:/Users/ak958/OneDrive/Desktop/Python-Sys-Module-Examples/sys.py']
# and we can add argument by python sys.py arg arg2
# output : ['sys.py', 'arg', 'arg2']

def function1():
    print ('First function')

def function2():
    print("second function")

arguments = sys.argv[1:]

if len(arguments) != 1:
    print(f"ERROR: 1 argument expected {len(arguments)} given")
    sys.exit()

"""
python sys.py arg arg2
['sys.py', 'arg', 'arg2']
ERROR: 1 argument expected 2 given

"""



argument = arguments[0]

if argument == 'f' or argument == 'first':
    function1()

elif argument == 's' or argument == 'second':
    function2()

else:
    print(f"ERROR: {argument} not available!")

