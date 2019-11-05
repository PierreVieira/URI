"""
Autor: Pierre Vieira
Data da submissão: 13/09/2018 22:20:57
"""
#include <stdio.h>
#include <math.h>
int main()
{
    float x1, x2, y1, y2, dist;
    scanf("%f %f",&x1, &y1);
    scanf("%f %f",&x2, &y2);
    dist = sqrt(pow(x2 - x1,2)+pow(y2 - y1,2));
    printf("%.4f\n",dist);
}
