import timeit
import pprint

# iterkeys items versus just dict

d = 'd = dict(zip(xrange(1000),xrange(1000)))'


comparisons = {
    'dict iteration':{
        'in dict': '''
for i in d:
    pass
''',
        'iteritems': '''
for i, j in d.iteritems():
    pass
'''     
},
    'list creation': {
        'looped append': '''
l = []
for i in xrange(1000):
    l.append(i)
''',
        'comprehension': '''
l = [i for i in xrange(1000)]
'''
},
    'ranges': {
        'range': '''
for i in range(1000):
    pass
''',
        'xrange': '''
for i in xrange(1000):
    pass
''',
},
    'looped concat vs join comprehension': {
        'concats': '''
ayes = ''
for i in xrange(1000):
    ayes += 'i'
''',       
        'join string method': '''
ayes = ''.join(['i' for i in (xrange(1000))])
''',
},
}

resultdict = {}
for i in comparisons:
    resultsubdict = {}
    for j in comparisons.get(i):
        context = timeit.Timer(
                stmt=comparisons.get(i).get(j),
                setup=d)
        results = context.repeat(repeat=10, number=1000)
        resultsubdict[j] = min(results)
        print j, min(results)
    resultdict[i] = resultsubdict
pprint.pprint(resultdict)

for i, j in resultdict.iteritems():
    values = list(j.itervalues())
    fastesttime = min(values)
    values.remove(fastesttime)
    secondfastesttime = min(values)
    slowesttime = max(values)
    slowestmethod = fastestmethod = ''
    for k, v in j.iteritems():
        if v == fastesttime:
            fastestmethod = k
        if v == slowesttime:
            slowestmethod = k
    percentfaster = (((slowesttime/fastesttime) - 1)*100)
##    if len(j) > 2:
    print ('fastest method for {item} is {fastest}, '
          'which is {percentfaster} percent faster than {slowest}, '
          ''.format(item=i, fastest=fastestmethod,
                    slowest=slowestmethod,
                    percentfaster=percentfaster))
##    for j in resultdict.get(i):



    
