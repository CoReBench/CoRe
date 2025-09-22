#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
double run_horses(int destination, int total_horses, int *position, int *speed){
    int horses_running = total_horses;
    int *finished = (int*)malloc(total_horses * sizeof(int));
    memset(finished, 0, total_horses * sizeof(int));
    int hours_passed = 0;
    while(horses_running > 0)
    {
        hours_passed++;
        for(int i = 0; i < total_horses; i++)
        {
            if(finished[i] != 1)
            {
                position[i] += speed[i];
                if(i - 1 >= 0 && position[i] > position[i - 1])
                {
                    position[i] = position[i - 1];
                    speed[i] = speed[i - 1];
                }
                if (position[i] >= destination)
                {
                    finished[i] = 1;
                    horses_running--;
                }
            }
        }
    }
    free(finished);
    return (double)destination / (double)hours_passed;
}
int main() {
    int T = 0;
    scanf("%d", &T);
    for(int i = 0; i < T; i++)
    {
        int destination = 0;
        int total_horses = 0;
        scanf("%d %d", &destination, &total_horses);
        int *position = (int*)malloc(total_horses * sizeof(int));
        int *speed = (int*)malloc(total_horses * sizeof(int));
        memset(position, 0, total_horses* sizeof(int));
        memset(speed, 0, total_horses* sizeof(int));
        for(int j = 0; j < total_horses; j++)
        {
            scanf("%d %d", &(position[total_horses - j - 1]), &(speed[total_horses - j - 1]));
        }
        double cruise_speed = run_horses(destination, total_horses, position, speed);
        printf("Case #%d: %f\n", i + 1, cruise_speed);
        free(position);
        free(speed);
    }
    return 0;
}