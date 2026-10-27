import subprocess, os, time
from narasi import V
import sys; sys.path.insert(0, r'D:\newshaji\work7'); import narasi_baru; V.update(narasi_baru.V)
import narasi_cerita; narasi_cerita.terapkan(V)

os.makedirs("seg", exist_ok=True)
for n in sorted(V):
    for i, (d, sp) in enumerate(V[n]["s"]):
        out = f"seg/v{n}_{i}.wav"
        if os.path.exists(out) and os.path.getsize(out) > 2000:
            continue
        t = time.time()
        subprocess.run(["curl", "-s", "-X", "POST", "http://127.0.0.1:3900/generate",
                        "-F", f"text={sp}", "-F", "profile_id=44861c7e", "-F", "language=Indonesian",
                        "-F", "seed=1163825626", "-o", out], check=True)
        print(n, i, round(time.time() - t, 1), os.path.getsize(out), flush=True)
print("TTSDONE", flush=True)

