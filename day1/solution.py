from os import read
import pathlib

def findNumberOfSlidingWindowIncreases(lines, sizeOfWindow = 3):
    increaseInDepth = 0
    numberOfWindows = range(len(lines) - sizeOfWindow + 1)
    previousWindowDepth = 0
    for window in numberOfWindows:
        depthsInWindow = lines[window:window+sizeOfWindow]
        currentWindowDepth = 0
        for depth in depthsInWindow:
            currentWindowDepth+=int(depth)
        if (previousWindowDepth != 0 and currentWindowDepth > previousWindowDepth):
            increaseInDepth += 1
            print("++ position: {0:d}, current depth: {1:d}, previous depth: {2:d}, depths {3}".format(window, currentWindowDepth, previousWindowDepth, depthsInWindow))
        else:
            print("position: {0:d}, current depth: {1:d}, previous depth: {2:d}, depths {3}".format(window, currentWindowDepth, previousWindowDepth, depthsInWindow))
        previousWindowDepth = currentWindowDepth
    return increaseInDepth

# Get input contents
with open(pathlib.Path(__file__).parent / 'input.txt') as input:
    contents = input.read()

    lines = contents.splitlines()

    numberOfIncreases = findNumberOfSlidingWindowIncreases(lines, 1)
    numberOfIncreasesForSlidingWindow = findNumberOfSlidingWindowIncreases(lines)

    print("--------------------------------------------------------------")
    print("Solutions")
    print("The depth increased {:d} times. ".format(numberOfIncreases))
    print("The sliding window depth increased {:d} times. ".format(numberOfIncreasesForSlidingWindow))
    print("--------------------------------------------------------------")