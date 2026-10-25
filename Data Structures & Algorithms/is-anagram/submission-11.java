class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length() != t.length()) return false;

        HashMap<Character, Integer> mapS = new HashMap<>();
        HashMap<Character, Integer> mapT = new HashMap<>();

        for(int i = 0; i < s.length(); i++) {
            mapS.put(s.charAt(i), 1 + mapS.getOrDefault(s.charAt(i), 0));
            mapT.put(t.charAt(i), 1 + mapT.getOrDefault(t.charAt(i), 0));
        }

        for(char key : mapS.keySet()) {
            if(!mapS.get(key).equals(mapT.get(key))) {
                return false;
            }
        }
        return true;
    }
}
