variable = 'hello world'
variable2 = "haldo waldo"

print variable
print variable2
print 'first: %(variable)s' % {'variable': variable}
print "second: %(variable2)s" % {'variable2': variable2}
print "format: {} | {}".format(variable, variable2)
