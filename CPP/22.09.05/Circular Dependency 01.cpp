/* Circular references 예제 
   참고 : http://sweeper.egloos.com/2826435 
   A와 B가 서로의 shared_ptr을 가지고 있으면 레퍼런스 카운터가 0이 되지 않아 메모리가 해제되지 않는다.
   이를 가리켜 Circular dependency(순환 참조)라고 한다. */

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
        /* 함수 밖으로 나가면 소멸, 하지만 party 객체가 user를 참조하고 있으므로 소멸되지 않는다. */
        UserPtr user(new User);

        /* 순환 참조 발생 */
        party->AddMember(user);
        user->SetParty(party);
    }

    /* reset 함수를 통해 해제를 시도해도 순환 참조로 서로를 가리키고 있어 소멸할 수 없다. */
    party.reset();

    return 0;
}