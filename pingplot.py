#!/usr/bin/python
import sys
import matplotlib.pyplot as plt
from parse import *

def main():
	for arg in sys.argv[1:]:
		file = open(arg)
		pings = {}
		#Read from file, split into array of individual lines
		file = file.read()
		file = file.split('\n')
		file.pop(0)

		for line in file:
			if (line == ""):
				break

			result = parse("64 bytes from 216.58.194.206: icmp_seq={:d} ttl=54 time={:g} ms", line)
			if (result == None):
				result = []
				data = parse("Request timeout for icmp_seq {:d}", line)
				result.append(data[0])
				result.append(-1.000)
			pingNum = result[0]
			packetTime = result[1]
			pings[pingNum] = packetTime

		x = list(pings.keys())
		y = list(pings.values())
		plt.plot(x, y)
		plt.xlabel("Ping Number")
		plt.ylabel("Packet Time")
		plt.show()

if (__name__ == "__main__"):
    main()
