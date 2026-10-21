#include <stdio.h>
#include <string.h>

typedef struct {
    char name[16];
    int points;
    int scored;
    int conceded;
} Team;

Team teams[20];
int used[20];

int find_team(const char name[], int t)
{
    for (int i = 0; i < t; i++) {
        if (strcmp(teams[i].name, name) == 0) {
            return i;
        }
    }
    return -1;
}

void record(Team *team, int scored, int conceded)
{
    team->scored += scored;
    team->conceded += conceded;
    if (scored > conceded) {
        team->points += 3;
    } else if (scored == conceded) {
        team->points += 1;
    }
}

int better(const Team *a, const Team *b)
{
    if (a->points != b->points) {
        return a->points > b->points;
    }
    int diff_a = a->scored - a->conceded;
    int diff_b = b->scored - b->conceded;
    if (diff_a != diff_b) {
        return diff_a > diff_b;
    }
    if (a->scored != b->scored) {
        return a->scored > b->scored;
    }
    return strcmp(a->name, b->name) < 0;
}

int main()
{
    int t, m;
    scanf("%d %d", &t, &m);
    for (int i = 0; i < t; i++) {
        scanf("%s", teams[i].name);
    }
    for (int k = 0; k < m; k++) {
        char home[16], away[16];
        int home_goals, away_goals;
        scanf("%s %s %d %d", home, away, &home_goals, &away_goals);
        record(&teams[find_team(home, t)], home_goals, away_goals);
        record(&teams[find_team(away, t)], away_goals, home_goals);
    }
    for (int rank = 0; rank < 3; rank++) {
        int best = -1;
        for (int i = 0; i < t; i++) {
            if (!used[i] && (best == -1 || better(&teams[i], &teams[best]))) {
                best = i;
            }
        }
        used[best] = 1;
        printf("%s %d %d %d\n", teams[best].name, teams[best].points,
               teams[best].scored - teams[best].conceded, teams[best].scored);
    }
    return 0;
}
