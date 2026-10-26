import subprocess,numpy as np,json
from faster_whisper import WhisperModel
m=WhisperModel("small",device="cpu",compute_type="int8")
for i in (1,2,3):
    b=subprocess.run(["ffmpeg","-v","error","-i",f"v{i}.mp3","-ac","1","-ar","16000","-f","f32le","-"],capture_output=True).stdout
    segs,_=m.transcribe(np.frombuffer(b,dtype=np.float32),language="id",vad_filter=True,word_timestamps=True)
    ws=[(w.word.strip(),w.start,w.end) for s in segs for w in s.words]
    json.dump(ws,open(f"w{i}.json","w"))
    print(i,len(ws))
