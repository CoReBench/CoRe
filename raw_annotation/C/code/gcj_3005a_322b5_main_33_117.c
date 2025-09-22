#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdarg.h>
#include <math.h>
char* readline() {
	size_t bufLen = 1024, dataLen = 0;
	char* data = malloc(bufLen);
	while (1) {
		char* cursor = data + dataLen;
		char* line = fgets(cursor, bufLen - dataLen, stdin);
		if (!line) { break; }
		dataLen += strlen(cursor);
		if (dataLen < bufLen - 1 || data[dataLen - 1] == '\n') { break; }
		size_t new_length = bufLen << 1;
		data = realloc(data, new_length);
		if (!data) { break; }
		bufLen = new_length;
	}
	if (data[dataLen - 1] == '\n') {
		data[dataLen - 1] = '\0';
	}
	else
	{
		dataLen++;
		data[dataLen - 1] = '\0';
	}
	data = realloc(data, dataLen);
	return data;
}
int G[1000][1000];
int targetX, targetY;
void main(int argc, char **argv)
{
	unsigned int u_w;
	int T;
	char *str;
	char *retStr;
	str = readline();
	sscanf(str, "%d", &T);
	free(str);
	u_w = 1;
	while (T-- != 0)
	{
		int R, C, H, V;
		int i, j, k, l, m;
		char *Waffle[10];
		int ChocChipCount[10];
		for (i = 0; i < 10; i++)
			ChocChipCount[i] = 0;
		str = readline();
		sscanf(str, "%d %d %d %d", &R, &C, &H, &V);
		free(str);
		for (i = 0; i < R; i++)
		{
			Waffle[i] = readline();
			for (j = 0; j < C; j++)
			{
				if (Waffle[i][j] == '@')
				{
					ChocChipCount[i]++;
				}
			}
		}
		retStr = "IMPOSSIBLE";
		for (i = 1; (i < R && (strcmp(retStr, "IMPOSSIBLE") == 0)); i++)
		{
			int topCount, bottomCount;
			int topleftCount, toprightCount;
			int bottomleftCount, bottomrightCount;
			topCount = 0;
			bottomCount = 0;
			for (j = 0; j < i; j++)
				topCount += ChocChipCount[j];
			for (j = i; j < R; j++)
				bottomCount += ChocChipCount[j];
			if (topCount != bottomCount)
				continue;
			else
			{
				for (k = 1; k < C; k++)
				{
					topleftCount = 0;
					toprightCount = 0;
					for (l = 0; l < i; l++)
					{
						for (m = 0; m < k; m++)
							if (Waffle[l][m] == '@')
								topleftCount++;
						toprightCount += ChocChipCount[l];
					}
					toprightCount -= topleftCount;
					if (topleftCount == toprightCount)
					{
						bottomleftCount = 0;
						bottomrightCount = 0;
						for (l = i; l < R; l++)
						{
							for (m = 0; m < k; m++)
								if (Waffle[l][m] == '@')
									bottomleftCount++;
							bottomrightCount += ChocChipCount[l];
						}
						bottomrightCount -= bottomleftCount;
						if (bottomleftCount == bottomrightCount)
						{
							retStr = "POSSIBLE";
							break;
						}
					}
				}
			}
		}
		printf("Case #%d: %s", u_w, retStr);
		u_w++;
	}
}