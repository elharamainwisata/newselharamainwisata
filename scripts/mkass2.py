import re,sys,json,difflib
n=sys.argv[1]
hdr=open("../work2/sub3_c.ass",encoding="utf-8").read().split("[Events]")[0]+"[Events]\nFormat: Layer,Start,End,Style,Name,MarginL,MarginR,MarginV,Effect,Text\n"
def ts(t):
    h=int(t//3600);m=int(t%3600//60);s=t%60
    return f"{h}:{m:02d}:{s:05.2f}"
norm=lambda w:re.sub(r"[^a-z0-9]","",w.lower())
ws=json.load(open(f"w{n}.json")); words=open(f"s{n}.txt",encoding="utf-8").read().split()
A=[norm(w[0]) for w in ws]; B=[norm(w) for w in words]
sm=difflib.SequenceMatcher(None,B,A,autojunk=False)
st=[None]*len(B); en=[None]*len(B)
for blk in sm.get_matching_blocks():
    for k in range(blk.size): st[blk.a+k]=ws[blk.b+k][1]; en[blk.a+k]=ws[blk.b+k][2]
# interpolate gaps
i=0;total=ws[-1][2]
while i<len(B):
    if st[i] is None:
        j=i
        while j<len(B) and st[j] is None: j+=1
        t0=en[i-1] if i>0 else 0.0; t1=st[j] if j<len(B) else total
        for k in range(i,j):
            st[k]=t0+(t1-t0)*(k-i)/(j-i); en[k]=t0+(t1-t0)*(k-i+1)/(j-i)
        i=j
    else: i+=1
ev=[];cur=[];
def flush():
    global cur
    if cur: ev.append((st[cur[0]],en[cur[-1]],cur_text())); cur=[]
def cur_text(): return " ".join(words[k] for k in cur)
for k in range(len(B)):
    if cur and (len(cur_text()+" "+words[k])>34 or (words[cur[-1]][-1] in ".?" )):
        flush()
    cur.append(k)
flush()
# make contiguous: extend each end to next start if gap<0.6
out=[]
for idx,(a,b,t) in enumerate(ev):
    if idx+1<len(ev) and ev[idx+1][0]-b<0.6: b=ev[idx+1][0]
    out.append((a,b,t))
with open(f"sub{n}.ass","w",encoding="utf-8") as f:
    f.write(hdr)
    for a,b,c in out: f.write(f"Dialogue: 0,{ts(a)},{ts(b)},Default,,0,0,0,,{c}\n")
print(n,len(out),sum(1 for s in sm.get_matching_blocks()),"matched words:",sum(b.size for b in sm.get_matching_blocks()),"/",len(B))
