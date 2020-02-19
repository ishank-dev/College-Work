//book program using arraylist
import java.util.*;

class Book implements Comparable<Book> {

    String title, author, publisher;
    Double price;
    Book(String t, String aut, String pub, Double pr) {
        title = t;
        author = aut;
        publisher = pub;
        price = pr;
    }
    
    Double getPrice() {
        return price;
    }
    
    public String toString() {
        return "\nTitle: " + title + "\nAuthor: " + author + "\nPublisher:" + publisher + "\nPrice:" + price;
    }
    
    public int compareTo(Book b) {
        return getPrice().compareTo(b.getPrice());
    }
}

public class BookStore {
    public static void main(String[] args) {
        ArrayList<Book> alist = new ArrayList<Book>();
        alist.add(new Book("Title 1", "Author 1", "Publisher 1", 1234.00));
        alist.add(new Book("Title 2", "Author 2", "Publisher 2", 12345.00));
        alist.add(new Book("Title 3", "Author 3", "Publisher 3", 123456.00));
        
        ArrayList<Book> slist = new ArrayList<Book>(alist);
        Collections.sort(slist);
        System.out.println("Sorted List");
        for(int i = 0; i < slist.size(); i++)
        {
            System.out.println(slist.get(i));
        }
        for(int i = 0; i < alist.size(); i++)
        {
            System.out.println(alist.get(i));
        }
    }
}


