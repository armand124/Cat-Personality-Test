#include <bits/stdc++.h>

class PeopleDeclaration
{
   public:
    std::vector<std::string> AllNames;
    void PushingNames(&std::vector<std::string> V)
    {
        V.push_back("Bingus");
        V.push_back("Boingus");
        V.push_back("Spoingus");
        V.push_back("Merlin");
        V.push_back("Floppa");
    }
};

class PeopleFunctions
{   
   public:
    std::map<std::string , double > Names;
    void iterateFirst(std::map<std::string, double> Names)
    {
        PeopleDeclaration::PushingNames(PeopleDeclaration::AllNames);
        
        for(int i=0 ; i<PeopleDeclaration::AllNames.end();i++)
         {
                Names[PeopleDeclaration::AllNames[i]] = 0;
         }
    }

};