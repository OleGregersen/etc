#include <stdio.h>
#include <stdlib.h>

int main()
{
    int num, *arr1, *arr2, i;
    scanf("%d", &num);
    arr1 = (int*) malloc(num * sizeof(int));
    for(i = 0; i < num; i++) {
        scanf("%d", arr1 + i);
    }


    /* Write the logic to reverse the array. */
    arr2 = (int*) malloc(num * sizeof(int));
    for(i=1;i<=num;i++)
    {
        arr2[i-1] = arr1[num-i];
    }

    for(i = 0; i < num; i++)
        printf("%d ", *(arr2 + i));
    return 0;
}
