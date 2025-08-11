#include <stdio.h>
#include <stdlib.h>
#include <conio.h>
#include <time.h>

int duzlem[4][4]={{0,0,0,0},{0,0,0,0},{0,0,0,0},{0,0,0,0}};
int randomsayi = 2, puan = 0, sifirsayar=0 ;
int main(){
    randomsayiver();
    randomsayiver();
    matris();
    while(1){
        char yonlendirme;

        yonlendirme=getch();
        if(yonlendirme=='W' || yonlendirme=='w'){
            rotate(1);
            islem();
            randomsayiver();
            randomsayiver();
            rotate(3);
            matris();
        }
        else if(yonlendirme=='A' || yonlendirme=='a'){
            islem();
            randomsayiver();
            randomsayiver();
            matris();
        }
        else if(yonlendirme=='S' || yonlendirme=='s'){
            rotate(3);
            islem();
            randomsayiver();
            randomsayiver();
            rotate(1);
            matris();
        }
        else if(yonlendirme=='D' || yonlendirme=='d'){
            rotate(2);
            islem();
            randomsayiver();
            randomsayiver();
            rotate(2);
            matris();
        }
        else if(yonlendirme=='E' || yonlendirme=='e'){
            gameover();
            return 0;
        }
    }
    return 0;
}
void randomsayiver(){
    int i,j,k,l;
    srand(time(NULL));
    sifirsay();
    if(sifirsayar!=0){
        while(1){
            i=rand()%4;
            j=rand()%4;
            if(duzlem[i][j]==0){
                duzlem[i][j]=2;
                break;
                }
        }
    }
}
void sifirsay(){
    int i,j;
    sifirsayar=0;
    for(i=0;i<4;i++){
        for(j=0;j<4;j++){
            if(duzlem[i][j]==0){
                sifirsayar++;
            }
        }
    }
}
void matris(){
    int i,j,k,l;
    system("cls");
    printf("              2048 game              \n");
    printf(" yukari asagi sag ve sol yonlendirme icin sirasiyla w,a,s,d tuslarini kullanin.\n\n");
    for(i=0;i<4;i++){
        for(j=0;j<4;j++){
            printf("   %d  ",duzlem[i][j]);
        }
        printf("\n\n");
    }
    printf("puanin : %d\n",puan);
}
void islem(){
    int i,j,k,l,islemsayisi=0;
    for (i=0;i<4;i++){
        for(l=0;l<4;l++){
            for(j=3;0<j;j--){
                if(duzlem[i][j-1]==0){
                    duzlem[i][j-1]=duzlem[i][j];
                    duzlem[i][j]=0;
                    islemsayisi+=1;
                }
            }
        }

        for(k=1;k<4;k++){
            if(duzlem[i][k]==duzlem[i][k-1])
            {
                duzlem[i][k-1]=duzlem[i][k]*2;
                duzlem[i][k]=0;
                islemsayisi+=1;
                puan+=duzlem[i][k-1];
            }
        }
        for(l=0;l<4;l++){
            for(j=3;0<j;j--){
                if(duzlem[i][j-1]==0){
                    duzlem[i][j-1]=duzlem[i][j];
                    duzlem[i][j]=0;
                    islemsayisi+=1;
                }
            }
        }
    }
    if(islemsayisi==0){

        gameover();
    }
}


void gameover(){

    system("cls");
    printf("          OYUN BITTI \n");
    printf( "         PUANIN :%d",puan);
    getch();
    return 0;
}

void rotate(turnum){

    int i,temp=0;
    for(i=0;i<turnum;i++){
        //1
        temp=duzlem[0][0];
        duzlem[0][0]=duzlem[0][3];
        duzlem[0][3]=duzlem[3][3];
        duzlem[3][3]=duzlem[3][0];
        duzlem[3][0]=temp;
        temp=0;
        //2
        temp=duzlem[0][1];
        duzlem[0][1]=duzlem[1][3];
        duzlem[1][3]=duzlem[3][2];
        duzlem[3][2]=duzlem[2][0];
        duzlem[2][0]=temp;
        temp=0;
        //3
        temp=duzlem[0][2];
        duzlem[0][2]=duzlem[2][3];
        duzlem[2][3]=duzlem[3][1];
        duzlem[3][1]=duzlem[1][0];
        duzlem[1][0]=temp;
        //4
        temp=duzlem[1][1];
        duzlem[1][1]=duzlem[1][2];
        duzlem[1][2]=duzlem[2][2];
        duzlem[2][2]=duzlem[2][1];
        duzlem[2][1]=temp;
        temp=0;
    }
}






