#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

#define BLOCK_SIZE 512
typedef uint8_t BYTE;

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./recovery IMAGE\n");
        return 1;
    }
    FILE *filename = fopen(argv[1], "r");
    if (filename == NULL)
    {
        printf("file \"%s\" cannot open\n", argv[1]);
        return 1;
    }

    FILE *jpg;
    BYTE *buffer = malloc(BLOCK_SIZE * sizeof(BYTE));
    if (buffer == NULL)
    {
        return 1;
    }
    unsigned int i = 0;
    while (fread(buffer, sizeof(BYTE), BLOCK_SIZE, filename) == BLOCK_SIZE)
    {
        if (buffer[0] == 0xff && buffer[1] == 0xd8 &&
            buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
            if (i != 0)
            {
                fclose(jpg);
            }
            char image[8];
            sprintf(image, "%03i.jpg", i);
            jpg = fopen(image, "w");
            i += 1;
        }
        if (i != 0)
        {
            fwrite(buffer, BLOCK_SIZE, 1, jpg);
        }
    }
    free(buffer);
    fclose(jpg);
    fclose(filename);
    return 0;
}