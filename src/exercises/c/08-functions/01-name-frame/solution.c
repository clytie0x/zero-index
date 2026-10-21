#include <stdio.h>
#include <string.h>

char name[55];

void print_repeat(char symbol, int count)
{
    for (int i = 0; i < count; i++) {
        printf("%c", symbol);
    }
}

void print_border(int width)
{
    print_repeat('#', width);
    printf("\n");
}

void print_blank(int width)
{
    printf("#");
    print_repeat(' ', width - 2);
    printf("#\n");
}

int main()
{
    int padding;
    scanf("%s %d", name, &padding);
    int width = strlen(name) + 2 * padding + 2;
    print_border(width);
    for (int i = 0; i < padding; i++) {
        print_blank(width);
    }
    printf("#");
    print_repeat(' ', padding);
    printf("%s", name);
    print_repeat(' ', padding);
    printf("#\n");
    for (int i = 0; i < padding; i++) {
        print_blank(width);
    }
    print_border(width);
    return 0;
}
