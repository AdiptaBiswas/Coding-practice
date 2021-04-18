# include<stdio.h>

void edit(int *);

void main()
{
    char resp;
    int age = 25;
    int prev_age = age;
    printf("Do you want to change your age from %d?\n", age);
    printf("Press 'Y' to change and 'N' to ignore: ");
    scanf("%c", &resp);
    if (resp == 'Y')
        {
            edit(&age);
            printf("Your age has been changed from %d to %d.", prev_age, age);
        }
    else
        printf("You chose not to change your age.");
    
}

void edit(int *n_age)
{
    printf("Enter your new age: ");
    scanf("%d", n_age);
}
