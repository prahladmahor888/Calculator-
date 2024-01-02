#include <stdio.h>
#include <math.h>
void main()
{
    int p,n;
    float r,a,ci;

    printf("Enter the Principal Amount = ");
    scanf("%d",&p);
    printf("Enter the Time = ");
    scanf("%d",&n);
    printf("Enter Rate = ");
    scanf("%f",&r);
    a = p*pow(((100+r)/100),n);
    ci = a - p;
    printf("total value = %f",ci);
    
}