import sys
"""
print('Hello World')

# They are the same
sys.stdout.write("Hello World\n")
"""

"""
# be careful here the error will print before the stdout
sys.stdout.write("Hello world")
sys.stderr.write("This is an error\n") 

"""



# print(input())

print(sys.stdin.read())