class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # get counts of the different preferences in students list
        # while we iterate through sandwhiches we decrement the counts in dict
        # add up all the counts after the decrement and return 

        prefs_dict = {}
        for pref in students:
            if pref in prefs_dict:
                prefs_dict[pref] +=1
            else:
                prefs_dict[pref] = 1
                
        for sandwhich in sandwiches:
            if prefs_dict.get(sandwhich, 0) > 0:
                prefs_dict[sandwhich] -= 1
            else:
                break

        count = 0

        for pref in prefs_dict:
            count += prefs_dict[pref]

        return count
        