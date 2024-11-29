import time
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
    for i in range(10000):
        cmd = "tester.exe"
        cmd += " python sample.py"
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
        print(i, score, "AVE", int(sum_score / norm), "WORST", max_score_i, max_score, "BEST", min_score_i, min_score, "SLOW", max_time_i, max_time)

if __name__ == "__main__":
    main()