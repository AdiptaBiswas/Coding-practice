# include<stdio.h>
# include<stdlib.h>

void array_sum();

void main()
{
   array_sum();
}

void max_num(int *p, int size)
{
    int max = 0;
    for (int i = 0; i < size; i++)
    {
        if (max < (*(p+i)))
            {
                max = *(p+i);
            }
    }
    (void)free(p);
    printf("> Maximum number in array: %d", max);
}

void array_sum()
{
   int *ptr;
   int size, num;
   int sum = 0;
   printf("> Enter array size: ");
   scanf("%d", &size);
   ptr = (int*) calloc(size, 4);
   
   for (int i = 0; i < size; i++)
    {
        printf("    > Enter number: ");
        scanf("%d", ptr+i);
        sum = sum + *(ptr+i);
    }
    printf("> Sum of array: %d\n", sum);
    max_num(ptr, size);
}