#include <stdbool.h>
#include <stdio.h>

int bubblesort(int *nums, int length) {
	for (int i = 0; i < length; i++) {
		bool sorted = true;
		for (int j = 0; j < length-1; j++) {
			if (nums[j] > nums[j+1]) {
				sorted = false;
				int key = nums[j];
				nums[j] = nums[j+1];
				nums[j+1] = key;
			}
		}
		if (sorted == true) {
			break;
		}
	}
}

int sumlist(int *nums, int length) {
    int sum = 0;
	for (int i = 0; i < length; i++) {
		sum += nums[i];
	}

    return sum;
}
