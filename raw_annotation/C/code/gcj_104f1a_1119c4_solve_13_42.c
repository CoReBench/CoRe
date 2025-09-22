#include "stdio.h"
#include "stdlib.h"
#include "ctype.h"
#include "string.h"
void solve();
int getInt();
float getFloat();
char* getWord();
int main(int argc, char** argv) {
    solve();
    return 0;
}
void solve() {
    const int numCases = getInt();
    const int maxNights = getInt();
    const int maxGophers = getInt();
    for(int c = 1; c <= numCases; c++) {
        int answer = 1;
        for(int night = 1; night <= maxNights; night++) {
            const int numBlades = night + 1;
            if(numBlades > 18) {
                break;
            }
            for(int hole = 0; hole < 18; hole++) {
                printf("%i ", numBlades);
            }
            printf("\n");
            int sum = 0;
            for(int hole = 0; hole < 18; hole++) {
                sum += getInt();
            }
            if((sum % numBlades) == 0) {
                answer *= numBlades;
            }
        }
        printf("%i\n", answer);
        const int correct = getInt();
        if(correct == -1) {
            return;
        }
    }
}
int getInt() {
    int result;
    scanf("%i", &result);
    return result;
}
float getFloat() {
    float result;
    scanf("%f", &result);
    return result;
}
char* getWord() {
    int size = 1;
    char* word = malloc(size * sizeof(char));
    char c;
    int i = 0;
    while(isspace(c = getchar()));
    ungetc(c, stdin);
    while(!isspace(c = getchar())) {
        if(i + 1 >= size) {
            size *= 2;
            word = realloc(word, size * sizeof(char));
        }
        word[i] = c;
        i++;
    }
    word[i] = '\0';
    return word;
}