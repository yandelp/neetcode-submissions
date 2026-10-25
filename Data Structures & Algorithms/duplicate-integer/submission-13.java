class Solution {
    public boolean hasDuplicate(int[] nums) {
        Set<Integer> mySet = new HashSet<>();

        for(int i : nums) {
            if(!mySet.add(i)) {
                return true;
            }
        }

        return false;
    }
}