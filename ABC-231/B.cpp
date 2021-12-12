#include <iostream>
#include <map>
#include <string>
using namespace std;

int main() {
  map<string, int> dict;
  int n;
  cin >> n;
  for (int i = 0; i < n; i++) {
    string name;
    cin >> name;
    dict[name]++;
  }

  string ans_name = "";
  int ans_cnt = -1;

  for (map<string, int>::iterator i = dict.begin(); i != dict.end(); i++) {
    string name = i->first;
    int cnt = i->second;
    if (cnt>ans_cnt){
      ans_name = name;
      ans_cnt = cnt;
    }
  }

  cout<<ans_name<<endl;

  return 0;
}
