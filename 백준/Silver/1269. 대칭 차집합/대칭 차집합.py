import sys
input = sys.stdin.readline

input()
sys.stdout.write(str(len(set(input().split())^set(input().split())))+"\n")
