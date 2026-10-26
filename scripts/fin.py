import subprocess,sys
n=sys.argv[1]
dur={"1":51.5,"2":48.2,"3":45.25}[n]
fc=(f"[0:v]subtitles=sub{n}.ass:fontsdir='C\:/Windows/Fonts',eq=contrast=1.04:saturation=1.1[v0];"
    "[1:v]format=rgba,colorchannelmixer=aa=0.9[lg];[v0][lg]overlay=(W-w)/2:90,format=yuv420p[v]")
subprocess.run(["ffmpeg","-v","error","-y","-i",f"visual{n}.mp4","-i","logo_sh.png","-i",f"v{n}.mp3","-filter_complex",fc,"-map","[v]","-map","2:a","-af","loudnorm=I=-16:TP=-1.5","-c:v","libx264","-crf","21","-preset","medium","-c:a","aac","-b:a","192k","-t",str(dur),"-movflags","+faststart",f"r{n}.mp4"],check=True)
