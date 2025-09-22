#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <math.h>
typedef uint8_t uint8;
void solve(int caseNuim);
int main(int argc, char* argv[])
{
	int ndata;
	scanf("%d", &ndata);
	for (int asdf = 0; asdf < ndata; asdf++)
	{
		solve(asdf + 1);
	}
	return 0;
}
void solve(int caseNum)
{
	int nflavors;
	scanf("%d", &nflavors);
	uint8* sold = calloc(sizeof(uint8), nflavors);
	int* preferred = calloc(sizeof(int), nflavors);
	for (int i = 0; i < nflavors; i++)
	{
		int count;
		int leastPopular = -1;
		scanf("%d", &count);
		if (count < 0)
		{
			printf("ERROR: received count of %d\n", count);
			return;
		}
		for (int j = 0; j < count; j++)
		{
			int preference;
			scanf("%d", &preference);
			preferred[preference]++;
			if (!sold[preference] &&
				((leastPopular < 0) || (preferred[preference] < preferred[leastPopular])))
			{
				leastPopular = preference;
			}
		}
		printf("%d\n", leastPopular);
		fflush(stdout);
		if (leastPopular >= 0)
		{
			sold[leastPopular] = 1;
		}
	}
	free(preferred);
}