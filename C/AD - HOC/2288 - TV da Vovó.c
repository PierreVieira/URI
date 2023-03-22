/*
 * Autor: Pierre Vieira
 * Data de submissão: 22/03/2023 00:16:20
 */

#include <stdio.h>

#define MAX_SIZE 1001

int rows, cols, image[MAX_SIZE][MAX_SIZE];

void readImage() {
    for (int i = 0; i < rows; i++)
        for (int j = 0; j < cols; j++)
            scanf("%d", &image[i][j]);
}

void applyShift(int *horizontalShift, int *verticalShift) {
    int a, b;
    while (scanf("%d %d", &a, &b) == 2 && (a || b)) {
        *horizontalShift += a;
        *verticalShift += b;
    }
    *verticalShift = -*verticalShift;
}

void printShiftedImage(int horizontalShift, int verticalShift, int testNumber) {
    int shiftedRow, shiftedCol;

    printf("Teste %d\n", testNumber);
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            if (j != 0)
                printf(" ");
            shiftedRow = (rows + (i - verticalShift) % rows) % rows;
            shiftedCol = (cols + (j - horizontalShift) % cols) % cols;
            printf("%d", image[shiftedRow][shiftedCol]);
        }
        printf("\n");
    }
    printf("\n");
}

int main() {
    int horizontalShift, verticalShift, testNumber = 1;

    while (scanf("%d %d", &rows, &cols) == 2 && rows) {
        readImage();

        horizontalShift = verticalShift = 0;
        applyShift(&horizontalShift, &verticalShift);

        printShiftedImage(horizontalShift, verticalShift, testNumber++);
    }

    return 0;
}