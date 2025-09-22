#include <stdio.h>          
#include <stdbool.h>
const char NUL = '\0';
bool
ope_line()
{
	char oline[101];
	const char letter[6][5] = {"abcde", "fghij", "klmno", "pqrst", "uvwxy", "z.?! "};
	int c = getc(stdin);
	if (c == EOF)
		return false;
	if (c == '\n')
		return true;
	bool b_na = false;
	int ix = 0;
	while (c != '\n' && c != EOF)
	{
		int s = c - '1';
		c = getc(stdin);
		if (c == '\n' || c == EOF)
		{
			b_na = true;
			break;
		}
		int t = c - '1';
		oline[ix++] = letter[s][t];
		c = getc(stdin);
	}
	if (b_na)
		printf("NA\n");
	else
	{
		oline[ix] = NUL;
		printf("%s\n", oline);
	}
	if (c == EOF)
		return false;
	return true;
}
int
main(int argc, char **argv)
{
	while (true)
	{
		if (!ope_line())
			break;
	}
	return 0;
}