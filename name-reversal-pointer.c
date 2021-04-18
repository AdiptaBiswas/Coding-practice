# include<stdio.h>

char* swap(char *);

void main()
{
    char f_name[20];
    char *ptr;
    printf("> Enter a name: ");
    ptr = &f_name[0];
    scanf("%s", ptr);
    printf("> Entered name is: %s\n", ptr);
    printf("> Entered name in reversed order is: %s", swap(ptr));
}

char* swap(char *ptr)
{
    int length;
    char temp;
    for (int i = 0; *(ptr + i) != '\0'; i++)
        {
            length = i;
        }
    length += 1;
    for (int i = 0; i < length/2; i++)
        {
            temp = *(ptr+i);
            *(ptr+i) = *(ptr+length-1-i);
            *(ptr+length-1-i) = temp;
        }  
    return ptr;
}

/* Output:

> Enter a name: Adipta                                                                                                                        
> Entered name is: Adipta                                                                                                                     
> Entered name in reversed order is: atpidA

*/