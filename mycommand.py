# /Users/cat/myfile/github/lldb/mycommand.py

import lldb
import re

def __lldb_init_module (debugger, dict):
  debugger.HandleCommand('command script add -f mycommand.getAll getAll')

def getValue(x):
    value = lldb.frame.EvaluateExpression(x)
    if (value.TypeIsPointerType()):
        ret = value.GetObjectDescription()
    else:
        ret = value.GetValue()
    if ret:
        return ret
    else:
        return "Not Found"

def parseVarString(string):
    objs = re.findall("\\{.*?\\}", string)
    objs = map(lambda x: x.replace('{','').replace('}',''), objs)
    objs = map(lambda x: getValue(x), objs)
    base = re.sub("\\{.*?\\}", "%s", string)

    return base % tuple(objs)

def logv(extra=''):
    fun = lldb.frame.GetFunctionName()
    line = lldb.frame.GetLineEntry().GetLine()
    print '%s [Line %d] %s' % (fun, line, parseVarString(extra))

def log(extra):
    print parseVarString(extra)

def getAll():
    print "load my command" 
    #print lldb.frame.get_all_variables()
