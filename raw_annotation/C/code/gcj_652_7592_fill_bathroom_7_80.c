#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#define MIN(a,b) (((a)<(b))?(a):(b))
#define MAX(a,b) (((a)>(b))?(a):(b))
void fill_bathroom(int n_case, int stalls, int users){
    int *stalls_occupancy = (int*)malloc(stalls * sizeof(int));
    memset(stalls_occupancy, 0, stalls * sizeof(int));
    int *ls = (int*)malloc(stalls * sizeof(int));
    int *rs = (int*)malloc(stalls * sizeof(int));
    int max_crit1 = 0;
    int max_crit2 = 0;
    for(int i = 0; i < stalls; i++)
    {
        ls[i] = i;
        rs[i] = stalls - i - 1;
    }
    for(int i = 0; i < users; i++)
    {
        int pos = 0;
        max_crit1 = 0;
        max_crit2 = 0;
        for(int j = 0; j < stalls; j++)
        {
            if(stalls_occupancy[j] == 0)
            {
                int crit1 = MIN(ls[j], rs[j]);
                int crit2 = MAX(ls[j], rs[j]);
                if(crit1 >= max_crit1 && crit2 > max_crit2)
                {
                    pos = j;
                    max_crit1 = crit1;
                    max_crit2 = crit2;
                }
                else if (crit1 > max_crit1)
                {
                    pos = j;
                    max_crit1 = crit1;
                    max_crit2 = crit2;
                }
            }
        }
        stalls_occupancy[pos] = 1;
        int reset_counter = 0;
        for(int i = pos + 1; i < stalls; i++)
        {
            if(stalls_occupancy[i] == 0)
            {
                ls[i] = reset_counter;
                reset_counter++;
            }
            else
            {
                ls[i] = reset_counter;
                reset_counter++;
                break;
            }
        }
        reset_counter = 0;
        for(int i = pos - 1; i >= 0; i--)
        {
            if(stalls_occupancy[i] == 0)
            {
                rs[i] = reset_counter;
                reset_counter++;
            }
            else
            {
                rs[i] = reset_counter;
                reset_counter++;
                break;
            }
        }
    }
    free(stalls_occupancy);
    free(ls);
    free(rs);
    printf("Case #%d: %d %d\n", n_case + 1, max_crit2, max_crit1);
}
int main() {
    int T = 0;
    scanf("%d", &T);
    for(int i = 0; i < T; i++)
    {
        int stalls = 0, users = 0;
        scanf("%d %d", &stalls, &users);
        fill_bathroom(i, stalls, users);
    }
    return 0;
}