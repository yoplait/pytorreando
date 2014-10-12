# variables= {}
# execfile( "someFile.py", variables )
# print variables # globals from the someFile module
def display_results(results, count=5):
    if (results) < count: count = len(results)

    for i in range(0, count):
        print results[i],

data=[1,2,3,4,5,6,7]
display_results(data)
print
display_results(data, len(data))
