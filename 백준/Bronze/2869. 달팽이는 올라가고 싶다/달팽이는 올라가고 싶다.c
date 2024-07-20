int main() {
	int up, down, height;
	scanf("%d %d %d",&up, &down, &height);

	height -= up;
	int day = 1;

	if (height < 0) {
		printf("%d", day);
		return 0;
	}

	day += height / (up - down);
	
	if (height%(up-down)) {
		day += 1;
	}
	printf("%d", day);
	return 0;
}