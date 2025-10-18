class Solution {
    public List<String> removeAnagrams(String[] words) {
        List<String> result = new ArrayList<>();
        for(String word : words){
            if(result.isEmpty() ||  !isAnagram(word , result.get(result.size()-1))){
                result.add(word);
            }
        }
        return result;
    }

    private boolean isAnagram(String s1 , String s2){
        char[] arr1 = s1.toCharArray();
        char[] arr2 = s2.toCharArray();
        Arrays.sort(arr1);
        Arrays.sort(arr2);
        return Arrays.equals(arr1 , arr2);
    }
}