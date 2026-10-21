#include <stdio.h>

typedef struct {
    char name[21];
    int score;
} Student;

Student students[1000];

int main()
{
    int n;
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%s %d", students[i].name, &students[i].score);
    }
    int best = 0;
    for (int i = 1; i < n; i++) {
        if (students[i].score > students[best].score) {
            best = i;
        }
    }
    int count = 0;
    for (int i = 0; i < n; i++) {
        if (students[i].score == students[best].score) {
            count++;
        }
    }
    printf("%s %d\n", students[best].name, students[best].score);
    printf("%d\n", count);
    return 0;
}
