from fetcher import Fetcher
from customexceptions import ArgsException
from subprocess import Popen, PIPE
import sys
import os

#Arguments: path/web.config path/dump.sql path/mysqldump.exe
def main():
    args = sys.argv[1:]
    commandandarguments = Fetcher().CommandAndArguments(getWebConfigPath(args), 
                                                        getApp(args))

    dumpfilepath = getDumpFilePath(args)
    executeCommandAndArguments(commandandarguments, dumpfilepath);

def executeCommandAndArguments(caa, dumpfilepath):
    result = Popen(caa, stdout=PIPE).stdout

    dumpfile = open(dumpfilepath, 'w')
    dumpfile.write( result.read() )
    dumpfile.close()
    result.close()

def validateArgsLen(args, length):
    if len(args) != length:
        exceptionMsg = 'Was expecting {0} arguments but got {1}'.format( length, len(args) )
        raise ArgsException, exceptionMsg

def getWebConfigPath(args):
    """1st argument should be the path to the web.config"""
    print args
    try:
        path = args[0]
    except:
        raise ArgsException, 'Web.config argument was missing'
    
    if not 'web.config' in path.lower():
        raise ArgsException, 'First argument should be the path to the web.config'

    return path 

def getDumpFilePath(args):
    """2nd argument should be the path to the dump file."""

    try:
         path = args[1]
    except:
        raise ArgsException, 'Second argument (dump file) was not found'
    
    return path 

def getApp(args):
    """3rd argument should be the application to create the dump file. Don't
    check for mysqldump cause might support other applications in future."""

    try:
         return args[2]
    except:
        raise ArgsException, '3rd argument should be the application(path) for creating the sql backup'

if __name__ == '__main__':
    main()
