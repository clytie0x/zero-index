#include <stdio.h>

char keys[2000001];
char left[2000000];
char right[2000000];
int left_size = 0, right_size = 0;

int main()
{
    scanf("%2000000s", keys);
    for (int i = 0; keys[i] != '\0'; i++) {
        char c = keys[i];
        if (c == '<') {
            if (left_size > 0) {
                left_size--;
                right[right_size] = left[left_size];
                right_size++;
            }
        } else if (c == '>') {
            if (right_size > 0) {
                right_size--;
                left[left_size] = right[right_size];
                left_size++;
            }
        } else if (c == '#') {
            if (left_size > 0) {
                left_size--;
            }
        } else {
            left[left_size] = c;
            left_size++;
        }
    }
    if (left_size + right_size == 0) {
        printf("EMPTY\n");
        return 0;
    }
    for (int i = 0; i < left_size; i++) {
        putchar(left[i]);
    }
    for (int i = right_size - 1; i >= 0; i--) {
        putchar(right[i]);
    }
    printf("\n");
    return 0;
}
