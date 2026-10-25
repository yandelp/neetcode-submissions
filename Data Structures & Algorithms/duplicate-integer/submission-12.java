class Solution {
    public boolean hasDuplicate(int[] nums) {
        Set<Integer> mySet = new HashSet<>();

        for(int i : nums) {
            mySet.add(i);
        }

        return mySet.size() != nums.length;
    }
}