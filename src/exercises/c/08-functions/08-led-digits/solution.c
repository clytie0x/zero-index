#include <stdio.h>

char segments[10][8] = {"abcdef", "bc", "abdeg", "abcdg", "bcfg",
                        "acdfg", "acdefg", "abc", "abcdefg", "abcdfg"};
char digits[25];
int size;

int is_on(int digit, char segment)
{
    for (int i = 0; segments[digit][i] != '\0'; i++) {
        if (segments[digit][i] == segment) {
            return 1;
        }
    }
    return 0;
}

void print_repeat(char symbol, int count)
{
    for (int i = 0; i < count; i++) {
        printf("%c", symbol);
    }
}

void print_horizontal(char segment)
{
    for (int i = 0; digits[i] != '\0'; i++) {
        if (i > 0) {
            printf(".");
        }
        printf(".");
        print_repeat(is_on(digits[i] - '0', segment) ? '#' : '.', size);
        printf(".");
    }
    printf("\n");
}

void print_vertical(char left, char right)
{
    for (int i = 0; digits[i] != '\0'; i++) {
        int digit = digits[i] - '0';
        if (i > 0) {
            printf(".");
        }
        printf("%c", is_on(digit, left) ? '#' : '.');
        print_repeat('.', size);
        printf("%c", is_on(digit, right) ? '#' : '.');
    }
    printf("\n");
}

int main()
{
    scanf("%d %s", &size, digits);
    print_horizontal('a');
    for (int r = 0; r < size; r++) {
        print_vertical('f', 'b');
    }
    print_horizontal('g');
    for (int r = 0; r < size; r++) {
        print_vertical('e', 'c');
    }
    print_horizontal('d');
    return 0;
}
