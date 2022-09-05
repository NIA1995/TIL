// ConsoleApplication2.cpp : 이 파일에는 'main' 함수가 포함됩니다. 거기서 프로그램 실행이 시작되고 종료됩니다.
//

#include <iostream>
#include <chrono>
#include <vector>
#include <numeric>
#include <execution>
#include <string>
#include <algorithm>
#include <map>
#include <sstream>
#include <memory>

using namespace std;

class User;
typedef shared_ptr<User> UserPtr;

class Party
{
public:
    Party()  {}
    ~Party() { m_MemberList.clear(); }

public:
    void AddMember(const UserPtr& UserPtr)
    {
        m_MemberList.push_back(UserPtr);
    }

private:
    typedef vector<UserPtr> MemberList;
    MemberList m_MemberList;
};
typedef shared_ptr<Party> PartyPtr;

class User
{
public:
    void SetParty(const PartyPtr& partyPtr)
    {
        m_Party = partyPtr;
    }

private:
    PartyPtr m_Party;
};

int main()
{
    PartyPtr party(new Party);

    for (int i = 0; i < 5; ++i)
    {
        UserPtr user(new User);

        party->AddMember(user);

        user->SetParty(party);
    }

    party.reset();

    return 0;
}