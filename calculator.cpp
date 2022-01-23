#include "Questions.h"
#include <fstream>
#include<string>
std::fstream input("session.txt");
std::ofstream output("outputCharacter.txt");
std::fstream standings("standing.txt");
std::ofstream stand("standing.txt");
std::string id; int score;
std::string goodId ;
int myScore;
std::map<std::string , int > scoreForEach;
void del()
{
    output<<"";
}
signed main()
{
   input>>id>>score;
   del();
   int goodScore= 0;
   if(score==0)
    goodScore = 0;
    if(score==1)
        goodScore = 20;
    if(score==2)
        goodScore = 40;
    if(score==3)
        goodScore = 60;
    if(score==4)
        goodScore = 80;
    if(score==5)
        goodScore = 100;

    while(standings>>goodId>>myScore)
    {
        scoreForEach[goodId] = myScore;
    }
    scoreForEach[id] +=score;
    for(auto itr = scoreForEach.begin() ; itr!=scoreForEach.end(); itr++)
    {
        stand<<itr->first<<' '<<itr->second;
        output<<itr->first<<' '<<itr->second;
    }
}