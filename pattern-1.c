#include<stdio.h>

void pr_star(int);

void main()
{
  int star = 10;
  pr_star(star);
}

void pr_star(int star)
{
    printf("\t\t");
    for (int i=1; i<=star/2; i++)
    {
        for (int j=1; j<=i; j++)
        {
            printf("%d", j);
        }
        for (int k=i; k<=star-i; k++)
        {
            printf(" ");
        }
        for (int l=(star-i)+1; l<=star; l++)
        {
            printf("%d", l);
        }
        printf("\n");
        printf("\t\t");
    }
}

/* Output:
                1         10                                                                                                                                                   
                12       910                                                                                                                                                   
                123     8910                                                                                                                                                   
                1234   78910                                                                                                                                                   
                12345 678910        
*/
