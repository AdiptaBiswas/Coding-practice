#include<stdio.h>

void main()
{
    int num, rem, i, temp = 0;
    int cub_num = 0;
    int quo;
    printf("Enter a number: ");
    scanf("%d", &num);
    printf("\n");
    temp = num;
    
    while (temp>=10)
    {
        rem = temp % 10;
        printf("Remainder value: %d\n", rem);
        quo = temp / 10;
        printf("Quotient value: %d\n", quo);
        cub_num += rem*rem*rem*rem;
        printf("%d^4 value: %d\n", rem, cub_num);
        temp = quo;
    }
    
    cub_num += temp*temp*temp*temp;
    printf("%d^4 value: %d\n\n", temp, cub_num);
    
    if (cub_num == num)
        printf("%d == %d, %d is a Narcissistic number", num, cub_num, num);
    
    else
        printf("%d != %d, %d is not a Narcissistic number", num, cub_num, num);
}

/* Output:

Enter a number: 9474                                                                                                                                                           
                                                                                                                                                                               
Remainder value: 4                                                                                                                                                             
Quotient value: 947                                                                                                                                                            
4^4 value: 256                                                                                                                                                                 
Remainder value: 7                                                                                                                                                             
Quotient value: 94                                                                                                                                                             
7^4 value: 2657                                                                                                                                                                
Remainder value: 4                                                                                                                                                             
Quotient value: 9                                                                                                                                                              
4^4 value: 2913                                                                                                                                                                
9^4 value: 9474                                                                                                                                                                
                                                                                                                                                                               
9474 == 9474, 9474 is a Narcissistic number

*/
