#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

int main(){
    char* s = (char *)malloc(512000 * sizeof(char));
    scanf("%s",s);
    char* t = (char *)malloc(512000 * sizeof(char));
    scanf("%s",t);
    int k,i=0,change=0; 
    scanf("%d",&k);
    int l1,l2;
    l1=strlen(s);
    l2=strlen(t);
    if(l1+l2<=k)
        printf("Yes\n");
    else{
        while(i<l1 && *(s+i)==*(t+i)){
            i++;
        }
        if(i==l1 || i==l2)
            i--;
        change=l1-i+l2-i;
       
        if(change<=k && (k-change)%2==0)
            printf("Yes\n");
        else
            printf("No\n");
    }
    return 0;
}

