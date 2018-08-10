#!/usr/bin/env python3 -B

import collections
import datetime
import itertools

Job = collections.namedtuple('Job', ['weight', 'length'])

print(datetime.datetime.now(), "Reading input...")
with open("jobs.txt") as f:
    jobs = [ Job(*[ int(n) for n in line.split() ]) for line in f.readlines()[1:] ]

print(datetime.datetime.now(), "Sorting jobs...")
jobs.sort(key = lambda job: (job.weight - job.length, job.weight), reverse = True)

print(datetime.datetime.now(), "Computing weighted sum of completion times...")
completion_times = itertools.accumulate([ job.length for job in jobs ])
weighted_sum = sum(job.weight * completion_time for job, completion_time in zip(jobs, completion_times))

print(weighted_sum)
