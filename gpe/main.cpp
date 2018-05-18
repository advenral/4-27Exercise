#include <iostream>
#include <vector>
#include <algorithm>

#include <sstream>
#include <stdlib.h>
using namespace std;

int main(void){
	int ca;
	cin>> ca;
	while(ca--){
		int num, ans=0;
		cin>> num;
		string input;
		for(int i=0; i<num; i++){
			cin>> input;
			if(input=="LEFT"){
				ans--;
			}
			else if(input=="RIGHT"){
				ans++;
			}
			else{//http://shipuahamed.com/2012/12/uva-12503-robot-instructions.html
			 
				//stringstream k;
				//k<< input.end();
				//find i
			}
		}
		cout<< ans<< endl;
	}
	
	return 0;
}
//catlog i=i*2*2i-1/i+1
/*
	//判斷數字是否回文，非回文就加自己反向的數字，直到成回文 
	int num;
	string word;
	cin>> num;
	while(num--){
		cin>> word;
		string origin= word;
		reverse(word.begin(), word.end());
		
		int sum=0, cou=0;
		while(word!=origin && cou<1000){
			stringstream tmp;
			
			//轉成數字相加 
			sum= atoi(word.c_str()) + atoi(origin.c_str());
			
			//轉成字串 
			tmp<< sum;
			word= tmp.str();
			
			//紀錄新字串 
			origin= word;
			reverse(word.begin(), word.end());
			cou++;
		}
		cout<< cou<< " "<< word<< endl;
	}
*/

/*	string str1, str2;
	vector<char> vec;
	while(cin>> str1>> str2){
		for(unsigned i=0; i<str1.size(); i++){
			for(unsigned j=0; j<str2.size(); j++){
				if(str1[i]==str2[j]){
					if(find(vec.begin(), vec.end(), str1[i]) == vec.end() )
						vec.push_back(str1[i]);
				}
			}
		}
		sort(vec.begin(), vec.end());
		for(unsigned i=0; i<vec.size(); i++){
			cout<< vec[i];
		}
		cout<< endl;
	}
*/

/*
    int num;
    while(cin>> num &&num){
	    int a=(num==1)? 0:num;
	    int odd=2;
	    while(num!=1){
	    	if(num%odd == 0){
	    		while(num%odd == 0){
	    			num/= odd;
				}
				a= a*(odd-1)/(odd);
			}
			odd++;
		}
	    cout<< a<< endl;
	}
*/

/*
    int cas, max, rep;
    cin>> cas;
    while(cas--){
        cin>> max>> rep;
        for(int i=0; i<rep; i++){
            for(int j=1; j<=max; j++){
                for(int k=0; k<j; k++){
                    cout<< j; 
                }
   		 	 	cout<< endl;
        	}
			for(int k=max-1; k>0; k--){
                for(int n=1; n<=k; n++)
                    cout<< k;
                cout<< endl;
            }
            cout<< endl;
        }
    }
*/
