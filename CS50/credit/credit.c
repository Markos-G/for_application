#include <stdio.h>
#include <cs50.h>
#include <math.h>

int main(void)
{
    // chack valitity with Lung's Algo
    long card = get_long("Number: ");
    long buffer = card;
    int sum = 0;
    int sum2 = 0;
    int digits;
    bool skip = true;
    while (buffer)
    {
        int b = buffer % 10;
        if (skip)
        {
            sum2 = sum2 + b;
            skip = false;
        }
        else
        {
            b = b * 2;
            if (b >= 10)
            {
                sum = sum + b / 10 + b % 10;
            }
            else
            {
                sum = sum + b;
            }
            skip = true;
        }
        digits = digits + 1;
        buffer = buffer / 10;

    }

    int total;
    total = sum + sum2;

    // print type of card
    if (total % 10 == 0)
    {
        long power = pow(10, digits - 1);
        long power2 = pow(10, digits - 2);
        int first = card / power;
        int second = card / power2 % 10;

        if (first == 4 && digits >= 13 && digits <= 16)
        {
            printf("VISA\n");
        }
        else if (first == 3 &&
                 (second == 4 || second == 7) &&
                 digits == 15)
        {
            printf("AMEX\n");
        }
        else if (first == 5 &&
                 (second == 1 ||
                  second == 2 ||
                  second == 3 ||
                  second == 4 ||
                  second == 5) &&
                 digits == 16)
        {
            printf("MASTERCARD\n");
        }
        else
        {
            printf("INVALID\n");
        }
    }
    else
    {
        printf("INVALID\n");
    }

}
