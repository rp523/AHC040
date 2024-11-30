from pathlib import Path
import time, os
from subprocess import getoutput
def main():
    sum_score = 0
    norm = 0
    min_score = -1
    min_score_i = -1
    max_score = -1
    max_score_i = -1
    max_time = -1
    max_time_i = -1
    exe_path = Path("exec.exe")
    if exe_path.exists():
        os.remove(exe_path)
    getoutput("cargo fmt && cargo build -r && copy target\\release\\atcoder.exe {}".format(exe_path))
    for i in range(50):
        cmd = "tester.exe"
        #cmd += " python sample.py"
        cmd += " {}".format(exe_path)
        cmd += r" < tools\in\{0:04d}.txt".format(i)
        cmd += r" > tools\out\{0:04d}.txt".format(i)
        t0 = time.time()
        score = int(getoutput(cmd)[len("Score = "):])
        t1 = time.time()
        dt = int(1000 * (t1 - t0))
        if max_score < 0 or max_score < score:
            max_score = score
            max_score_i = i
        if min_score < 0 or min_score > score:
            min_score = score
            min_score_i = i
        if dt > max_time:
            max_time = dt
            max_time_i = i
        sum_score += score
        norm += 1
        print(i, score, dt, "AVE", int(sum_score / norm), "WORST", max_score_i, max_score, "BEST", min_score_i, min_score, "SLOW", max_time_i, max_time)

if __name__ == "__main__":
    main()