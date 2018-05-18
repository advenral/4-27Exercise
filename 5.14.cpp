#include <stdio.h>

int main(void){
    int cas, max, rep;
    cin>> cas;
    while(cas--){
        cin>> max>> rep;
        int tmp=0;
        for(int i=0; i<rep; i++){
            for(int j=1; j<=max; j++){
                for(int k=0; k<j; k++){
                    cout<< j; 
                    tmp++;
                }
                cout<< endl;
                if(tmp== max){
                    for(int k=tmp-1; k>0; k--){
                        for(int n=1; n<=k; n++)
                           cout<< k;
                        cout<< endl;
                    }
                }
            }
            cout<< endl;
        }
    }
    return 0;
}