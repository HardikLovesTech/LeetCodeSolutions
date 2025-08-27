class Solution {
    public int areaOfMaxDiagonal(int[][] dimensions) {
        int maxDiagSq = -1;
        int maxArea = 0;

        for (int[] dim : dimensions) {
            int length = dim[0];
            int width = dim[1];

            int diagSq = length * length + width * width;
            int area = length * width;

            if (diagSq > maxDiagSq) {
                maxDiagSq = diagSq;
                maxArea = area;
            } else if (diagSq == maxDiagSq) {
                maxArea = Math.max(maxArea, area);
            }
        }

        return maxArea;
    }
}