// P.S: https://leetcode.com/problems/task-scheduler

// MaxHeap, Counter like function, Queue
class Solution {
    public int leastInterval(char[] tasks, int n) {
        Map<Character, Integer> map = new HashMap<>();
        Queue<int[]> q = new LinkedList<>(); // [cnt, idleTime]
        int time = 0;

        // count the frequency for each chars
        for (char c : tasks){
            map.put(c,map.getOrDefault(c, 0) + 1);
        }

        // Put the frequency in MaxHeap
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Comparator.reverseOrder());
        
        for (Character c: map.keySet()){
            int val = map.get(c);
            maxHeap.add(val);
        }

        while (!q.isEmpty() || !maxHeap.isEmpty()){
            time += 1;
            if (!maxHeap.isEmpty()){
                int cnt = maxHeap.poll() - 1;
                if (cnt != 0){
                    q.add(new int[]{cnt, n + time});
                }
            }
            if (!q.isEmpty() && q.peek()[1] == time){
                maxHeap.offer(q.poll()[0]);
            }
        }
        return time;
    }
}