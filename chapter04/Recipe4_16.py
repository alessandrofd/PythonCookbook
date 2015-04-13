# Recipe 4.16. Replacing Infinite while Loops with an Iterator
#
# Problem: You have a code that uses a while loop to iteratively process data because it involves a function or some
#   kind of unusual test condition that doesn't fall into the usual iteration pattern.
#
# Solution: A somewhat common scenario is porgrams involving I/O is to write code like this:
#
#     CHUNKSIZE = 8192
#
#     def reader(s):
#         while True:
#             data = s.recv(CHUNKSIZE)
#             if data == b'':
#                 break
#             process_data(data)
#
# Such code can often be replaced using iter(), as follows:
#
# def reader(s):
#     for chunk in iter(lambda: s.recv(CHUNKSIZE), b''):
#         process_data(data)
#
# If you're a bit skeptical that it might work, you can try a similar example involving files. For example:

import sys
f = open('passwd.txt')
for chunk in iter(lambda: f.read(10), ''):
    n = sys.stdout.write(chunk)

# DISCUSSION
#
# A little-known feature of the built-in iter() function is that it optionally accepts a zero-argument callable and
# sentinel (terminating) value as inputs. When used in this way, it creates an iterator that repeatedly calls the
# supplied callable over and over again until it returns the value given as a sentinel.
#
# This particular approach works well with certain kinds of repeatedly called functions, such as those involving I/O.
# For example, if you want to read data in chunks from sockets or files, you usually have to repeatedly execute read()
# or recv() call followed by an end-of-file test. This recipe simply takes these two features and combines them together
# into a single iter() call. The use of lambda in the solution is needed to create a callable that takes no arguments,
# yet still supplies the desired size argument to recv() or read().