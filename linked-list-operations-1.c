#include<stdio.h>
#include<stdlib.h>

struct Node {
    int val;
    struct Node *next;
};

struct Node *head;

void insert(int);
void print();

int main()
{
    head = NULL;
    int inp;
    for (int i = 0; i < 10; i++)
    {
        printf("Enter: ");
        scanf("%d", &inp);
        insert(inp);
    }
    print();
}

void insert(int num)
{
    struct Node *temp = (struct Node*) malloc(sizeof(struct Node));
    int inp;
    temp -> val = num;
    temp -> next = head;
    head = temp;
}

void print()
{
    struct Node *temp = head;
    printf("The List is: ");
    while (temp -> next != NULL)
    {
        printf("%d, ", temp -> val);
        temp = temp -> next;
    }
    printf("\n");
}

/* Output:

Enter: 12                                                                                                                                       
Enter: 45                                                                                                                                       
Enter: 65                                                                                                                                       
Enter: 87                                                                                                                                       
Enter: 98                                                                                                                                       
Enter: 36                                                                                                                                       
Enter: 38                                                                                                                                       
7Enter: 9                                                                                                                                       
Enter: 72                                                                                                                                       
Enter: 18                                                                                                                                       
The List is: 18, 72, 79, 38, 36, 98, 87, 65, 45,                                                                                                
                                                                                                                                                
                                                                                                                                                
...Program finished with exit code 0 

*/
