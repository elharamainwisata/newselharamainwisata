import subprocess,os,sys
H=r"D:\newshaji\haji_drive"; U=r"D:\newshaji\umrah"
FC="scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,fps=30,format=yuv420p,setsar=1"
AR=[("ar_0827",3.8),("ar_0837",8.1),("ar_0846",6.1),("ar_0849",4.6),("ar_0840",3.2),("ar_0858",3.6),("ar_0864",4.0),("ar_0867",4.1),("ar_0829",2.5),("ar_0852",3.1),("ar_0855",3.4),("ar_0870",3.2),("mi_0909",5.3)]
TENT=lambda order:[(f"{H}\{n}.mov",0,min(d,4.2)) for n,d in order]
def umr(lst): return [(f"{U}\{u}.mp4",s,4.0) for u,s in lst]
tag=sys.argv[1]; need=float(sys.argv[2])
if tag=="1":
    T=[AR[i] for i in (0,2,4,5,1,3,6,7,9,10)]
    seq=TENT(T[:8])+[("c05.mp4",0,None),("c06.mp4",0,None),("c12.mp4",0,None)]+TENT(T[8:])+umr([("u15",24),("u13",41),("u09",6),("u11",30),("u03",14),("u02",0),("u08",12),("u14",6),("u13",20),("u15",40),("u09",44)])
elif tag=="2":
    seq=umr([("u15",24),("u13",41),("u02",0),("u09",6),("u11",30)])+TENT([AR[i] for i in (3,6,0,5,7,2,1,4,8,9,10,11,12)])+umr([("u08",12),("u14",6),("u03",14),("u16",10),("u12",5),("u15",5)])
else:
    seq=umr([("u15",24),("u13",41),("u03",14),("u02",0),("u09",6),("u11",30),("u13",8),("u15",5),("u03",35),("u02",30),("u09",30),("u11",6),("u08",12),("u14",6),("u16",10),("u12",5),("u15",40),("u13",20),("u09",44),("u03",2),("u02",15),("u11",18),("u14",30),("u08",30)])
os.makedirs(f"cuts{tag}",exist_ok=True); lst=[];tot=0
for i,(f,s,d) in enumerate(seq):
    if tot>=need: break
    out=f"cuts{tag}/c{i:02d}.mp4"
    if f.endswith("mp4") and "\\" not in f:  # prebuilt
        out=f; dd=3.9
    else:
        subprocess.run(["ffmpeg","-v","error","-y","-ss",f"{s:.2f}","-t",f"{d:.2f}","-i",f,"-vf",FC,"-an","-c:v","libx264","-crf","17","-preset","ultrafast",out],check=True); dd=d
    lst.append(out); tot+=dd
print(tag,len(lst),round(tot,1))
open(f"list{tag}.txt","w").write("".join(f"file '{p}'\n" for p in lst))
subprocess.run(["ffmpeg","-v","error","-y","-f","concat","-safe","0","-i",f"list{tag}.txt","-c","copy",f"visual{tag}.mp4"],check=True)
