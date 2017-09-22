map<string, int> teams;
vector<pair<int, string> > all_teams;

int main() {
    // teams.txt is the html format file in icpc dhaka site
    // all universities.txt will contains all univs with number of teams
    freopen("teams.txt", "r", stdin);
    freopen("all_universities.txt", "w", stdout);
    
    // class="gridCols">Khulna University Of Engineering and Technology
    
    string line;
    string search_str = "gridCols";
    while(getline(cin, line)) {
        int found = line.find(search_str);
        if (found!=std::string::npos) {
            string name_of_univ = line.substr(found + search_str.size() + 2);
            teams[name_of_univ] ++ ;
        }
    }
    map<string, int>::iterator it;
    for(it = teams.begin(); it != teams.end(); it++) {
        all_teams.push_back(make_pair(it->second, it->first));
    }
    sort(all_teams.rbegin(), all_teams.rend());
    
    int total_teams = 0;
    for(int i = 0; i < all_teams.size(); i++) {
        cout << std::right << std::setw(70);
        cout << all_teams[i].second << " " << all_teams[i].first << endl;
        total_teams += all_teams[i].first;
    }
    
    cout << "\n\n\n\n\n";
    cout << "Total Universities : " << all_teams.size() << endl;
    cout << "Total Teams : " << total_teams << endl;
}
