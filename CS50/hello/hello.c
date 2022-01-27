#include <stdio.h>
#include <cs50.h>

int main(void)
{
    // reguest name
    string name = get_string("What's your name?");
    // print the output with the name from user
    printf("hello, %s\n", name);
}