#include <stdio.h>
char temp[22][22];
int compt(int y, int x)
{
	if (temp[y][x])
	{
		temp[y][x] = 0;
		return 1 + compt(y-1, x) + compt(y+1, x)
		         + compt(y, x-1) + compt(y, x+1);
	}
	else return 0;
}
int main(int argc, char **argv)
{
	unsigned long int no_cases, case_no;
	scanf("%lu", &no_cases);
	for (case_no = 0; case_no != no_cases; case_no++)
	{
		int r, c, x, y, s;
		int best = 0;
		char grid[20][20];
		char extras[6] = {};
		char quads[16] = {1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1};
		scanf("%i%i", &r, &c);
		for (y = 0; y != r; y++)
		{
			while (getchar() != '\n') 
				{;} 
			int last = 2, this;
			for (x = 0; x != c; x++)
			{
				grid[y][x] = this = getchar() == 'W';
				extras[last << 1 | this] = 1;
				last = this;
			}
			temp[y][0] = temp[y][c+1] = 0;
		}
		for (x = 0; x != c; x++) 
			temp[0][x] = temp[r+1][x] = 0;
		quads[10] |= extras[2];
		quads[5] |= extras[1];
		for (y = 1; y != r; y++)
			for (x = 1; x != r; x++)
				quads[grid[y-1][x-1] << 3 | grid[y-1][x] << 2 | grid[y][x-1] << 1 | grid[y][x]] = 1;
		for (y = 1; y != r; y++)
			for (x = 0; x != r; x++)
			{
				int j = grid[y-1][x] << 2 | grid[y][x];
				quads[j << 1 | j] = 1;
			}
		for (int q = 0; q != 16; q++)
			if (quads[q])
				for (int ydiv = 0; ydiv <= r; ydiv++)
					for (int xdiv = 0; xdiv <= c; xdiv++)
					{
						for (y = 0; y != r; y++)
							for (x = 0; x != c; x++)
							{
								temp[y+1][x+1] = grid[y][x] == (q >> ((y < ydiv) << 1 | (x < xdiv)) & 1);
							}
						for (y = 0; y != r; y++)
							for (x = 0; x != c; x++)
							{
								s = compt(y + 1, x + 1);
								if (s > best) 
									best = s;
							}
					}
		printf("Case #%lu: %i\n", case_no + 1, best);
	}
	return 0;
}