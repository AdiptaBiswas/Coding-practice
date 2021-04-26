# include<stdio.h>

void insert(int *);

void main()
{
    int arr[10];
    int *ptr;
    ptr = &arr[0];
    printf("Value insertion in Array\n\n");
    for (int i = 0; i < 10; i++)
    {
        printf("> Enter: ");
        scanf("%d", ptr+i);
    }
    printf("\n");
    printf("> Values entered: ");
    for (int i = 0; i < 10; i++)
    {
        if (i != 9)
            printf("%d , ", *(ptr+i));
        else
            printf("%d", *(ptr+i));
    }
    insert(ptr);
}

void insert(int *arr)
{
    int position;
    int *ptr;
    int numb;
    ptr = &arr[0];
    printf("\n\n");
    printf("> To insert value, enter position: ");
    scanf("%d", &position);
    printf("\n");
    printf("Enter value to insert: ");
    scanf("%d", &numb);
    printf("\n");
    for (int i = 9; i >= position-1; i--)
    {
        arr[i+1] = arr[i];
    }
    arr[position-1] = numb;
    for (int i = 0; i < 11; i++)
    {
        if (i != 10)
            printf("%d , ", arr[i]);
        else
            printf("%d", arr[i]);
    }
    printf("\n");
}

