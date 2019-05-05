#include<stdio.h>
#include<string.h>
void* initial_next(char *words,int length,int *next){
    int k=-1;
    int j=0;
    next[0]=-1;
    while(j<length){
        if(k==-1 || words[k] ==words[j])
            next[++j]=++k;
        else
            k=next[k];
    }
}
int kmp_compare(char* input_words,char* formal_words,int* next){
    int i_length =strlen(input_words);
    int m_length=strlen(formal_words);
    int distance = i_length-m_length;
    int stack[distance];
    int deep=0;
    int counter=0;
    for(int i=0;i<=distance;i++){
        int result;
        result=find_begin_index(i,i_length,input_words,formal_words,next);//返回-1就报错
        if(result!=-1){
            if(deep==0)
                stack[deep++]=result;
            else{
                if(stack[deep-1] == result)
                    break;
                else
                    stack[deep++]=result;

            }
        }
    }
    return deep;
}
int find_begin_index(int begin,int end,char* input_words,char* formal_words,int* next){
    int m=0;
    int tag=-1;
    for(int i=begin;i<end;i++){
        if(i==begin && input_words[i]!=formal_words[m])
            return -1;
        else{
            if(input_words[i]==formal_words[m]){
                if(m+1==strlen(formal_words)){
                    tag = i+1-strlen(formal_words);
                    printf("返回点为%d ",tag);
                    return tag;
                }
                m++;
            }
            else{
                while(next[m]!=-1){
                    m=next[m];
                    if(input_words[i]==formal_words[m]){
                        m++;
                        break;
                    }
                }
                m=0;
            }
        }
    }
    return -1;
}
void main(){
    int number;
    printf("输入一个数字:");
    scanf("%d",&number);
    for(int i=0;i<number;i++){
            char formal_words[20];
            printf("输入模型:");
            scanf("%s",formal_words);
            char input_words[128];

            scanf("%s",input_words);
            int length = strlen(formal_words);
            int next[length];
            initial_next(formal_words,length,next);

            int tmp=kmp_compare(input_words,formal_words,next);
            printf("%d\n",tmp);
    }
}
