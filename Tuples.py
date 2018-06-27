name = raw_input("Enter file:")

#handle = open(name,'r')
#text = handle.read()
f_text = open(name)

counts = dict()

for line in f_text:
    line = line.rstrip()
    if not line.startswith("From "):
       continue
    words = line.split()
    sel_word = words[5]
    sel_time = sel_word.split(':')
    sel_hr = sel_time[0]
    #print sel_hr
    #for word in sel_hr:
    counts[sel_hr] = counts.get(sel_hr,0) +  1
    #print counts    
   
for (k,v) in sorted(counts.items()):
    print k, v
