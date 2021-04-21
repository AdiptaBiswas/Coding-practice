# include<stdio.h>
# include<stdlib.h>

typedef struct
{
    int marks[5];
    char name[30];
    int avg;
    int d_birth;
    int m_birth;
    int y_birth;
    int age;
    int standard;
} STUD;

STUD student_1;
void gen_info();
void marks_avg();
void dob();

void main()
{
    printf("Welcome to student portal..\n\n");
    gen_info();
        
}
    
void gen_info()
{
    char *ptr;
    ptr = student_1.name;
    printf(">> Enter student name: ");
    fgets(ptr, 30, stdin);
    printf("   $ Student name: %s", student_1.name);
    ptr = NULL;
    printf(">> Enter student marks: ");
    marks_avg();
    free(ptr);
    dob();
    printf(">> Enter student standard: ");
    scanf("%d", &student_1.standard);
    printf("   $ Student standard: Class-%d", student_1.standard);
}
    
void marks_avg()
{
    int *ptr;
    int sum = 0;
    int avg = 0;
    ptr = (int*) calloc(4, 5);
    ptr = student_1.marks;
    for (int i = 0; i < 5; i++)
    {   
        scanf("%d", ptr+i);
    }
    for (int i = 0; i < 5; i++)
    {
        sum += *(ptr+i);
    }
    student_1.avg = sum/5;
    printf("   $ Student average marks: %d\n", student_1.avg);
}

void dob()
{
    printf(">> Enter student D.O.B: ");
    scanf("%d/%d/%d", &student_1.d_birth, &student_1.m_birth, &student_1.y_birth);
    printf("   $ Student D.O.B entered: %d/%d/%d\n", student_1.d_birth, student_1.m_birth, student_1.y_birth);
    student_1.age = 2021 - student_1.y_birth;
    printf("   $ Student current age: %d\n", student_1.age);
}