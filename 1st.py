Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import builtins
>>> dir(builtins)
['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 'BlockingIOError', 'BrokenPipeError', 'BufferError', 'BytesWarning', 'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError', 'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning', 'EOFError', 'Ellipsis', 'EnvironmentError', 'Exception', 'False', 'FileExistsError', 'FileNotFoundError', 'FloatingPointError', 'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError', 'ImportWarning', 'IndentationError', 'IndexError', 'InterruptedError', 'IsADirectoryError', 'KeyError', 'KeyboardInterrupt', 'LookupError', 'MemoryError', 'ModuleNotFoundError', 'NameError', 'None', 'NotADirectoryError', 'NotImplemented', 'NotImplementedError', 'OSError', 'OverflowError', 'PendingDeprecationWarning', 'PermissionError', 'ProcessLookupError', 'RecursionError', 'ReferenceError', 'ResourceWarning', 'RuntimeError', 'RuntimeWarning', 'StopAsyncIteration', 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError', 'SystemExit', 'TabError', 'TimeoutError', 'True', 'TypeError', 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError', 'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning', 'ValueError', 'Warning', 'WindowsError', 'ZeroDivisionError', '__build_class__', '__debug__', '__doc__', '__import__', '__loader__', '__name__', '__package__', '__spec__', 'abs', 'all', 'any', 'ascii', 'bin', 'bool', 'breakpoint', 'bytearray', 'bytes', 'callable', 'chr', 'classmethod', 'compile', 'complex', 'copyright', 'credits', 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'exit', 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass', 'iter', 'len', 'license', 'list', 'locals', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property', 'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip']
>>> print("Hello")
Hello
>>> print=10
>>> print
10
>>> print("hek")
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    print("hek")
TypeError: 'int' object is not callable
>>> builtins.print("hey")
hey
>>> del print
>>> print("hey there")
hey there
>>> import keyword
>>> print(keyword.kwlist)'
SyntaxError: EOL while scanning string literal
>>> print(keyword.kwlist)
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
>>> import os
>>> os.getcwd()
'C:\\Python\\Python37-32'
>>> os.listdir()
['DLLs', 'Doc', 'include', 'Lib', 'libs', 'LICENSE.txt', 'NEWS.txt', 'python.exe', 'python3.dll', 'python37.dll', 'pythonw.exe', 'Scripts', 'tcl', 'Tools', 'vcruntime140.dll']
>>> os.mkdir("New")
>>> os.listdir()
['DLLs', 'Doc', 'include', 'Lib', 'libs', 'LICENSE.txt', 'New', 'NEWS.txt', 'python.exe', 'python3.dll', 'python37.dll', 'pythonw.exe', 'Scripts', 'tcl', 'Tools', 'vcruntime140.dll']
>>> os.rename("New","New_Folder")
>>> os.listdir()
['DLLs', 'Doc', 'include', 'Lib', 'libs', 'LICENSE.txt', 'NEWS.txt', 'New_Folder', 'python.exe', 'python3.dll', 'python37.dll', 'pythonw.exe', 'Scripts', 'tcl', 'Tools', 'vcruntime140.dll']
>>> os.rmdir("New_Folder")
>>> os.listdir()
['DLLs', 'Doc', 'include', 'Lib', 'libs', 'LICENSE.txt', 'NEWS.txt', 'python.exe', 'python3.dll', 'python37.dll', 'pythonw.exe', 'Scripts', 'tcl', 'Tools', 'vcruntime140.dll']
>>> for i in range(10):print(i)

0
1
2
3
4
5
6
7
8
9
>>> for i in range(10):print(i,end=',')

0,1,2,3,4,5,6,7,8,9,
>>> for i in range(1,22):
	os.mkdir("participate_"+str(i))
	os.chdir("participate_"+str(i))
	for j in range(1,21)
	
SyntaxError: invalid syntax
>>> for i in range(1,22):
	os.mkdir("participant_"+str(i))
	os.chdir("participant_"+str(i))
	for j in range(1,21):
		os.mkdir("days_"+str(j))
	os.chdir(os.pardir)

	
>>> 
