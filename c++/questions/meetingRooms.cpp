#include <vector>
using namespace std;

class Interval{
    public:
        int start, end;
        Interval (int start, int end){
            this->start = start;
            this->end = end;
        }
};
/**
 * @brief Comp class for intervals based on starts
 * 
 */
class intervalCompOnStartsFunctor {
public:
    bool operator()(const Interval& a, const Interval& b) const {
        return a.start < b.start;
    }
   // bool operator < ()
};

class Solution {
public:
    /**
     * @brief Determiens if there are any time conflicts in the schedule
     * 
     * @param intervals vector of intervals
     * @return bool
     */
    bool canAttendMeetings(vector<Interval>& intervals) {
        if (intervals.size() == 0) return true;
        auto intervalCompOnStarts = [](const Interval& a, const Interval& b){return a.start < b.start;};
        // sort(intervals.begin(), intervals.end(), intervalCompOnStarts);
        sort(intervals.begin(), intervals.end(), intervalCompOnStartsFunctor());

        for (int i = 0; i < intervals.size() - 1; i++){
            if (intervals[i+1].start < intervals[i].end) return false;
        }
        return true;
    }

};
