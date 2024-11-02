# Loop control statements = change a loop execution from it's normal sequence

# break =           used to terminate the loop entirely
# continue =        skips to the next iteration of the loop
# Pass =            does nothing, act as a placeholder

#-------------------------------------------------------------------
while True:
    name = input("Enter your name: ")
    if name != "":
        break
#-------------------------------------------------------------------

phn_no = "123-456-7890"
for i in phn_no:
    if i =="-":
        continue
    print(i,end=" ")
#-------------------------------------------------------------------

for i in range(1,30):
    if i == 13:
        pass
    else:
        print(i,end=" ")