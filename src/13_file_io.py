"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# YOUR CODE HERE
#open the file assign to f, then read it into read_data, print.
f = open("foo.txt", "r")
read_data = f.read()
print(read_data)
f.close()
# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE

#open the file to read first 3 lines
with open('foo.txt') as myfile:
    heads = [next(myfile) for x in range(3)]
#write the first 3 lines into a bar.txt
with open('bar.txt', 'w') as writefile:
    writefile.writelines(heads)