#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct Book {
    int book_number;
    int id;
    char title[100];
    char author[100];
};

void addBook() {
    struct Book b;
    FILE *fp = fopen("library.txt", "a");

    printf("Enter Book Number: ");
    scanf("%d", &b.book_number);
    printf("Enter Book ID: ");
    scanf("%d", &b.id);
    getchar();
    printf("Enter Title: ");
    fgets(b.title, sizeof(b.title), stdin);
    printf("Enter Author: ");
    fgets(b.author, sizeof(b.author), stdin);

    fprintf(fp, "%d %d %s%s", b.book_number, b.id, b.title, b.author);
    fclose(fp);

    printf("Book added.\n");
}

void viewBooks() {
    FILE *fp = fopen("library.txt", "r");
    if (fp == NULL) {
        printf("No books found.\n");
        return;
    }

    int book_number, id;
    char title[100], author[100];

    printf("\nAvailable Books:\n");
    while (fscanf(fp, "%d %d %[^\n] %[^\n]", &book_number, &id, title, author) == 4) {
        printf("Book Number: %d\n", book_number);
        printf("Book ID: %d\n", id);
        printf("Title: %s\n", title);
        printf("Author: %s\n", author);
        printf("---------------------\n");
    }

    fclose(fp);
}

void issueBook(char librarian[]) {
    int book_number;
    printf("Enter Book Number to issue: ");
    scanf("%d", &book_number);

    FILE *fp = fopen("issued_books.txt", "a");
    fprintf(fp, "%s %d\n", librarian, book_number);
    fclose(fp);

    printf("Book number %d issued to %s\n", book_number, librarian);
}

void viewIssuedBooks(char librarian[]) {
    FILE *fp = fopen("issued_books.txt", "r");
    if (fp == NULL) {
        printf("No issued books.\n");
        return;
    }

    char name[50];
    int book_number;
    int found = 0;

    printf("\nBooks issued to %s:\n", librarian);
    while (fscanf(fp, "%s %d", name, &book_number) == 2) {
        if (strcmp(name, librarian) == 0) {
            printf("Book Number: %d\n", book_number);
            found = 1;
        }
    }

    if (!found)
        printf("No books issued to you.\n");

    fclose(fp);
}

int main() {
    char username[50], password[20];
    const char correct_pass[] = "admin123";

    printf("Librarian Login\n");
    printf("Enter username: ");
    fgets(username, sizeof(username), stdin);
    username[strcspn(username, "\n")] = 0;

    printf("Enter password: ");
    fgets(password, sizeof(password), stdin);
    password[strcspn(password, "\n")] = 0;

    if (strcmp(password, correct_pass) != 0) {
        printf("Incorrect password. Access denied.\n");
        return 0;
    }

    int choice;
    while (1) {
        printf("\nLibrary Menu:\n");
        printf("1. Add Book\n");
        printf("2. View All Books\n");
        printf("3. Issue Book\n");
        printf("4. View My Issued Books\n");
        printf("5. Exit\n");
        printf("Enter choice: ");
        scanf("%d", &choice);
        getchar();

        switch (choice) {
            case 1: addBook(); break;
            case 2: viewBooks(); break;
            case 3: issueBook(username); break;
            case 4: viewIssuedBooks(username); break;
            case 5: printf("Exiting.\n"); return 0;
            default: printf("Invalid choice.\n");
        }
    }

    return 0;
}
