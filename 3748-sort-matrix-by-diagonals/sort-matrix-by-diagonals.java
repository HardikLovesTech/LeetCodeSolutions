class Solution {
    public int[][] sortMatrix(int[][] grid) {
        int n = grid.length;
        Map<Integer, PriorityQueue<Integer>> diagonals = new HashMap<>();

        // Step 1: Group all diagonals using (i - j) as the key
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                int key = i - j;
                diagonals.putIfAbsent(key,
                    new PriorityQueue<>(key >= 0 ? Collections.reverseOrder() : Comparator.naturalOrder())
                );
                diagonals.get(key).add(grid[i][j]);
            }
        }

        // Step 2: Refill grid with sorted diagonals
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                int key = i - j;
                grid[i][j] = diagonals.get(key).poll();
            }
        }

        return grid;

    }
}