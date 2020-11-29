public static void main(String[] args) {
        int[] testArray = {32, -3, 99, 71, 1, -5, 0, 8, 44};
        quickSort(0, testArray.length - 1, testArray);
        Arrays.stream(testArray).forEach(el -> System.out.print(el + " "));
}
public static void quickSort(int begin, int end, int[] array) {
        if (array.length == 0 || end <= begin) {
                return;
        }
        int pivot = array[(begin + end) / 2];
        int b = begin, e = end;
        while (b <= e) {
                while (array[b] < pivot) {
                        b++;
                }
                while (array[e] > pivot) {
                        e--;
                }
                if (b <= e) {
                        int temp = array[b];
                        array[b++] = array[e];
                        array[e--] = temp;
                }
        }
        
        if (begin < e) {
                quickSort(begin, e, array);
        }
        if (end > b) {
                quickSort(b, end, array);
        }
}
