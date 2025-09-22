#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <inttypes.h>
#define NDEBUG
#define MAX(a, b) (((a) > (b)) ? (a) : (b))
#define MIN(a, b) (((a) < (b)) ? (a) : (b))
#define ABS(a) (((a) < (0)) ? -(a) : (a))
#define SGN(a) (((a) < 0) ? -1 : ((a) > 0))
#define UPDATEMAX(a, b) (((a) < (b)) ? (((a) = (b)), 1) : 0)
#define UPDATEMIN(a, b) (((a) > (b)) ? (((a) = (b)), 1) : 0)
#define SWAP(a, b) { char SWAP_tmp[sizeof(a)]; memcpy(SWAP_tmp, &(a), sizeof(a)); (a) = (b); memcpy(&(b), SWAP_tmp, sizeof(a)); }
#define  ALMOST_EQUAL(a, b) (((double) ABS((a) - (b))) < ((double) 0.000000001))
#define ALMOST_ZERO(a) ALMOST_EQUAL(a, ((double) 0))
static char *strPOSSIBLE = "POSSIBLE";
static char *strIMPOSSIBLE = "IMPOSSIBLE";
#define MAX_R 500
#define MAX_B 500
typedef struct {
	int T;
} game_t;
typedef struct {
	int id;
	game_t *game;
	int R, B;
	int res;
} round_t;
void solveRound(round_t *round)
{
	int r = round->R;
	int b = round->B;
	int k = 1;
	int tmp;
	while (1) {
		if ((r+b) < k) {
			break;
		}
		for (int i = k / 2; i >= 0; i--) {
			if ((r >= i) && (b >= (k -i))) {
				round->res++;
				r -= i;
				b -= k-i;
			}
			if ((2 * i) == k) {
				continue;
			}
			tmp = r;
			r = b;
            b = tmp;
			if ((r >= i) && (b >= (k -i))) {
				round->res++;
				r -= i;
				b -= k-i;
			}
		}
		k++;
	}
}
void printRound(round_t *round)
{
	fprintf(stdout, "Case #%d: %d\n", round->id, round->res);
	fflush(stdout);
}
void playRound(round_t *round)
{
	solveRound(round);
	printRound(round);
}
void resetRound(round_t *round)
{
	game_t *game = round->game;
	memset(round, 0, sizeof(*round));
	round->game = game;
}
round_t *allocRound()
{
	round_t *round = malloc(sizeof(round_t));
	round->game = malloc(sizeof(game_t));
	resetRound(round);
	return round;
}
void fetchNextRound(round_t *round, int id)
{
	resetRound(round);
	round->id = id;
	scanf("%d%d", &round->R, &round->B);
}
int main()
{
	int T;
	scanf("%d", &T);
	round_t *round = allocRound();
	for (int i = 1; i <= T; i++) {
		fetchNextRound(round, i);
		playRound(round);
	}
}