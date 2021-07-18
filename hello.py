
#score = input('Enter a score: ')
#i = float(score)

#if i >= 0.9:
    #print('A')
    #quit()
#if i >= 0.8:
   # print('B')
    #quit()
#if i >= 0.7:
    #print('C')
    #quit()
#if i >= 0.6:
    #print('D')
    #quit()
#if i >= 0.9:
    #print('F')
    #quit()
#elif i< 0.0 or i > 1.0:
    #print('Error')
#else:
    #print('DONE!')


#big = max('Hello world')
#tiny = min('Hello world')
#print(big)
#print(tiny)
#print(tiny)
def addtwo(a, b):
    added = a + b
    return a

x = addtwo(2, 7)
print(x)

def stuff():
    print('Hello')
    return
    print('World')

stuff()
def computepay(sh, sr):
    xh = input('Enter hours: ')
    xr = input('Enter rate: ')
    sh = float(xh)
    sr = float(xr)
    if sh > 40:
        reg = sh * sr
        otp = (sh - 40)*(sr*0.5)
        xp = reg + otp
    #return xp

#print('Pay',computepay(45, 10.50))
max_num = 0
ids = [45, 89, 3, 8, 93,78]
for i in ids:
    if i > max_num:
        max_num = i
#print('Maximum is:', max_num)

myCount = 0
ids = [45, 89, 3, 8, 93, 78]
for i in ids:
    myCount = myCount + 1
    #print(myCount, i)
    #break

mySum = 0
ids = [45, 89, 3, 8, 93, 78]
for i in ids:
    mySum = mySum + i
    #print(i, mySum)

count = 0
mySum = 0
ids = [45, 89, 3, 8, 93, 78]
for i in ids:
    mySum = mySum + i
    count = count + 1
    #print(count, i, mySum)
#print('Total is:', mySum,'and the Average is : ', mySum / count)

smallest = None
ids = [45, 89, 3, 8, 93, 78]
for i in ids:
    if smallest is None:
        smallest = i
    elif i < smallest:
        smallest = i
    #print('Minimum is:', smallest, i)

a = [4, 8, 9]
b = a
#print(b)
c = list(a)
#print(c)

num = 0
total = 0.0
#while True:
 #   sval = input('Enter a number: ')
  #  if sval == 'done':
   #     break
    #try:
     #   fval = float(sval)
    #except:
        #print('Invalid input')
     #   continue
    #num = num + 1
    #total = total + fval
#print('All Done!')
#print(total, num, total/num)



num = 0
average = 0.0
total = 0.0
deviatons = 0
dev_squares = 0
total_deviations_squares = 0
variance = 0
#while True:
    #data = input('Enter a digit: ')
    #if data == 'done':
        #break
    #try:
        #fdata = float(data)
    #except:
        #print('Invalid Input')
        #continue
    #num = num + 1
    #total = total + fdata
    #average = total / num
    #deviatons = fdata - average
    #dev_squares = deviatons ** 2
    #total_deviations_squares = total_deviations_squares + dev_squares
    ##variance = total_deviations_squares/ num
    
#print('All done')
#print(num, total,average, variance )


#largest = None
#smallest = None
#while True:
    #num = input('Enter a number: ')
    #if num == 'done':
        #break
    #try:
        #fnum = float(num)
    #except:
        #print('Invalid input')
        #continue
    #if smallest is None:
        #smallest = fnum
    #elif fnum < smallest:
        #smallest = fnum
    #if largest is None:
        #largest = fnum
    #elif fnum > largest:
        #largest = fnum
#print( 'Maximum is: ', largest)
#print( 'Minimum is: ', smallest)

def computepay(h, r):
    xh = input('Enter hours: ')
    xr = input('Enter rate: ')
    h = float(xh)
    r = float(xr)
    if h > 40:
        reg = h * r
        otp = (h - 40)*(r*0.5)
        xp = reg + otp
    return xp

#print('Pay',computepay('h','r'))

#name = input('What is your name? ')
#color = input('What is your favourate color? ')

#print(name, 'likes', color)

#birth_year = input('What is your birth year? ')
#fyr = int(birth_year)
#age = 2021 - fyr

#print('You are', age , 'years old')

#name = 'YUSSIF ABDUL SALAM'
#let = name['']
#print(let)
#print(name[-5])
#while name[-1]> let: 

#name = 'Jennifer'
#print(name[1:-1])

#index = 0
#while index < len(name):
    ##letter = name[index]
    #(letter)
    #index = index -1

greet = '  hello every body.  '

greet_new = greet.replace('l', 'x')
#print(greet_new)
istp = greet_new.lstrip()
#print(istp)
rpst = greet_new.rstrip()
#print(rpst)
#print('h' in greet_new)
#print('w' in greet_new)
str1 = "Hello"
str2 = 'there'
bob = str1 + str2
#print(bob)

x = '20'
y = int(x)+2
#print(y)

x = 'From marquard@uct.ac.za'

#print(x[14:17])

#print(len('banana') * 7)

data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
pos = data.find('.')
#print(data[pos:pos+3])

text = "X-DSPAM-Confidence:    0.8475"

n_found = text.find('0')
col = text.find(':')
#print(text.index[col])
#print(text[23:])

# Use the file name mbox-short.txt as the file name
#fname = input("Enter file name: ")
#fh = open(fname)
total = 0
count = 0
#for line in fh:
    #if line.startswith("X-DSPAM-Confidence:"):
        #print(line)
        #count = count + 1
        #x = line[19:]
        #y = float(x)
        #total = total + y
#print("Done", count, total/count )

name = ['Glenn', 'Hansel', 'skupper','Anatu']
name.sort()
#print(name[0])

t = [9, 41, 12, 3, 74, 15]
#print(t[2:4])

a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
#print(len(c))

#x = list(range(5))
#print(x)

fruit = 'Banana'
#fruit[0] = 'b'
#y = fruit.replace('B',b)
#print(y)

#fname = input("Enter file name: ")
#fh = open(fname)
#lst = list()    
#for line in fh:
    #lst = lst.append(fh, 'r')
    #lst.sp

obj = ['avu', 'crot', 'frot', '4', [4, 5, 8,]]
#um = range(len(obj))
#print(um)
obj.append('uvom')
#print(obj)

#print(range(4))

#numlist = list()
#while True:
    #inp = input('Enter a number: ')
    #if inp == 'done': break
    #value = float(inp)
    #numlist.append(value)

#print(sum(numlist)/len(numlist))


nMW = 'YUSSif abdul salam kironatogma alhassan'
#abc = nMW.split()
#print(abc)
#file_name = open('romeo.txt', 'r')
#print(file_name)

#fname = input('Enter file name: ')
#fh = open(fname)
#lst = list()
#for line in fh:
    # = line.rstrip()
    #line = line.split()
    #for word in line:
        #if word in lst: continue
        #else:
            #lst.append(word)
    #print(lst.sort())

#fname = input("Enter file name: ")
#fh = open(fname)
#lst = list()
#for line in fh:
    #line = line.rstrip()
    #lexis = line.split()
    #for i in range (len(lexis)):
        #if lexis[i] not in lst:
            #lst.append(lexis[i])

#lines = lst.sort()
#print (lst)

#fname = input("Enter file name: ")
#fhandle = open(fname)
#lst = list()
#for line in fhandle:
        #line = line.rstrip()
        #words = line.split()
        #for i in range (len(words)):
            #if words[i] not in lst:
                #lst.append(words[i])
#lst.sort()
#print (lst)

#fname = input('Enter file name: ')
#if len(fname) < 1:
    #fname = "learn.txt"
#fh=open(fname)
#count=0
#for line in fh:
    #line=line.rstrip()
    #if line.startswith('From '):
       # email=line.split()
    #count=count+1
    #print(email[1])

#print("There were", count, "lines in the file with From as the first word")

#fname = input("Enter file name: ")
#if len(fname) < 1 : fname = "learn.txt"

#fh = open(fname)
#count = 0

#for line in fh:
    #line = line.rstrip()
    #wds = line.split()
    #if not line.startswith('From '): continue
    #count = count + 1
    #print(wds[1])


#print('There were', count, 'lines in the file with From as the first word')

#items = dict()
#items['bag'] = 45
#items['money'] = 'Ghc 89.00'
#items['hancherchief'] = 87
#print(items)

#counts = dict()
#names = ['ama', 'yussif', 'latif', 'latif', 'mumuni', 'yussif', 'yussif', 'rakak', 'mumuni', 'sly', 'daniel']
#mode = 0
#lowest = None
#for name in names:
    #if name not in counts:
        #counts[name] = 1
   # else:
        #counts[name] = counts[name] + 1
    #if counts[name] > mode:
        #mode = counts[name]
#print(counts, 'the most appearing name is:', mode)

#jjj = {'nuoman': 45, 'ames':9, 'mathematics':87, 'apau':23, 'yison':9, 'kubo':46, 'sunnah':67}
#print(list(jjj))
#print(jjj.keys())
#print(jjj.values())
#print(jjj.items())

#fname = input('Enter a file name: ')
#fh = open(fname)
#counts = dict()

#for line in fh:
    #words = line.split()
    #for word in words:
        #counts[word] = counts.get(word, 0) + 1

#bigword = None
#bigcount = None
#for word, count in counts.items():
    #if bigword is None or count > bigcount:
        #bigword = word
        #bigcount = count
#print(bigword, bigcount)

#stuff = dict()
#print(stuff.get('candy',-1))

#lst = dict()
#lst["name"] = 'YUSSIF'
#lst['age'] = 28
#lst['colour'] = 'dark'
#lst['community'] = 'Wa'
#lst['car type'] = 'rangerover'
#myItems = lst.items()
#print(lst.keys())
#print(lst.values()) 
#for y in lst:
  #  print(y)
#print(myItems)
#stuff = dict()
#print(stuff['candy'])



#fname = input("Enter a file name: ")
#file = open(fname)
#email = dict()
#for line in file:
  #if line.startswith("From "):
    #words = line.split()
    #word = words[1]
    #email[word] = email.get(word,0) + 1

#mostMails = max(email, key=email.get)
#print(mostMails, email[mostMails])


mydict = {'a': 3, 'b': 4, 'c': 8}
#print(dir(mydict.items()))
#for v, k in sorted

days = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')
#print(days[2])
(x, y) = (3, 4)
#print(dir(days))

#print(x, y)

#fname = input("Enter a file name: ")
#file = open(fname)
#time = dict()
#count = 0
#for line in file:
  #if line.startswith("From "):
    #words = line.split()
    #hour = words[5]
    #time[hour] = time.get(hour, 0) + 1
    
        #count = count + 1
        #print(hr, count)



#fname = input("Enter a file name: ")
#file = open(fname)
#time = dict()
#x_list = list()
#time= dict()

#count = list
#for line in file:
   #if line.startswith("From "):
        #words = line.split()
        #colon_col = words[5]
         
        #h,m,s = colon_col.split(":")
        #x_list.append(h)

#for num in x_list:
    #time[num] = time.get(num, 0) + 1
    #if num not in time:
        #time[num] = 1
    #else:
        #time[num] += 1


#for key, val in list(sorted(time.items())):
   # print(key,val)


#name = input('Please enter your name in the box: ')
#fh = name
#age = input('Enter birth year: ')
#newAge = int(age)
#cal_age = 2021 - newAge
#cpt = fh.upper()
#msg = f'{cpt} is {cal_age} years old'
#print(msg)
nwq_Array = input('enter a digit: ')
fh = list(nwq_Array)
array = [ 45, 89, 34,78, 35, 23]
count = 0
sum_of_dig = 0
max_dig = 0
for i in fh:
    if i > max_dig:
        max_dig = i
    count = count + 1
    sum_of_dig = sum_of_dig +i
print(max_dig, count, 'average: ', sum_of_dig/count )



samples = [8, 4, 43, 8, 3, 87,2,3, 4,5, 6,]
samples.append(45)
print(samples)









