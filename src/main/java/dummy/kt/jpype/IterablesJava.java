package dummy.kt.jpype;

import org.jetbrains.annotations.NotNull;

import java.util.Iterator;

public class IterablesJava {
    public static Iterable<Integer> intRange(int min, int max) {
        return new Iterable<Integer>() {
            @NotNull
            @Override
            public Iterator<Integer> iterator() {
                return new Iterator<Integer>() {
                    private int x = min;

                    @Override
                    public boolean hasNext() {
                        return x < max;
                    }

                    @Override
                    public Integer next() {
                        return x++;
                    }
                };
            }
        };
    }
}
