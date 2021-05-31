import java.io.*;
import java.util.ArrayList;
import java.util.List;
import java.util.Random;

public class GenerateData {

    private static final int MAX_BUCKET_CAPACITY = 10;
    private static final int MIN_BUCKET_CAPACITY = 2;
    private static final int BUCKETS_COUNT = 500;

    public static void main(String[] args) throws IOException {
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(new File("src/main/java/buckets.txt")));
        BufferedReader bufferedReader = new BufferedReader(new FileReader(new File("src/main/java/items.txt")));
        List<String> list = new ArrayList<>();
        while (bufferedReader.ready()) {
            String string = bufferedReader.readLine();
            list.add(string);
        }

        for (int i = 0; i < BUCKETS_COUNT; i++) {
            int volume = randomValue(MIN_BUCKET_CAPACITY, MAX_BUCKET_CAPACITY);
            for (int j = 0; j < volume; j++) {
                int id = randomValue(list.size() - 1, 0);
                bufferedWriter.write(list.get(id) + " ");
            }
            bufferedWriter.write("\n");
        }
        bufferedWriter.flush();
    }

    public static int randomValue(int min, int max) {
        return (int) (Math.random() * (max - min) + min);
    }
}
