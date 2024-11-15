arr=[input() for _ in range(5)]
f=[*filter(lambda i: "FBI" in arr[i-1], range(1, 6))]
print((" ".join(map(str,f)), "HE GOT AWAY!")[not f])
