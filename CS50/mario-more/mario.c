#include <stdio.h>
#include <cs50.h>

int main(void)
{
    //request user input for height in the range
    int height;
    do
    {
        height = get_int("Height: ");
    }
    while (height < 1 || height > 8);
    for (int i = 1; i <= height; i++)
    {
        for (int j = height - i ; j >= 1 ; j--)
        {
            printf(" ");
        }
        for (int j = 0 ; j < i ; j++)
        {
            printf("#");
        }
        printf("  ");
        for (int j = 0 ; j < i ; j++)
        {
            printf("#");
        }
        printf("\n");
    }
}

