#include <vector>
#include <string>
#include <fstream>
#include <iostream>
std::ofstream emergencyOuput("EmergencyStatus.txt");
std::string emergencyCode;

void eraseOutput()
{
    emergencyOuput<<"";
}

signed main()
{
    std::cin>>emergencyCode;
    emergencyOuput<<emergencyCode;
    if(emergencyCode=="clear")
    {
        eraseOutput();
    }
}