#include "Types.h"
#include <fstream>

class GetStart
{
   public:
    bool isOver()
    {
        bool start;
        std::ifstream input("start_session.txt");
        input>>start;
        return !start;
    }
};
void CalculateProcents(&std::string Id, &double Pro)
{

}
signed main()
{
    GetStart session;

    if(!session.isOver)
    {
        PeopleFunctions::iterateFirst(PeopleFunctions::Names);

    }
    while(!session.isOver)
    {
        
    }
}