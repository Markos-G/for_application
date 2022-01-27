#include "helpers.h"
#include <math.h>
#include <stddef.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int average_rgb = round((image[i][j].rgbtRed +
                                image[i][j].rgbtGreen +
                                image[i][j].rgbtBlue) / 3.0);
            image[i][j].rgbtRed = average_rgb;
            image[i][j].rgbtGreen = average_rgb;
            image[i][j].rgbtBlue = average_rgb;
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    int midpoint = round(width / 2.0);
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < midpoint; j++)
        {
            RGBTRIPLE temp_rgb =image[i][j];
            image[i][j] = image[i][(width - 1) - j];
            image[i][(width - 1) - j] = temp_rgb;
        }
    }
    return;
}

// Blur image

void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE temp[height][width];
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            temp[i][j] = image[i][j];
        }
    }

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            unsigned short sum_r = 0;
            unsigned short sum_b = 0;
            unsigned short sum_g = 0;
            float number_of = 0;
            for (int k = -1; k < 2; k++)
            {
                if (i + k < 0 || i + k > height - 1)
                {
                    continue;
                }
                for (int l = -1; l < 2; l++)
                {

                    if (j + l < 0 || j + l > width - 1)
                    {
                        continue;
                    }
                    sum_r += temp[i + k][j + l].rgbtRed;
                    sum_g += temp[i + k][j + l].rgbtGreen;
                    sum_b += temp[i + k][j + l].rgbtBlue;
                    number_of += 1;
                }
            }
            image[i][j].rgbtRed = round(sum_r / number_of);
            image[i][j].rgbtGreen = round(sum_g / number_of);
            image[i][j].rgbtBlue = round(sum_b / number_of);
        }
    }
    return;
}

// Detect edges
void edges(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE temp[height][width];
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            temp[i][j] = image[i][j];
        }
    }
    int Gx[3][3] = {{-1, 0, 1},
                    {-2, 0, 2},
                    {-1, 0, 1}};
    int Gy[3][3] = {{-1, -2, -1},
                    {0, 0, 0},
                    {1, 2, 1}};
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int sum_rx = 0;
            int sum_ry = 0;
            int sum_bx = 0;
            int sum_by = 0;
            int sum_gx = 0;
            int sum_gy = 0;
            for (int k = -1; k < 2; k++)
            {
                if (i + k < 0 || i + k > height - 1)
                {
                    continue;
                }
                for (int l = -1; l < 2; l++)
                {
                    if (j + l < 0 || j + l > width - 1)
                    {
                        continue;
                    }
                    sum_rx += temp[i + k][j + l].rgbtRed * Gx[k + 1][l + 1];
                    sum_ry += temp[i + k][j + l].rgbtRed * Gy[k + 1][l + 1];
                    sum_gx += temp[i + k][j + l].rgbtGreen * Gx[k + 1][l + 1];
                    sum_gy += temp[i + k][j + l].rgbtGreen * Gy[k + 1][l + 1];
                    sum_bx += temp[i + k][j + l].rgbtBlue * Gx[k + 1][l + 1];
                    sum_by += temp[i + k][j + l].rgbtBlue * Gy[k + 1][l + 1];
                }
            }
            int Gr = round(sqrt(sum_rx * sum_rx + sum_ry * sum_ry));
            int Gg = round(sqrt(sum_gx * sum_gx + sum_gy * sum_gy));
            int Gb = round(sqrt(sum_bx * sum_bx + sum_by * sum_by));
            if (Gr > 255)
            {
                Gr = 255;
            }
            if (Gg > 255)
            {
                Gg = 255;
            }
            if (Gb > 255)
            {
                Gb = 255;
            }
            image[i][j].rgbtRed = Gr;
            image[i][j].rgbtGreen = Gg;
            image[i][j].rgbtBlue = Gb;
        }
    }
    return;
}


