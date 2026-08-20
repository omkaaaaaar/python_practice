from collections import namedtuple
from collections import deque
from collections import Counter
from collections import defaultdict
from collections import OrderedDict


person = namedtuple('Person', ['name','age'])
s1 = person('Mohit', 30)
print(s1)
print(s1.name)


dq = deque([1,2,3,4,5])
dq.append(6)
dq.appendleft(0)
print("List afer Deque appending:",dq)
dq.pop()
dq.popleft()
print("List after pop", dq)


text = "apple banana apple orange banana apple"
count = Counter(text)
print("Word Counts:",count)
print(count['p'])
count = Counter(text.split())
print(count)
print(count["apple"])


score = defaultdict(int) #it means/int means that the variable which gets stored in the score it should be storerd/shown as an integer
score['math']=40 #this means that default score for math is 90, if students score above it then they'll get pass, if they score below 90 they'll fail
score['science']=35
print (score)
marks = int(input("Enter the Marks "))
if marks < score['math']:
    print("fail")
else:
    print("pass")    

if marks < score['science']:
    print("fail")
else:
    print("pass")  


od = OrderedDict()
od['apple']=1
od['banana']=2
print(od)