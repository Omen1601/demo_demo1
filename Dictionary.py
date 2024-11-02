# Dictionary = A Changeable, unordered collection of unique key:value pairs
#              Fast Because they using Hashing, allow us to access a value quickly
Names = {'om':'waghmare',
         'ram':'eklare',
         'ajay':'sangewar',
         'daksh':'gautam'
         }

print(Names['ajay'])
print("\n",Names.get('kunnu'))              # .get()    if it is not available in Dict the print None
print("\n",Names.keys())                    # .keys()   all the keys
print("\n",Names.values())                  # .values() all the values
print("\n",Names.items())                   # .items()  all key:value

Names.update({'kunnu': 'Sahu'})             # .update() add new key:value pair
Names.update({'kunnu': 'Siddhu'})           # update() also change any key or value
Names.pop('daksh')                          # .pop() delete element and return index
print("\n")

for key,value in Names.items():
    print(key,value)

print("\n",Names.clear())