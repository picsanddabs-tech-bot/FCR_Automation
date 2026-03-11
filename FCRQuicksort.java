public class FCRQuicksort {
    
    // Method to perform quicksort
    public static void quickSort(int[] array, int begin, int end) {
        if (begin < end) {
            int partitionIndex = partition(array, begin, end);
            quickSort(array, begin, partitionIndex-1);
            quickSort(array, partitionIndex+1, end);
        }
    }

    // Method to find the partition position
    private static int partition(int[] array, int begin, int end) {
        int pivot = array[end];
        int i = (begin-1);

        for (int j = begin; j < end; j++) {
            if (array[j] <= pivot) {
                i++;
                int swapTemp = array[i];
                array[i] = array[j];
                array[j] = swapTemp;
            }
        }

        int swapTemp = array[i+1];
        array[i+1] = array[end];
        array[end] = swapTemp;

        return i+1;
    }

    // Main method to test the quicksort implementation
    public static void main(String[] args) {
        int[] numbers = {10, 7, 8, 9, 1, 5};
        int size = numbers.length;
        quickSort(numbers, 0, size-1);
        System.out.println("Sorted array: ");
        for (int number : numbers) {
            System.out.print(number + " ");
        }
    }
}
