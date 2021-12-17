#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

int main(){
    int n,i,j,count,max=0,k,lim; 
    int m; 
    scanf("%d %d",&n,&m);
    char* topic[n];
    for(i = 0; i < n; i++){
       topic[i] = (char *)malloc(1024 * sizeof(char));
       scanf("%s",topic[i]);
    }
   
    for(i = 0; i < n-1; i++){
       for(j=i+1;j<n;j++){
           count=0;
           for(k=0;k<m;k++){
               if(topic[i][k]=='1' || topic[j][k]=='1')
                   count++;
           }
          if(count>max){
              max=count;
              lim=1;
          }
          else if(count==max)
              lim++;
       }
    }
    printf("%d\n%d",max,lim);
    return 0;
}

