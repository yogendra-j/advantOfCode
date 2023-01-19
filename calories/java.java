package calories;

import java.io.FileInputStream;
import java.io.IOException;
import java.util.PriorityQueue;
import java.util.Scanner;

public class java {
    public static void main(String[] args) {
        System.out.println("main");
        System.out.println(getMaxCalories());
    }

    private static int getMaxCalories() {
        PriorityQueue<Integer> max_cals = new PriorityQueue<>();
        int cur_sum = 0;
        try (
                FileInputStream inputStream = new FileInputStream("input.txt");
                Scanner sc = new Scanner(inputStream, "UTF-8");) {
            
            while (sc.hasNextLine()) {
                String line = sc.nextLine();
                if (line.isBlank()) {
                    max_cals.offer(cur_sum);
                    if (max_cals.size() == 4) max_cals.poll();
                    cur_sum = 0;
                } else {
                    cur_sum += Integer.parseInt(line);
                }
            }
            // note that Scanner suppresses exceptions
            if (sc.ioException() != null) {
                throw sc.ioException();
            }
        } catch (IOException e) {
            e.printStackTrace();
        }

        return max_cals.stream().reduce(0, (sum, cur) -> sum + cur);
    }
}