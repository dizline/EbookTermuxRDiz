#!/usr/bin/python2


print "\nMasukkan File Yang Mau Di EnPyc"
print "\033[31m-----------------------------------------------------"

py_file = raw_input("\033[33m[File.Py]:> \033[0m")
from py_compile import compile
compile(py_file)
print
print "\033[32mSukses file Di Di Simpan:\033[0m {}c".format(py_file)
exit()